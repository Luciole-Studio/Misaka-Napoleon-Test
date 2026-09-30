#!/usr/bin/env python3
"""Anna's Archive — search & download books and articles.

Port of https://github.com/iosifache/annas-mcp to Python.
Scrapes Anna's Archive HTML for search, uses fast_download API for downloads.
Dependencies: beautifulsoup4, requests
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.parse
import tempfile
import zipfile
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print(json.dumps({
        "status": "error",
        "error": "需要安装依赖: pip3 install requests beautifulsoup4",
    }))
    sys.exit(1)

FALLBACK_DOMAINS = [
    "annas-archive.gl",
    "annas-archive.pk",
    "annas-archive.gd",
]
DEFAULT_OUTPUT_ROOT = os.environ.get("HERMES_OUTPUT_ROOT", os.path.expanduser("~/Documents/Hermes"))
DEFAULT_DOWNLOAD_DIR = os.environ.get("HERMES_ANNAS_DOWNLOAD_DIR", os.path.join(DEFAULT_OUTPUT_ROOT, "downloads", "annas-archive"))
# Skill-local config/state; migrated from legacy OpenClaw credential storage.
_SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.abspath(os.path.join(_SKILL_DIR, "..", "config.json"))

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)

SCIDB_URL = "https://zh.{base}/scidb/{doi}"
MD5_URL = "https://{base}/md5/{hash}"
FAST_DOWNLOAD_URL = "https://{base}/dyn/api/fast_download.json?md5={hash}&key={key}"
SCIDB_DOWNLOAD_URL = "https://zh.{base}/scidb?doi={doi}"
SITE_NAME = r"(?:Anna[’']s Archive|安娜的档案)"


def _get_session():
    """Create a requests session with browser-like headers."""
    s = requests.Session()
    s.headers.update({
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    })
    # Keep certificate verification enabled, including credentialed requests.
    return s


def _get_config():
    """Load saved skill-local config (base_url, secret_key)."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


class AnnasError(Exception):
    """Machine-readable failure; page challenges are never empty search results."""
    def __init__(self, code, message, **details):
        super().__init__(message)
        self.result = {"status": "error", "code": code, "error": message, **details}


def _normalise_base(value):
    raw = value.strip()
    u = urllib.parse.urlsplit(raw if "://" in raw else "https://" + raw)
    if (u.scheme != "https" or u.hostname not in FALLBACK_DOMAINS or
            u.username or u.password or u.port not in (None, 443) or
            u.path not in ("", "/") or u.query or u.fragment):
        raise AnnasError("untrusted_domain", "Use a currently verified Anna's Archive HTTPS domain.")
    return u.hostname


def _candidate_bases(base_url=None):
    configured = base_url or os.environ.get("ANNAS_BASE_URL") or _get_config().get("base_url")
    # An explicit pin must not silently send requests or credentials to another host.
    return [_normalise_base(configured)] if configured else list(FALLBACK_DOMAINS)


def _get_base_url():
    return _candidate_bases()[0]


def _resolve_base(base_url=None):
    return _candidate_bases(base_url)[0]


def _validate_site_url(url):
    u = urllib.parse.urlsplit(url)
    hosts = {d for d in FALLBACK_DOMAINS} | {"zh." + d for d in FALLBACK_DOMAINS}
    if u.scheme != "https" or u.hostname not in hosts or u.username or u.password or u.port not in (None, 443):
        raise AnnasError("untrusted_redirect", "Page redirected outside verified Anna's Archive hosts.")
    return url


def _page_response(session, url):
    # Validate each redirect before visiting it; never follow parked-domain redirects.
    for _ in range(5):
        _validate_site_url(url)
        response = session.get(url, timeout=25, allow_redirects=False)
        if response.status_code not in (301, 302, 303, 307, 308):
            return response
        location = response.headers.get("Location")
        response.close()
        if not location:
            raise AnnasError("invalid_redirect", "Redirect has no Location header.")
        url = urllib.parse.urljoin(url, location)
    raise AnnasError("redirect_loop", "Too many page redirects.")


def _checked_soup(html, url, status_code=200):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    page_text = soup.get_text(" ", strip=True)
    challenge = (title.lower().strip() in ("ddos-guard", "just a moment...", "attention required! | cloudflare")
                 or ("Checking your browser before accessing" in page_text and "Anna" not in title))
    if status_code == 429:
        raise AnnasError("rate_limited", "Upstream rate limit; do not loop or rotate identities.", http_status=429)
    if challenge or status_code == 403:
        raise AnnasError("browser_required", "The HTTP page is blocked; continue in the existing local browser.",
                         browser_required=True, browser_url=url, http_status=status_code)
    if status_code >= 400:
        raise AnnasError("http_error", "Anna's Archive returned HTTP " + str(status_code), http_status=status_code)
    if not re.search(SITE_NAME, title, re.I):
        raise AnnasError("unexpected_page", "Response is not a verified Anna's Archive content page.", browser_url=url)
    for link in soup.find_all("a", href=True):
        href = urllib.parse.urlsplit(link["href"])
        if href.scheme == "https" and href.hostname in FALLBACK_DOMAINS and not href.username and not href.password and href.port in (None, 443):
            link["href"] = urllib.parse.urlunsplit(("", "", href.path, href.query, href.fragment))
    return soup


def _login_session(session, base):
    """Use the existing key via the site's normal login, never the download API.

    The account cookie remains in this in-memory session only. Membership controls
    whether protected pages accept it; no browser state is imported or persisted.
    """
    key = _get_secret_key()
    if not key:
        return False
    base = _normalise_base(base)
    url = "https://" + base + "/account/"
    with session.post(url, data={"key": key}, timeout=25, allow_redirects=False) as response:
        if response.status_code == 429:
            raise AnnasError("rate_limited", "Account login is rate limited; do not retry automatically.", http_status=429)
        if response.status_code not in (302, 303):
            raise AnnasError("login_failed", "The configured key did not establish an account session.", http_status=response.status_code)
        target = urllib.parse.urlsplit(urllib.parse.urljoin(url, response.headers.get("Location", "")))
        if (target.scheme != "https" or target.hostname != base or target.username or target.password
                or target.port not in (None, 443) or target.path not in ("/account", "/account/") or target.query or target.fragment):
            raise AnnasError("login_redirect", "Unexpected login redirect was not followed.")
        if not any(c.name == "aa_account_id2" and c.domain.lstrip(".") == base and not c.is_expired()
                   for c in session.cookies):
            raise AnnasError("login_failed", "Login did not return the expected account session cookie.")
    return True


def _fetch_page(path, base_url=None, *, subdomain=""):
    attempts = []
    bases = _candidate_bases(base_url)
    for base in bases:
        url = "https://" + subdomain + base + path
        try:
            with _get_session() as session:
                # Credentials go only to the selected primary host. Mirror fallbacks
                # stay anonymous unless explicitly selected via --domain/config.
                if base == bases[0]:
                    _login_session(session, base)
                response = _page_response(session, url)
                try:
                    soup = _checked_soup(response.text, response.url, response.status_code)
                    return soup, base, response.url
                finally:
                    response.close()
        except AnnasError as exc:
            attempts.append({"domain": base, **exc.result})
            if exc.result["code"] in ("rate_limited", "login_failed", "login_redirect"):
                raise
        except requests.RequestException as exc:
            attempts.append({"domain": base, "code": "network_error", "error": type(exc).__name__})
    blocked = any(a.get("code") == "browser_required" for a in attempts)
    raise AnnasError("browser_required" if blocked else "fetch_failed",
                     "No verified HTTP page was obtained; results are unknown, not empty.",
                     attempts=attempts, browser_required=blocked,
                     browser_url="https://" + subdomain + bases[0] + path)


def _redact_error(error):
    message = str(error)
    try:
        key = _get_secret_key()
        if key:
            message = message.replace(key, "[REDACTED]")
    except (OSError, ValueError):
        pass
    return re.sub(r"([?&](?:key|token|secret_key)=)[^&\s]+", r"\1[REDACTED]", message, flags=re.I)


def _get_secret_key():
    config = _get_config()
    return os.environ.get("ANNAS_SECRET_KEY") or config.get("secret_key") or ""


def _safe_filename(text, max_len=150):
    """Create filesystem-safe filename."""
    safe = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', text)
    safe = safe.replace('..', '_')
    safe = safe.strip('. ')
    if len(safe) > max_len:
        safe = safe[:max_len]
    return safe or "untitled"


def _extract_meta(meta_text):
    """Parse meta string like '✅ English [en] · PDF · 12.3MB' into parts."""
    parts = meta_text.split('·')
    language = ""
    fmt = ""
    size = ""

    if parts:
        lang_part = parts[0].strip()
        # Remove checkmark and brackets
        lang_part = re.sub(r'[✅✓]', '', lang_part).strip()
        if '[' in lang_part:
            language = lang_part[:lang_part.index('[')].strip()
        else:
            language = lang_part

    fmt_re = re.compile(r'\b(EPUB|PDF|MOBI|AZW3?|DJVU|CBZ|CBR|FB2|DOCX?|TXT)\b', re.I)
    size_re = re.compile(r'[\d.]+\s*(MB|KB|GB|TB)', re.I)

    for part in parts[1:]:
        part = part.strip()
        if not fmt:
            m = fmt_re.search(part)
            if m:
                fmt = m.group(1).upper()
        if not size:
            m = size_re.search(part)
            if m:
                size = m.group(0)

    return language, fmt, size


# ── Search ────────────────────────────────────────────────────────────

def _parse_result_cards(soup, base):
    """Parse search result cards from BS4 soup. Works for both books and articles."""
    items = []
    seen = set()
    # Select only outer card links (have 'block' class), not inner title links
    for link in soup.select('a[href^="/md5/"].custom-a.block'):
        parent = link.parent
        if not parent:
            continue

        info_div = parent.select_one("div.max-w-full")
        if not info_div:
            continue

        # Title
        title_el = info_div.select_one('a[href^="/md5/"]')
        title = title_el.get_text(strip=True) if title_el else ""
        if not title:
            continue

        # Authors — look for user-edit icon span's parent <a>
        authors = ""
        for a_tag in info_div.select('a[href^="/search"]'):
            if a_tag.select_one('span[class*="user-edit"]'):
                authors = a_tag.get_text(strip=True)
                break

        # Publisher / Journal
        publisher = ""
        for a_tag in info_div.select('a[href^="/search"]'):
            if a_tag.select_one('span[class*="company"]'):
                publisher = a_tag.get_text(strip=True)
                break

        # Meta (language, format, size)
        meta_div = info_div.select_one("div.text-gray-800")
        language, fmt, size = "", "", ""
        if meta_div:
            language, fmt, size = _extract_meta(meta_div.get_text())

        # Hash from href
        href = link.get("href", "")
        md5_hash = urllib.parse.urlsplit(href).path.removeprefix("/md5/").lower()
        if not re.fullmatch(r"[a-f0-9]{32}", md5_hash) or md5_hash in seen:
            continue
        seen.add(md5_hash)

        items.append({
            "title": title,
            "authors": authors,
            "publisher": publisher,
            "language": language,
            "format": fmt,
            "size": size,
            "hash": md5_hash,
            "url": f"https://{base}/md5/{md5_hash}",
        })

    return items


def _search_result(soup, query, base, url, *, transport="http", articles=False):
    search_body = soup.select_one("main") or soup
    items = _parse_result_cards(search_body, base)
    if not items:
        # Positive evidence of zero hits, not merely a parser that found no cards.
        text = search_body.get_text(" ", strip=True)
        if search_body.select('a[href^="/md5/"]') or not re.search(
                r"(?:no (?:files|results|books) found|0 results|results 0[-–]0|没有找到|未找到相关)", text, re.I):
            raise AnnasError("unrecognised_search_page", "Search structure is missing or changed; zero hits are not established.", browser_url=url)
    if articles:
        for item in items:
            item["journal"] = item.pop("publisher", "")
    return {"status": "ok", "query": query, "domain": base, "count": len(items),
            "results": items, "source_url": url, "transport": transport,
            "scope": "current_page_only", "complete": False}


def _search(query, content, base_url=None):
    params = {"q": query}
    if content == "journal":
        params["index"] = "journals"
    else:
        params["content"] = ["book_nonfiction", "book_fiction", "book_unknown"]
    path = "/search?" + urllib.parse.urlencode(params, doseq=True)
    soup, base, url = _fetch_page(path, base_url)
    return _search_result(soup, query, base, url, articles=content == "journal")


def search_books(query, base_url=None):
    return _search(query, "book_any", base_url)


def search_articles(query, base_url=None):
    if query.startswith("10."):
        return lookup_doi(query, base_url)
    return _search(query, "journal", base_url)


def parse_search_file(filename, source_url, query, articles=False):
    """Import public HTML exported from a normal browser; never read its cookies."""
    _validate_site_url(source_url)
    u = urllib.parse.urlsplit(source_url)
    if u.path != "/search" or urllib.parse.parse_qs(u.query).get("q") != [query]:
        raise AnnasError("source_mismatch", "The supplied search URL must match this query.")
    soup = _checked_soup(Path(filename).read_text(encoding="utf-8"), source_url)
    return _search_result(soup, query, u.hostname, source_url, transport="rendered_html", articles=articles)


# ── DOI Lookup ────────────────────────────────────────────────────────

def lookup_doi(doi, base_url=None):
    """Look up a paper by DOI via SciDB."""
    path = "/scidb/" + urllib.parse.quote(doi, safe="/")
    soup, base, scidb_url = _fetch_page(path, base_url, subdomain="zh.")
    md5_hash = ""
    for a_tag in soup.select('a[href^="/md5/"]'):
        href = a_tag.get("href", "")
        h = href.replace("/md5/", "")
        if re.fullmatch(r"[a-fA-F0-9]{32}", h):
            md5_hash = h.lower()
            break

    if not md5_hash:
        return {"status": "error", "error": f"DOI not found: {doi}"}

    # Step 2: Detail page for metadata
    paper = {
        "doi": doi,
        "hash": md5_hash,
        "page_url": scidb_url,
        "download_url": f"/scidb?doi={doi}",
    }

    detail_url = MD5_URL.format(base=base, hash=md5_hash)
    try:
        soup2, _, _ = _fetch_page("/md5/" + md5_hash, base)
        detail = _detail_result(soup2, md5_hash, detail_url)["detail"]
        paper.update({key: detail[key] for key in ("title", "authors", "size") if key in detail})

        # Journal from meta description
        meta_desc = soup2.find("meta", attrs={"name": "description"})
        if meta_desc:
            desc = meta_desc.get("content", "")
            parts = desc.split("\n\n")
            if len(parts) >= 3:
                paper["journal"] = parts[2].strip()
            elif len(parts) >= 2:
                paper["journal"] = parts[1].strip()

    except (AnnasError, requests.RequestException) as exc:
        paper["detail_warning"] = _redact_error(exc)

    return {"status": "ok", "paper": paper}


# ── Detail ────────────────────────────────────────────────────────────

def get_detail(md5_hash, base_url=None):
    """Get book/article details by MD5 hash."""
    md5_hash = _valid_hash(md5_hash)
    soup, base, url = _fetch_page("/md5/" + md5_hash, base_url)
    return _detail_result(soup, md5_hash, url)


def parse_detail_file(filename, source_url, md5_hash):
    md5_hash = _valid_hash(md5_hash)
    _validate_site_url(source_url)
    if urllib.parse.urlsplit(source_url).path != "/md5/" + md5_hash:
        raise AnnasError("source_mismatch", "The supplied detail URL must match this MD5.")
    soup = _checked_soup(Path(filename).read_text(encoding="utf-8"), source_url)
    result = _detail_result(soup, md5_hash, source_url)
    result["transport"] = "rendered_html"
    return result


def _detail_result(soup, md5_hash, url):
    info = {"hash": md5_hash, "url": url}

    # Title
    title_tag = soup.find("title")
    if title_tag:
        info["title"] = re.sub(r"\s+-\s+" + SITE_NAME + r"\s*$", "", title_tag.get_text(), flags=re.I).strip()

    # Authors
    for a_tag in soup.select('a[href^="/search"]'):
        if a_tag.select_one('span[class*="user-edit"]'):
            info["authors"] = a_tag.get_text(strip=True)
            break

    # Publisher
    for a_tag in soup.select('a[href^="/search"]'):
        if a_tag.select_one('span[class*="company"]'):
            info["publisher"] = a_tag.get_text(strip=True)
            break

    # Meta description
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc:
        info["description"] = meta_desc.get("content", "").strip()

    # All text-gray-500 divs for additional metadata
    for div in soup.select("div.text-gray-500"):
        text = div.get_text(strip=True)
        if "MB" in text or "KB" in text or "GB" in text:
            info["size"] = text
        elif "ISBN" in text:
            info["isbn"] = text

    # Download links
    download_links = []
    for a_tag in soup.select('a[href*="download"], a[href*="fast_download"]'):
        href = a_tag.get("href", "")
        text = a_tag.get_text(strip=True)
        if href and text:
            absolute = urllib.parse.urljoin(url, href)
            if urllib.parse.urlsplit(absolute).path.startswith(("/fast_download/", "/slow_download/")):
                download_links.append({"text": text, "url": absolute})
    if download_links:
        info["download_links"] = download_links

    if (not info.get("title") or info["title"].lower() in ("anna's archive", "anna’s archive", "安娜的档案", "not found", "404", "error")
            or not soup.select_one("#md5-panel-downloads, #md5-tab-details")):
        raise AnnasError("unrecognised_detail_page", "No identifiable record title was obtained.", browser_url=url)
    return {"status": "ok", "detail": info}


# ── Download ──────────────────────────────────────────────────────────

def _valid_hash(value):
    if not re.fullmatch(r"[a-fA-F0-9]{32}", value):
        raise AnnasError("invalid_md5", "Expected the 32-character MD5 from a verified record.")
    return value.lower()


def _file_md5(path):
    digest = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _verify_file(path, fmt, expected_md5=None):
    with open(path, "rb") as f:
        head = f.read(1024)
        f.seek(max(0, os.fstat(f.fileno()).st_size - 2048))
        tail = f.read()
    if not head or head.lstrip().lower().startswith((b"<!doctype html", b"<html")):
        raise AnnasError("invalid_download", "Downloaded content is empty or an HTML page.")
    if fmt == "pdf" and (b"%PDF-" not in head or b"%%EOF" not in tail):
        raise AnnasError("invalid_download", "PDF signature or end marker is missing.")
    if fmt == "epub":
        if not zipfile.is_zipfile(path):
            raise AnnasError("invalid_download", "EPUB is not a ZIP container.")
        with zipfile.ZipFile(path) as z:
            try:
                with z.open("mimetype") as f:
                    mime = f.read(128)
            except KeyError:
                mime = b""
            if mime.strip() != b"application/epub+zip":
                raise AnnasError("invalid_download", "EPUB mimetype is missing or incorrect.")
    actual = _file_md5(path)
    if expected_md5 and actual != expected_md5:
        raise AnnasError("checksum_mismatch", "Downloaded bytes do not match the requested record MD5.")
    return actual


def _download_path(outdir, title, fmt, md5_hash):
    if not re.fullmatch(r"[a-z0-9]{1,10}", fmt):
        raise AnnasError("invalid_format", "Invalid output format.")
    directory = Path(outdir or _get_config().get("download_dir") or DEFAULT_DOWNLOAD_DIR).expanduser()
    directory.mkdir(parents=True, exist_ok=True)
    name = _safe_filename(title) if title else "untitled"
    # Preserve legacy paths when already complete; do not overwrite another edition.
    legacy = directory / (name + "." + fmt)
    if legacy.is_file() and _file_md5(legacy) == md5_hash:
        return legacy
    return directory / (name + "__" + md5_hash[:12] + "." + fmt)


def _saved_result(path, fmt, md5_hash, *, skipped=False):
    actual = _verify_file(path, fmt, md5_hash)
    size = path.stat().st_size
    return {"status": "ok", "file": str(path), "filename": path.name, "size_bytes": size,
            "size_human": _human_size(size), "md5": actual, "verified": True, "skipped_existing": skipped}


def _fast_url(session, md5_hash):
    key = _get_secret_key()
    if not key:
        raise AnnasError("missing_key", "Fast downloads require an existing member API key.")
    # Exactly one approved host; never propagate a credential across redirects or mirrors.
    base = _resolve_base()
    url = FAST_DOWNLOAD_URL.format(base=base, hash=md5_hash, key=urllib.parse.quote(key, safe=""))
    with session.get(url, timeout=30, allow_redirects=False) as response:
        if 300 <= response.status_code < 400:
            raise AnnasError("api_redirect", "Credentialed API redirect was not followed.")
        try:
            data = response.json()
        except ValueError:
            raise AnnasError("api_non_json", "Fast Download API returned a non-JSON page.", http_status=response.status_code)
        if not isinstance(data, dict):
            raise AnnasError("api_schema", "Fast Download API returned an unexpected JSON shape.")
        if data.get("error"):
            message = _redact_error(data["error"])
            code = {"Not a member": "not_a_member", "Invalid key": "invalid_key"}.get(message, "api_error")
            raise AnnasError(code, message, http_status=response.status_code)
        if response.status_code >= 400 or not data.get("download_url"):
            raise AnnasError("api_error", "Fast Download API did not supply a file URL.", http_status=response.status_code)
        return data["download_url"]


def _store_download(session, url, path, fmt, md5_hash):
    # This path carries no account key. Validate transport on every partner redirect.
    for _ in range(6):
        u = urllib.parse.urlsplit(url)
        if u.scheme != "https" or not u.hostname or u.username or u.password:
            raise AnnasError("invalid_download_url", "File URLs must use HTTPS without embedded credentials.")
        response = session.get(url, timeout=120, stream=True, allow_redirects=False)
        if response.status_code in (301, 302, 303, 307, 308):
            location = response.headers.get("Location")
            response.close()
            if not location:
                raise AnnasError("invalid_redirect", "File redirect has no Location header.")
            url = urllib.parse.urljoin(url, location)
            continue
        break
    else:
        raise AnnasError("redirect_loop", "Too many file redirects.")
    tmp = None
    try:
        if response.status_code >= 400:
            raise AnnasError("download_http_error", "File server returned HTTP " + str(response.status_code))
        if "text/html" in response.headers.get("Content-Type", "").lower():
            raise AnnasError("invalid_download", "File server returned HTML, not a book.")
        fd, tmp = tempfile.mkstemp(prefix=".annas-", suffix=".part", dir=path.parent)
        with os.fdopen(fd, "wb") as f:
            for chunk in response.iter_content(chunk_size=65536):
                if chunk:
                    f.write(chunk)
        _verify_file(tmp, fmt, md5_hash)
        # Atomic no-clobber publish. Another download's result is never overwritten.
        try:
            os.link(tmp, path)
        except FileExistsError:
            return _saved_result(path, fmt, md5_hash, skipped=True)
        return _saved_result(path, fmt, md5_hash)
    finally:
        response.close()
        if tmp:
            Path(tmp).unlink(missing_ok=True)


def download_book(md5_hash, title="", fmt="pdf", outdir=None):
    md5_hash = _valid_hash(md5_hash)
    fmt = fmt.lower()
    path = _download_path(outdir, title, fmt, md5_hash)
    if path.exists():
        return _saved_result(path, fmt, md5_hash, skipped=True)
    with _get_session() as session:
        return _store_download(session, _fast_url(session, md5_hash), path, fmt, md5_hash)


def download_article(doi, outdir=None):
    result = lookup_doi(doi)
    if result.get("status") != "ok":
        return result
    paper = result["paper"]
    md5_hash = _valid_hash(paper["hash"])
    if _get_secret_key():
        try:
            result = download_book(md5_hash, title=paper.get("title", doi), outdir=outdir)
            result["method"] = "fast_download"
            return result
        except AnnasError as exc:
            if exc.result["code"] not in ("not_a_member", "invalid_key"):
                raise
    path = _download_path(outdir, paper.get("title", doi), "pdf", md5_hash)
    if path.exists():
        return _saved_result(path, "pdf", md5_hash, skipped=True)
    url = SCIDB_DOWNLOAD_URL.format(base=_resolve_base(), doi=urllib.parse.quote(doi, safe="/"))
    with _get_session() as session:
        result = _store_download(session, url, path, "pdf", md5_hash)
    result["method"] = "scidb"
    return result


def _human_size(b):
    for u in ("B", "KB", "MB", "GB"):
        if b < 1024:
            return f"{b:.1f} {u}"
        b /= 1024
    return f"{b:.1f} TB"


# ── SciDB (独立入口，无需 API key) ────────────────────────────────────

# ── Domains ───────────────────────────────────────────────────────────

def probe_domains():
    """A known search must produce records; a responsive homepage is insufficient."""
    results = []
    for base in FALLBACK_DOMAINS:
        start = time.monotonic()
        try:
            result = search_books("Pride and Prejudice", base)
            results.append({"domain": base, "up": result["count"] > 0,
                            "search_count": result["count"], "latency_ms": round((time.monotonic()-start)*1000)})
        except AnnasError as exc:
            results.append({"domain": base, "up": False, **exc.result})
    available = [r["domain"] for r in results if r.get("up")]
    return {"status": "ok" if available else "error", "code": "search_probe", "domains": results,
            "available": available, "recommended": available[0] if available else None}


# ── Config ────────────────────────────────────────────────────────────

def save_config(key=None, base_url=None, download_dir=None):
    """Save configuration to skill-local file."""
    config = _get_config()
    if key:
        config["secret_key"] = key
    if base_url:
        config["base_url"] = _normalise_base(base_url)
    if download_dir:
        config["download_dir"] = download_dir
    config["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(config, f, indent=2)

    return {"status": "ok", "message": "配置已保存", "config_file": STATE_FILE}


# ── CLI ───────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(
        prog="annas",
        description="Anna's Archive — search & download books and articles",
    )
    p.add_argument("--domain", help="指定域名 (如 annas-archive.gl)，不指定则自动探测可用域名")
    sub = p.add_subparsers(dest="action")

    # config
    s = sub.add_parser("config", help="配置 API key / base URL")
    s.add_argument("--key", help="Anna's Archive API key (付费获取)")
    s.add_argument("--base-url", help=f"Base URL (default: {FALLBACK_DOMAINS[0]})")
    s.add_argument("--download-dir", help=f"下载目录 (default: {DEFAULT_DOWNLOAD_DIR})")

    # domains
    sub.add_parser("domains", help="列出/探测可用域名")

    # search-book
    s = sub.add_parser("search-book", help="搜索图书")
    s.add_argument("query", help="搜索关键词")

    # search-article
    s = sub.add_parser("search-article", help="搜索论文 (关键词或DOI)")
    s.add_argument("query", help="关键词或DOI (如 10.1038/nature12345)")

    # doi
    s = sub.add_parser("doi", help="DOI查找")
    s.add_argument("doi", help="DOI (如 10.1038/nature12345)")

    # detail
    s = sub.add_parser("detail", help="查看详情 (by MD5 hash)")
    s.add_argument("hash", help="MD5 hash")

    # download-book
    s = sub.add_parser("download-book", help="下载图书 (需要API key)")
    s.add_argument("hash", help="MD5 hash (来自搜索结果)")
    s.add_argument("--title", default="", help="书名 (用于文件名)")
    s.add_argument("--format", default="pdf", help="格式 (pdf/epub/...)")
    s.add_argument("--outdir", help="下载目录")

    # download-article
    s = sub.add_parser("download-article", help="下载论文 (by DOI, 需API key)")
    s.add_argument("doi", help="DOI")
    s.add_argument("--outdir", help="下载目录")

    s = sub.add_parser("parse-search", help="Parse public search HTML exported by the existing browser")
    s.add_argument("query")
    s.add_argument("--html", required=True)
    s.add_argument("--source-url", required=True)
    s.add_argument("--articles", action="store_true")
    s = sub.add_parser("parse-detail", help="Parse public record HTML exported by the existing browser")
    s.add_argument("hash")
    s.add_argument("--html", required=True)
    s.add_argument("--source-url", required=True)

    args = p.parse_args()
    if not args.action:
        p.print_help()
        sys.exit(1)

    # Apply --domain override via env var so all functions pick it up
    if args.domain:
        os.environ["ANNAS_BASE_URL"] = args.domain

    try:
        if args.action == "config":
            result = save_config(key=args.key, base_url=args.base_url,
                                 download_dir=args.download_dir)
        elif args.action == "domains":
            result = probe_domains()
        elif args.action == "search-book":
            result = search_books(args.query)
        elif args.action == "search-article":
            result = search_articles(args.query)
        elif args.action == "doi":
            result = lookup_doi(args.doi)
        elif args.action == "detail":
            result = get_detail(args.hash)
        elif args.action == "download-book":
            result = download_book(args.hash, title=args.title,
                                   fmt=args.format, outdir=args.outdir)
        elif args.action == "parse-search":
            result = parse_search_file(args.html, args.source_url, args.query, args.articles)
        elif args.action == "parse-detail":
            result = parse_detail_file(args.html, args.source_url, args.hash)
        elif args.action == "download-article":
            result = download_article(args.doi, outdir=args.outdir)
        else:
            result = {"error": f"未知操作: {args.action}"}
    except AnnasError as e:
        result = e.result
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code if e.response is not None else None
        result = {"status": "error", "error": _redact_error(e), "http_status": status_code}
    except Exception as e:
        result = {"status": "error", "error": _redact_error(e)}

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0 if result.get("status") == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())

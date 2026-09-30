#!/usr/bin/env python3
"""Read-only runtime wrapper for the annas-archive skill script.

Loads the skill's annas.py from its read-only task mount, patches the config
lookup to a read-only candidate list (so the existing member key is used as the
skill documents), and executes it unchanged otherwise. No skill-tree writes.
"""
import os, sys, pathlib, json, types

SRC = pathlib.Path('/Users/makiko/.misaka/state/tasks/t_66ee8d/.skills-ro/annas-archive/scripts/annas.py')
CANDIDATES = [
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aa_config.json'),
    '/Users/makiko/.misaka/skills/annas-archive/config.json',
    '/Users/makiko/.misaka/shared/skill-library/repair-20260917T042736Z/skills/research-infra/annas-archive/config.json',
    '/Users/makiko/.misaka/state/tasks/t_66ee8d/.skills-ro/annas-archive/config.json',
]

code = SRC.read_text()

patch_old = '''def _get_config():
    """Load saved skill-local config (base_url, secret_key)."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}'''
patch_new = '''def _get_config():
    """Load saved config from read-only candidate paths (card-local first)."""
    for _p in _AA_CONFIG_CANDIDATES:
        if os.path.exists(_p):
            try:
                with open(_p) as f:
                    return json.load(f)
            except (OSError, ValueError):
                continue
    return {}'''
assert patch_old in code, 'config function shape changed; re-check skill script'
code = code.replace(patch_old, patch_new)

mod = types.ModuleType('annas')
mod.__dict__['_AA_CONFIG_CANDIDATES'] = CANDIDATES
mod.__dict__['__name__'] = 'annas'
mod.__dict__['__file__'] = str(SRC)
exec(compile(code, str(SRC), 'exec'), mod.__dict__)
sys.exit(mod.main())

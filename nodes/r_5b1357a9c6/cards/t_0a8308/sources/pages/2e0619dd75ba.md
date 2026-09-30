---
source_url: "https://www.nber.org/system/files/working_papers/w27904/w27904.pdf"
final_url: "https://www.nber.org/system/files/working_papers/w27904/w27904.pdf"
provider: "exa"
text_sha256: "2b5bdf1c11e5915441417d437f018b27a1dc7f2c32ab810de538df3561da02ca"
title: "October 2020, Revised July 2026"
content_kind: "page_text"
---

NBER WORKING PAPER SERIES

DISTANCE, EMPIRE, AND BRITISH EXPORTS OVER TWO CENTURIES

David S. Jacks 
Kevin Hjortshøj O'Rourke 
Alan M. Taylor 
Yoto V. Yotov 

Working Paper 27904 http://www.nber.org/papers/w27904

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 October 2020, Revised July 2026

We are most grateful to Felipe Benguria, Stephen Carroll, Bo Chen, Nick Dadson, Gabby Domingo, James Ensom, Rowena Gray, Mahmut Ipek, Margaret Kapitany, Sean Kelly, Sean Lee, Alaz Munzur, and Sarah Quincy for excellent research assistance. We appreciate the advice, suggestions, and help with data received from John Darwin, Guillaume Daudin, James Feyrer, Jules Hugot, Morgan Kelly, Thierry Mayer, Chris Meissner, Isabelle Méjean, Anders Mikkelsen, Farid Toubal, David Weinstein, and seminar participants at Huazhong University of Science and Technology, Queen’s University, Sciences Po Paris, the University of New South Wales, the 2019 Canadian Economics Association Annual Meeting, the 2020 Asia-Pacific Economic and Business History Conference, and the 2021 CEPR Economic History Symposium. Bishnu Gupta and three anonymous referees have made numerous suggestions which have helped us to significantly improve the paper. Finally, we gratefully acknowledge research support from the National Science Foundation (award number 0851158) and the Social Science and Humanities Research Council of Canada as well as All Souls College, the All-UC Group in Economic History, the Center for the Evolution of the Global Economy, and the NYU Abu Dhabi Faculty of Social Science. We wish to particularly thank Alison Oaxaca for all her help over the course of this project. The views expressed herein are those of the authors and do not necessarily reflect the views of the National Bureau of Economic Research.

NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications.

© 2020 by David S. Jacks, Kevin Hjortshøj O'Rourke, Alan M. Taylor, and Yoto V. Yotov. All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source.

Distance, Empire, and British Exports Over Two Centuries 
David S. Jacks, Kevin Hjortshøj O'Rourke, Alan M. Taylor, and Yoto V. Yotov 
NBER Working Paper No. 27904 
October 2020, Revised July 2026 
JEL No. F1, N7 

##### ABSTRACT

We introduce a new, publicly available dataset on the universe of British exports at the bilateral, commodity level from 1700 to 1899. We then pit two primary determinants of bilateral trade against one another: the trade-diminishing effects of distance versus the trade-enhancing effects of the British Empire. We find that the impact of distance fell by roughly two-thirds between the 1780s and 1860s. The influence of empire on British exports was very large throughout, but the impact of 18th century mercantilism was much higher than that of "liberal empire" in the late 19th century.

David S. Jacks 
National University of Singapore 
Department of Economics 
and CEPR 
dsjacks@gmail.com 

Kevin Hjortshøj O'Rourke Sciences Po Department of Economics kevin.orourke@sciencespo.fr

Alan M. Taylor Columbia University and CEPR and also NBER amt2314@columbia.edu

Yoto V. Yotov 
Drexel University 
School of Economics 
Department of Economics 
and International Business 
and ERI-BAS 
yotov@drexel.edu 

#### 1 Introduction

International trade has long been a central theme in British economic history, featuring in key debates about the roles of mercantilism in early modern growth and foreign markets during the Industrial Revolution (e.g., Findlay 1982; O’Brien and Engerman, 1991; Temin, 1997; Harley and Crafts, 2000; Allen, 2003). In the decades before World War I, contemporaries pointed to trade statistics as evidence that Britain was falling behind its competitors, and the argument that slowing exports might have caused sluggish British growth was subsequently investigated by a cliometric literature on late Victorian failure (Meyer, 1955; McCloskey, 1970). In this paper, we present a new publicly available database that speaks to these and many other issues, capturing the universe of British exports and providing information on commodity-level flows to 86 consistently-defined destinations between 1700 and 1899.1

Our data make it possible for the first time to quantify the impact of empire and distance – two very important determinants of bilateral trade costs – on British exports during the 18th and 19th centuries, and in particular to show how these impacts varied across sectors and over time. Mercantilism linked empire and trade closely in the 18th century: Allen (2003, p. 414) goes so far as to say that trade was "an exogenous measure of imperial advantage". But how quantitatively significant was this link and how does it compare with the impact of imperial ties in the post-mercantilist 19th century? Our data can help us distinguish between the impact on British exports of mercantilism on the one hand and free trade imperialism on the other, as well as allow us to determine when the transition between the two regimes began. There is a large literature on the impact of empires on trade. For instance, Mitchener and Weidenmier (2008) use gravity methods to

1We use the term “British” for convenience although it is slightly inaccurate. England and Wales were united with Scotland in 1707, forming the new state of Great Britain. In 1801 Britain and Ireland merged to form the United Kingdom. The issue is further discussed in Section 3.1 below.

explore these effects between 1870 and 1913. Eichengreen and Irwin (1995), Gowa and 
Hicks (2013), de Bromhead et al. (2019), and Jacks and Novy (2020) examine imperial ties 
during the trade bust of the interwar period, while Head, Mayer, and Ries (2010) study the 
erosion of colonial trade relationships post-independence. In contrast, we are able to push 
the analysis of empire and trade all the way back to 1700, the heyday of mercantilism. 
Another literature has emerged over the past two decades which uses contemporary 
data to document and explain the “distance puzzle” whereby the negative impact of 
distance on trade first increased and then failed to decline in the post-1950 period (Coe, 
Subramanian, and Tamirisa, 2007; Yotov, 2012). López-Córdova and Meissner (2003), 
Mitchener and Weidenmier (2008), Jacks, Meissner, and Novy (2011) and others use gravity 
methods to estimate distance coefficients in the late 19th century. Such efforts allowed 
Disdier and Head (2008) to go as far back as 1870 in their meta-analysis of distance effects: 
they document that the distance coefficient was smaller in the late 19th century than it is 
today. But was it even smaller in the 18th century? Or has there been a U-shaped pattern 
of 18th and 19th-century decline followed by a 20th century increase? 
Answers to such questions can potentially speak to debates about the development 
of maritime shipping and freight rates over the course of the past 300 years: when did 
transport costs decline and did they fall because of institutional factors or technological 
change (North, 1958, 1968)? If the latter was more important, then was this largely a 
19th century phenomenon sparked by the introduction of new technologies related to the 
Industrial Revolution (Harley, 1988)? Or did earlier technological progress, documented 
by a more recent literature and due largely to the coppering of ships, which increased both 
their longevity and speed, also have an impact (Solar and Rönnbäck, 2015)? Studying the 
changing impact of distance on British exports over time can provide further evidence to 
illuminate this issue. 
We also ask whether these impacts varied across sectors. Much of the gravity literature 

contents itself with estimating mean effects, but as Larch, Shikher, and Yotov (2025) stress, 
heterogeneity is frequently an important dimension of the data with elasticities not being 
constant either across sectors or over time. The impact of a variable such as distance or 
empire on trade depends on two elasticities: the elasticity of trade costs with respect to 
the variable in question and the elasticity of trade with respect to trade costs (Disdier and 
Head, 2008, p. 41). Both of these elasticities might be expected to vary across sectors and 
time. 
Take for example the argument of Magee and Thompson (2010) that empire mattered 
for trade flows because of consumer preferences in colonies settled by British emigrants: if 
this is true, then the elasticity of trade costs with respect to empire should be higher for 
consumer products such as food and drink than for a commodity like iron ore. Turning to 
the effects of distance, these should differ depending on the mode and cost of transportation 
which might be different for fuels like coal than for light manufactured goods like cotton 
textiles. As for the elasticity of trade flows with respect to trade costs, one might expect it 
to be higher for homogenous goods than for differentiated products on both counts. 
One would expect elasticities to vary not only across sectors but also over time, and 
particularly so in our period, since it saw momentous and almost continuous change. 
Shipping speeds rose from the 1780s, and the maritime shipping industry was transformed 
in the 19th century with the application of new metallurgical and steam technologies. 
Meanwhile, railway construction progressively linked ports to their hinterlands from the 
1830s. As we will see in Section 2.1, late 18th century technological progress tended to 
favour long-distance routes over shorter ones which should have reduced the elasticity of 
trade costs with respect to distance. 
Politically, the 18th century was the era of mercantilism, with constant warfare, a 
web of regulations controlling trade between Britain and her colonies, and the East India 
Company monopolizing British trade with China and India. This was succeeded by a 

period of relative peace after 1815, the progressive dismantling of old trading monopolies, 
and a transition around mid-century towards free trade and away from the mercantilist 
restrictions of the previous century. Empire could still have boosted trade flows via 
consumer preferences as in Magee and Thompson (2010) or via “trade-promoting capital 
such as common institutions and business networks” (Head, Mayer and Ries, 2010, p. 9). 
But it would not be surprising if such forces had a smaller impact on trade costs than the 
mercantilist legislation of the 18th century. 
With our new data in hand, we can for the very first time estimate the effects over the 
very long run of these two important proxies for bilateral trade costs, that in turn have 
been central to decades of applied work on the determinants of international trade. In sum, 
we find that the impact of distance fell by roughly two-thirds between the 1780s and 1860s 
but remained essentially flat in the late 19th century. Interestingly, the decline coincided 
with the onset of coppering. Likewise, the impact of empire on British exports was very 
large throughout, but 18th century mercantilism had a much bigger export-promoting 
effect than did "liberal empire" in the late 19th century. Finally, we also establish that 
there was significant heterogeneity across sectors in the impact of distance and empire on 
British exports. 
A brief account of some of the major technological and political changes affecting 
international trade over the course of the 18th and 19th centuries is given in Section 2. 
Section 3 introduces the new data underlying this paper. Section 4 discusses our empirical 
specifications while Section 5 presents our results and Section 6 concludes. 

#### 2 The technology and politics of trade

This period was one of enormous technological, political, and geopolitical transitions, all of which could be expected to have had an impact on the geography of British exports. In

this section we provide a brief introduction to the most notable of these, beginning with technological change in the shipping industry.

##### 2.1 Transportation technology

While there is no doubt that transportation technology improved dramatically in the wake of the steam revolution, whether and to what extent there were improvements in shipping in the 18th and early 19th centuries remains an open question. A slight complication is that different authors use different metrics such as the longevity of ships (Solar and Rönnbäck, 2015), shipping losses (Kelly, Ó Gráda, and Solar, 2021), shipping supply costs (Solar, 2013), ship speeds (Rönnbäck, 2012; Solar and Hens, 2016; Kelly and Ó Gráda, 2019), and freight rates which were the focus of much of the earlier literature (North, 1958, 1968; Harley, 1988). Nonetheless, despite some disagreements on details, the makings of a new consensus seem to be emerging from the recent literature. Harley (1988) used freight rate data on British shipping routes to conclude that there was substantial productivity growth in British shipping in the 19th century which accelerated sharply after mid-century with the transition from sail to steam. But the onset of quantitatively significant productivity improvement has now been pushed back to the late 18th century, particularly the decades after 1780. Copper sheathing protected ships against worms found in tropical waters which rotted the timber. Coppering thereby increased the longevity of ships by roughly one-half (Solar and Rönnbäck, 2015) and consequently lowered capital costs. It also protected ships against barnacle incrustations and seaweed, increasing ship speeds and the frequency of voyages. The Royal Navy coppered its entire fleet between 1779 and 1781, and the East India Company and slave merchants quickly adopted the new technology. Other innovations emphasized by Kelly and Ó Gráda (2019) and Kelly, Ó Gráda, and Solar (2021) include iron frames to reinforce

wooden hulls, flush (flat) decks and watertight hatches which were introduced in the 
1820s and 1830s, and improved navigation techniques. Kelly and Ó Gráda (2019) find 
an increase in ship speeds of about one-third from the 1780s to 1820s while Solar and 
Rönnbäck (2015) find that coppering alone increased ship speeds by about one-sixth. 
A noteworthy feature of this recent literature is that it focuses on ships used on long 
distance voyages, carried out among others by the East India Company, the Royal Navy, 
and slave merchants. Coppering was a warm water technology. By the end of the 18th 
century, all Asia-bound British ships, 90% of Africa-bound ships, and 50% of British ships 
headed for the West Indies and Latin America were coppered, compared to less than 6% of 
ships headed for Europe or North America (Solar and Rönnbäck, 2015, p. 812). Its impact 
on transport costs should thus have been asymmetric, having little or no effect on shorter 
voyages but lowering costs on the longest voyages. 
Technological progress accelerated in the 19th century with the advent of steamships. 
In contrast to coppering, the new steam technology was first used on shorter routes with 
British steamers plying the route to Paris by 1816. For several decades steamships were 
used mostly to transport mail, people, and similar high-value cargoes over short distances. 
A series of subsequent innovations, such as the compound engine, screw propellor, and 
steel hulls meant that in the late 19th century steamships profitably transported a wider 
range of goods while the opening of the Suez Canal in 1869 gave an important boost 
to steam on the Asian route (Fletcher, 1958; Jacks, Meissner, and Wolf, 2024). Despite 
this, sailing ships famously remained competitive on many long-distance routes until the 
century’s end. Hatton (2024) finds that passenger voyages by sail from the UK to Adelaide 
were three weeks shorter in the mid-1880s than in the late 1840s and attributes this to 
larger, iron-constructed, clipper-style boats and a greater ability to exploit the great circle 
route. Thus, the cost and speed of shipping fell dramatically over the course of the late 
19th century but on both shorter and longer routes. 

##### 2.2 Politics: from mercantilism to free trade

British trade in the 18th century was still shaped by the Navigation Acts of the late 17th century. These aimed to boost England’s role in international trade. Above all, this came at the expense of the Netherlands by excluding Dutch middlemen from English trade, including that between England and her overseas colonies. Such zero-sum thinking was typical of the mercantilist era, and the consequence was a commercial policy framework tightly linking Britain’s colonies to the metropole (Wilson, 1978; Ormrod, 2003). The period was also characterized by import tariffs and prohibitions while the East India Company held a monopoly on the trade between Britain and India as well as China. The 18th century saw Britain fighting wars in the Americas, Europe, and India, culminating in the American Revolutionary War and the quarter-century struggle against France that only ended in 1815. The period after 1815 was a relatively peaceful one as far as the UK was concerned, despite some notable exceptions such as the Crimean War of the 1850s. Economically, the immediate postwar decades saw a gradual transition away from the mercantilism and protectionism of the previous century. The Corn Laws protecting domestic agriculture were liberalized in 1828 and 1842 and abolished in 1846, while the UK also finally repealed the Navigation Acts in 1849. The East India Company lost its Indian and Chinese trade monopolies in 1813 and 1833, respectively. The loss of the United States in 1783 was a major blow. But the British Empire resumed its expansion in the 19th century in Africa and Asia while settler colonies were consolidated in British North America and established in Oceania. While the empire provided an important market for British manufactured goods, foreign competitors no longer faced mercantilist restrictions on their ability to do business there. Trade with the United States continued to flourish after American independence, further reducing the connection between British exports and the empire.

#### 3 Data

Subsection 3.1 discusses how we constructed our dataset, and subsection 3.2 offers a brief overview of British exports during the period from 1700 to 1899.

##### 3.1 A new British export dataset

Our main contribution is a new, publicly available dataset on the universe of bilateral, 
commodity-level British exports from 1700 to 1899. All related image files, files used for 
the raw data entry, and the cleaned and consolidated data used in this paper are available 
at: https://davidjacks.org/british-trade-data/. The primary sources of the data are the 
export ledgers compiled by the Customs and Excise Department under various titles from 
1697 to 1899 (see Appendix A). These were entirely hand-written until the mid-19th 
century and remained partly hand-written thereafter, thus precluding the use of optical 
character recognition software. 
424,551 lines of raw data from over 7,000 pages of ledgers were scanned, digitized, 
and (painstakingly) cleaned by hand. For our present purposes, we focus our attention on 
exports of British-produced goods. Our reasons for doing so relate to: (i) concerns over 
smuggling activity and under-reporting which primarily apply to imports and re-exports; 
and (ii) potential concerns over market versus official valuations of trade flows which ease 
considerably earlier in the case of exports than of imports (see below). 
The original data collection by the British government was used to determine bilateral 
trade flows for purposes of taxation. By 1697, there was already an extensive set of 
excises and tariffs in place which provided a significant fraction of central government 
revenue and which required close observation and detailed accounting of exports and 
imports of goods in British ports (O’Brien, 1988; Dal Bo et al., 2025). At the same time, 
an increasingly mercantilist understanding of the role of trade in shaping the domestic 

economy had developed. The ledgers provide annual summaries of bilateral exports, 
imports, and re-exports as well as annual outflows of gold and silver. Thus, a secondary 
objective of the original data collection was to use the balance of trade as a key indicator 
of the performance of the British economy and to measure net bullion flows which were a 
potential objective of economic policy. 
The ledgers contain a line-by-line account of Britain’s bilateral, commodity-level trade 
flows with all locations in the rest of the world. We have every reason to believe that 
they capture the full population of British trade flows as the correspondence between our 
data and values reported in older sources is nearly perfect. For example, the correlation 
between aggregate exports by year from Mitchell (1962) and the equivalent figures derived 
from the ledgers is >0.99 for the period from 1700 to 1899. Similarly, the cumulative 
reported values for aggregate exports taken from the two sources are 1.40 and 1.41 billion 
pounds, respectively. 
The ledgers are, however, presented in an inconsistent welter of detail. In some years, 
they distinguish between trade with London versus “outports”, trade carried out on British 
versus foreign ships, and/or the trade of sub-national units like England versus Scotland. 
There are also changes over time with respect to the reporting unit: thus, trade flows are 
captured for England and Wales up to 1780, for Great Britain up to 1830, and for the 
United Kingdom up to 1899.2 

The ledgers are the source for classic studies of British trade such as Schumpeter (1960). However, this pioneering work was mostly concerned with computing aggregate trade statistics, reflecting the scholarly interest of the period in macroeconomic aggregates as well as technological constraints on data storage. Consequently, despite the tremendous time and effort which was expended on compiling and aggregating these statistics, most

2In 1790 England accounted for 95% of all British exports. In 1840, England accounted for 90% of all UK exports.

of the related figures gave little sense of the important shifts in the commodity-by-country 
composition of British trade which occurred over this period. 
A notable advance came with the lifelong work of Ralph Davis, summarized in Davis 
(1979). In this slim but dense volume, Davis details British exports and imports using a 
classification scheme of 17 commodity groups across 15 geographical areas at ten-year 
intervals from 1785 to 1855.3 This is one of the only attempts to provide early British 
trade data at anywhere near the commodity-country level, with most studies reporting 
total trade figures for a particular commodity or a particular geographic area, but not their 
cross-tabulation. Our project is thus a continuation of – and hopefully an improvement on 
– the path-breaking work of Davis as no further systematic evidence has been disseminated 
at this level over the past five decades. 
Our first objective was to digitize the export ledgers at ten-year intervals from 1700 to 
1899.4 However, in any project like this there are a number of caveats regarding the data 
which should be addressed head-on: 

1. Going back as far as Clark (1938) and Schlote (1952), commentators have cautioned about the reliability of these statistics due to the lack of effort by and misaligned incentives of government agents, smuggling activity, and the under-reporting of imports in particular. Although such concerns are undoubtedly valid, the scale of this type of activity was almost certainly dominated by the volume of trade legitimately recorded and is more likely even smaller in the case of export activity. Furthermore, there is nothing in the historical record suggesting any systematic bias across commodities, countries, or commodity-by-country combinations.

3More precisely, he reports three-year averages based on the value of observations in the fourth, fifth, and sixth years of each decade. 4The full set of years in the final dataset are 1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1807, 1820, 1830, 1840, 1850, 1860, 1869, 1880, 1890, and 1899. The inclusion of “off years” like 1807, 1869, and 1899 was driven by the lack of data in particular benchmark years.

2. Before 1904 (that is, during our entire period of interest), British exports were reported for those destinations to which they were directly shipped. Thus, trans shipment trade went unreported (and, as a consequence, land-locked destinations are absent in the data). Additionally, while the goods categories reported in the ledgers were generally becoming more aggregated, the level at which destinations were reported was generally becoming more disaggregated. What this means is that in using the most geographically disaggregated data available in any given year to examine the extensive margin of British exports we run the risk of conflating the “real” extensive margin with changes in the process of data collection and coding. Accordingly, we aggregate the bilateral, commodity-level export data up to the smallest areas which can be consistently tracked through time. For example, we merge all observations on China and Hong Kong. In what follows, this amounts to having 86 destinations for every year in our final dataset. Appendix B describes the geographic distribution of the 86 destinations.

3. The evolving structure of the British economy over these two centuries entailed corresponding changes in the structure of the trade data reported in the ledgers. Some commodities suddenly emerge in the data (like railway carriages) while others disappear (like human hair). The chief problem this raises is how to assign consistent goods categories across years. From the original 424,551 observations of disaggregated exports from 1700 to 1899, we arrive at 254,998 observations of exports at the commodity level for the whole of England, Britain, or the UK (depending on the year being considered), rather than from individual ports or sub-national units. To these observations, we assign consistent destination identifiers as described above. We then assign SITC-2 codes to each of these observations at the commodity-destination level. Given that the commodity descriptions in the raw

data were sometimes quite imprecise, it is easier to assign exports to broader than to narrower categories. Thus, we obtain:

• 254,998 observations classified at one-digit sections (e.g, beverages & tobacco);

• 250,511 observations classified at two-digit divisions (e.g, beverages); and • 231,503 observations classified at three-digit groups (e.g, alcoholic beverages).

Given the rather large reduction in the number of observations when we move from the two-digit to the three-digit level, we settle on the two-digit level as our preferred level of analysis as it provides the best compromise between disaggregation and observation count, capturing more than 99% of the monetary value of aggregate British exports. We then sum the monetary value of individual observations within each two-digit division to form our measure of exports at the destination-division level. Finally, we interpret the ledgers as representing the full population of British trade and rectangularize the data by assigning zero values to observations for particular destination-division combinations for which there are no recorded values.

4. Another obstacle to the use of the ledgers is the fact that the underlying prices used to value bilateral trade flows were initially fixed – from 1702 to 1813 in the case of exports and from 1702 to 1853 in the case of imports (Davis, 1979, pp. 77-82).5

These “official prices” were based on average market prices prevailing in or around 1700 and were presumably used in an attempt to minimize bargaining over customs

5As Imlah (1948, 1958) points out, estimates of the current value of aggregate British exports are available from 1798 when an export convoy tax was imposed. These estimates of aggregate exports were compiled from the ledgers we use here and reported in the annual returns of the Inspector-General of the Customs. They were subsequently used by Imlah and others like Mitchell (1962). For better or worse, though, the detailed commodity level data in the ledgers remain valued at official prices until 1813 when CUST 8 becomes available. As Davis (1979, p. 79) points out, “though annual totals on this new (declared values) basis are available from 1798, the detailed analyses survive only from 1813.” We thank one of the referees for drawing our attention to this issue.

valuations and, thereby, maximize compliance.6 For many researchers, this implicit fixed price index was seen as a chief attraction of the data, in that it provided a consistent measure of real quantities exported and imported. For example, Deane and Cole (1962) famously used these data to construct their indices of industrial production. On the other hand, aggregating across such real quantities to obtain aggregate export values is clearly problematic. In order to address this issue, we estimate gravity models below using disaggregated data and division-year fixed effects, thereby controlling for changes in relative prices over time.

Finally, in all of our regressions, we drop observations related to parcel post and bullion, coins, gold, or silver. Our final dataset then consists of British exports to 86 consistently-defined destinations in 57 SITC divisions across 21 years between 1700 and 1899. This yields a final observation count of 102,942 (that is, 4,902 observations for each

of the 21 years).7

##### 3.2 Overview of British exports

As stressed above, the use of constant official prices to value exports prior to 1813 means 
that aggregating trade figures is problematic. Nevertheless, creating such an aggregate 
should give a rough indication of overall trends in British exports. However, there is no 
single export price index spanning the years from 1700 to 1899. Figure 1 instead plots 
two separate real export series, one with a value of 100 in 1807 and the other with a value 
of 100 in 1820. The first series in black depicts the sum of the official values in the ledgers 
from 1700 to 1807. This represents British real exports expressed in 1700 prices. The 
second series in grey depicts the sum of declared values in the ledgers from 1820 to 1899 
6A lack of administrative resources, deference to tradition, or even sheer laziness may also have been 
factors (Imlah, 1948, p. 133; Davis, 1979, p. 78). 
7As reported earlier, we have 250,511 observations classified at the two-digit level: thus, there are on 
average 2.4 commodities per destination-division combination. 

Figure 1: Aggregate British Real Exports, 1700–1899

25

50

100

200

400

800

1600

=

1 
0 
0 

=

1 
8 
2 
0 

1700 1750 1800 1850 1899 
1700 prices 
1880 prices 

Notes: The black line depicts the sum of the official values in the ledgers from 1700 to 1807 and represents British real exports expressed in 1700 prices. The grey line depicts the sum of declared values in the ledgers from 1820 to 1899 deflated by the export price index reported in Imlah (1958), and represents British real exports expressed in 1880 prices. The vertical line in 1813 demarcates a break in continuity between the two series as they use different base years for export prices.

deflated by the export price index reported in Imlah (1958). This represents British real exports expressed in 1880 prices. The two series are not strictly comparable as they use different base years for export prices, and the vertical line in 1813 is intended to convey this break in continuity. In what follows, we therefore focus on growth rates within each

period rather than on levels across them.

The black line suggests that British real exports increased by a factor of 5.8 between

1700 and 1807 when expressed in terms of 1700 export prices. Much of this increase occurred between 1740 and 1750 and again after the independence of the United States in 1783. Davis (1979, pp. 9-11) relates the jump between 1780 and 1790 to the supply shock emanating from technical change in the cotton industry whereas the sources of the jump between 1740 and 1750 are less clear. The grey line suggests that British real exports increased by a factor of 21.7 between 1820 and 1899 when expressed in terms of 1880 export prices. Notably, the growth in real exports from 1820 to 1860 (by a factor of 8.1)

Figure 2: The Extensive Margins of British Exports, 1700–1899

0

2

0

4

0

6

0

8

0

1

0

0

1700 1750 1800 1850 1899

Non-zero cells at the destination-division level

Non-zero destinations

Notes: The black line depicts the share of non-empty cells in our matrix of 86 destinations by 57 divisions in a given year. The grey line depicts the share of 86 destinations for which British exports in any division are positive.

was higher than that from 1860 to 1899 (a factor of 2.7). Whether this reflects the fallout from the Panic of 1866 (Xu, 2022) and/or the slowdown in British productivity growth from 1870 (Crafts and Mills, 2020) remains an open question.

Figure 2 considers the extensive margins of trade where the use of official prices prior to 1813 is not an issue. The black line depicts the share of non-zero cells in our full matrix of 86 destinations and 57 divisions. The grey line depicts the share of 86 destinations for which British exports in any division were positive in a given year. Both series are relatively flat between 1700 and 1780 (averaging 12% for the series in black and 30% for the series in grey). This suggests that most of the export growth for those years depicted in Figure 1 occurred on the intensive margin, that is, within a relatively fixed set of destination-division combinations. In contrast, the period from 1780 to 1899 was marked by a steady increase in both the share of non-zero cells (from 11% in 1780 to 59% in 1899)

and the share of non-zero destinations (from 29% in 1780 to 99% in 1899), suggesting that

Figure 3: British Export Share with the Empire, 1700–1899

0

2

0

4

0

6

0

8

0

1

0

0

1700 1750 1800 1850 1899

British Empire

British Empire plus United States after Independence

Notes: The black line represents the share of British exports going to destinations in the contemporaneously-defined British Empire.

The grey line represents this share plus the share of the United States after Independence.

British exports grew on the extensive as well as the intensive margin after 1800. Finally, the undepicted ratio of non-zero cells to non-zero destinations captures the average share of divisions with positive trade flows, conditional on a country importing goods from

Britain. Interestingly, this ratio is essentially flat from 1700 to 1807 with an average value of 0.41. It is also essentially flat from 1820 to 1899 with an average value of 0.59 but with a discrete jump in 1820 just as British industrialization really took hold.

Figure 3 depicts the importance of trade with the British Empire over these two hundred years. The black line represents the share of observed exports going to destinations in the contemporaneously-defined British Empire.8 The grey line adds the post-independence

United States to the total. The difference between the two lines after 1783 thus represents the US share of British exports. The share of the British Empire rose from 14% in 1700 to

54% in 1780. US independence initiated a precipitous decline in the empire share to 32%

8The figures prior to 1813 come with the same caveat as before: they are based on trade flows valued at fixed official prices. The same comment applies to Figure 4 and Figure 5.

Figure 4: British Export Shares by Continent, 1700–1899

1700 1750 1800 1850 1899 Africa Asia Europe N America Oceania S America

Notes: Shaded areas represent the share of British exports going to destinations by continent.

in 1790. There followed a relatively stable share over the 19th century with a final value of 34% in 1899. Exports to what would become the United States had been very important prior to independence. They represented on average 11% of total exports between 1700 and 1780, peaking at 22% in 1760. The dramatic rise in the US share of total exports between 1790 and 1807 reflects the resumption of normal trading relationships between ex-colony and coloniser as well as the diversion of British exports in light of the war with France (at least until the US Embargo Act came into effect in December 1807). The figure also highlights the importance of the United States as a destination for British exports after 1815, representing on average 13% of total exports between 1820 and 1899.9

Figure 4 depicts export destinations by continent over the same 200 year period. A few notable trends dominate: (a) the secular decline of the European share from 79% in

9Other notable destinations in the British Empire include: (a) British India whose share of total exports climbed from 3% in 1700 to 13% in 1899; (b) the British West Indies whose share of total exports declined from 5% in 1700 to <1% in 1899; and (c) the eventually self-governing Dominions of Australia, Canada, New Zealand, and South Africa whose share of total exports climbed from <1% in 1700 to 16% in 1899.

Figure 5: British Export Shares by One-Digit Sections, 1700–1899

1700 1750 1800 1850 1899 SITC 0, 1, 4 SITC 2, 3 SITC 5 SITC 6 SITC 7 SITC 8, 9

Notes: Shaded areas represent the share of British exports by 1-digit section.

1700 to 40% in 1899; (b) the rise and decline of the North American share (inclusive of the Caribbean and Central America) from 11% in 1700 to 59% in 1807 and 12% in 1899; (c)

the dramatic 19th century rise of the combined share for Africa and Asia (particularly the latter) from 16% in 1800 to 32% in 1899; and (d) the emergence of trade with Oceania and

South America (particularly the former) seen in their combined share rising from 2% in

1800 to 16% in 1899.

Finally, Figure 5 depicts the share of exports across the ten SITC one-digit sections.10

Here, we collapse similar sections for ease of presentation, e.g., sections (2) and (3) which capture all crude materials inclusive of coal. A few interesting patterns emerge. First, at the highest level of aggregation, manufactured goods in sections (5) through (9) dominate the total value of exports over these two centuries with an average share of 89%. Second, 10One-digit sections correspond to the following categories: (0) Food and live animals chiefly for food; (1) Beverages and tobacco; (2) Crude materials, inedible, except fuels; (3) Mineral fuels and lubricants; (4) Animal and vegetable oils, fats, waxes; (5) Chemicals and related products; (6) Goods classified chiefly by materials; (7) Machinery and transport equipment; (8) Miscellaneous manufactured articles; and (9) Commodities not classified elsewhere.

manufactured goods themselves are dominated by section (6) which includes critical goods like iron and steel, metal manufactured goods, and textile fabrics and yarns, commanding an overwhelming majority of British exports with an average share of 76%. Third, there is a clear decline in the export share of section (6) starting from 1869. However, part of this decline in section (6) is somewhat mechanical as this period also saw the rise of important and related new export industries: coal in section (3) along with machinery and railway-related equipment in section (7).

#### 4 Gravity in the very long run

A large literature has successfully applied the gravity model to the long-run history of international trade (e.g., Barjamovic et al., 2019; Flueckiger et al., 2022; Jacks, Meissner, and Novy, 2011). Structural gravity equations can be derived from a wide range of leading trade models. Following Anderson and van Wincoop (2003), Head and Mayer (2014), and Redding and Weinstein (2019), the basic structural gravity equation for industries (or in our case, SITC divisions) can be written as:

y k w

t k ij Π k i P k

j

1− σ k

. (1)

x k 
ij represents nominal exports of division k from i to j. The first term on the right hand 
side of Equation (1) is what bilateral trade would be in the absence of any frictions: it 
would simply be j’s expenditure on k (e k j) multiplied by i’s share of world output of k, 
y k i/y k w. The second term represents the impact of those frictions: bilateral trade costs for 
the division in question t k 
ij relative to the product of i’s outward multilateral resistance 
for k (Π k i) and j’s inward multilateral resistance for k (P k 
j ). The latter two elements are 
best thought of as indices of all outward and inward trade costs. Finally, σ k represents the 

elasticity of substitution for k governing the responsiveness of trade flows to relative trade costs. In a full panel setting, all variables in Equation (1) are potentially time-varying and the dimensionality of the dataset is ijkt. Equation (1) can then be estimated by:

lnx k ijt = ψ k it + γ k jt + δ k ij + z k ijt α k + ϵ k ijt . (2)

Time-varying origin-division fixed effects (ψ k it) control for i’s share of world output of good 
k and i’s outward multilateral resistance for k (Π k it). Time-varying destination-division 
fixed effects (γ k jt) control for j’s expenditure on k and j’s inward multilateral resistance for 
k (P k jt). For our purposes, the variables of greatest interest are z k 
ijt which are time-varying 
determinants of bilateral trade costs k (t k ijt), namely distance and empire. Finally, any 
time-invariant determinants are accounted for by the division-specific bilateral fixed 
effects (δ k ij) while ϵ k 
ijt represents the error term. 
In our setting, we only have data for one exporter, Britain. This means that we can 
drop the exporter index i from the estimating equation. Thus, we should estimate: 

lnx k jt = ψ k t + γ k jt + δ k j + z k jt α k + ϵ k jt. (3)

However, this is not possible as including time-varying destination-division fixed effects 
(γ k jt) would absorb all variation in the data. We can still include ψ k 
t which controls for the 
British outward multilateral resistance term for k and for Britain’s share of world output 
of k, but we cannot use fixed effects to control for either j’s expenditure on k or j’s inward 
multilateral resistance (IMR) for k. We therefore resort to proxies in this case. 
Division-specific expenditure for each destination is not available well into the 1960s, 
so we rely on estimates of destination economic mass. These are constructed as the product 
of GDP per capita from the Maddison Project Database 2020 and population from the 

Our World in Data website. Where possible, missing values are estimated using linear interpolation: this yields population data for all destination-year combinations, but GDP per capita data for only 30% of them.11 In order to circumvent the lack of data on GDP per capita, we assign missing observations a "representative" value equal to that for Turkey from 1700 to 1899. We note that this particular estimate of GDP per capita only rose by 36% over these two centuries at a time when British GDP per capita rose by 215%. Given this slow rise in estimated GDP per capita for 70% of our sample, the vast majority of variation in economic mass across destinations comes from variation in population. In Appendix E, we therefore report results where ln(GDPjt) is replaced with population. Our results are robust to this change.12

Similarly, data limitations prevent us from constructing proxies for the omitted 
division-specific IMR terms.13 We therefore use two proxies for aggregate IMR terms. First, 
we construct a measure of each destination’s time-varying distance from the economic 
center of gravity (ECG) from Quah (2011). The ECG is defined as the average location of 
world economic activity (again derived from Maddison’s estimates of GDP) in a given year. 
We use the log of j’s great-circle distance from the ECG, ln(DECGjt), as an atheoretical 
proxy to control for the IMR terms in our main analysis. Second, in Appendix E, we 
control for time-varying proxies for the IMR terms by destination, ln(IMRjt), that are 
constructed as GDP-weighted, great-circle distances between each destination and all 
other destinations. The results from these two proxies for the IMR terms are very similar 
to one other. 
In some specifications, we include destination-division fixed effects (γjk) which control 

11Appendix D reports the coverage for estimates of GDP per capita, population, and our proxy for GDP. 12In Appendix E, we also allow the coefficients on the proxy for real GDP to be division-specific and find no material differences in our results. 13In order to construct theory-consistent IMR terms, we would need the value of gross output for every destination-division-year combination as well as time-varying, division-specific bilateral trade costs for all country pairs in the world over these 200 years. Simply put, such data are not available.

for all time-invariant, destination-specific determinants of British exports for k. In the 
panel setting, they are the equivalent of the division-specific pair fixed effects (δ k ij) in 
Equation 2. Obviously, papers estimating distance coefficients typically do not include pair 
fixed effects. We are only able to include γjk because our distance variable is time varying 
due to the opening of the Suez Canal in November 1869. This implies that the distance 
variable will not be absorbed by such destination-specific fixed effects. Our distance 
coefficients estimated without controlling for γjk are thus more comparable with the 
existing literature. Finally, while Equation 3 suggests estimating division-specific distance 
and empire coefficients, we initially prefer estimating coefficients that are common to all 
divisions. This makes the exposition easier and facilitates comparisons with coefficients 
estimated using aggregate trade data. We do, however, provide an assessment of potential 
sectoral heterogeneity below. 
Our inclusion of proxies for destination economic mass and the IMRs terms as well 
as (in some specifications) destination-division fixed effects (γjk) potentially gets us 
closer to what theory requires. It is, however, important to acknowledge that since we 
cannot include time-varying destination-division fixed effects (γ k jt) we are only imperfectly 
proxying for expenditure and the IMR terms in each destination. This could bias our 
results. For example, we might expect that not adequately accounting for the IMR terms 
might bias the estimate on distance upward in absolute value (Anderson and van Wincoop, 
2003). The intuition is that, if the IMR terms are not accounted for, then the estimated 
impact of distance might also capture the impact of multilateral remoteness. Similarly, 
not accounting for the IMR terms could lead to upward bias in the estimate of the effect of 
empire since, without the IMR terms, the model will not account for any trade-diversion 
effects from third countries. Thus, our focus is more on changes over time in these 
coefficients than on their absolute values.14 

14Similarly, our real GDP proxy for destination expenditures is less than perfect. It is aggregate rather

Summing up, the baseline estimating equation for our data is:

x k jt = exp[ψ k t + γjk + α1ln(DISTjt) + α2EMP IREjt] × exp[α3ln(GDPjt) + α4ln(DECGjt) + α5W ARjt] × ϵ k jt. (4)

x k 
jt denotes British exports in two-digit SITC division k to country j in year t.15 As before, 
ψ k 
t are time-varying division fixed effects which control for all determinants of British 
exports that vary across divisions, years, and divisions-by-year. These are very important 
in the context of our data as UK exports were expressed in real terms until 1813 and in 
nominal terms from 1813. These fixed effects then control for changes in division-specific 
price levels and are therefore included in all of our main specifications. Below, we also 
discuss the impact of including destination-division fixed effects (γjk.) 
x k 
jt is now expressed in levels as we estimate the model in multiplicative form via 
Poisson Pseudo Maximum Likelihood (PPML). This estimator is the standard in the gravity 
literature due to its ability to account for both heteroskedasticity and the presence of zeros 
in trade data (Santos Silva and Tenreyro, 2006). Furthermore, PPML automatically eases 
the “adding-up constraints” presented by reduced form approaches like ours (Fally, 2015). 
Finally, we cluster standard errors at the destination-division level, ensuring that residuals 
than division-specific, and the majority of observations are assigned a representative income per capita. It is, 
however, less clear to us in which direction this biases the results. Another possible source of bias is reverse 
causality. Two key sources of potential endogeneity in our estimates are: (i) the fact that high trade volumes 
may lead to lower trade costs through scale effects which may impart a downward bias to the estimated 
impact of distance; and (ii) the omitted trade costs between the UK and destinations in the British Empire 
are potentially higher (or lower) than those between the UK and other destinations in the sample which 
would impart downward (or upward) bias in the estimates of empire in our model. If incorporation into the 
empire became more likely as trade flows increased, this would likewise bias the empire coefficient upwards. 
But there are also some partially mitigating factors here: we use time-varying division fixed effects which 
absorb some of the co-variation in the potentially endogenous variables and the error term; to proxy for 
bilateral trade costs we use geographic distances which are exogenous; and we use pooled disaggregated 
data which partially mitigates the possibility that trade flows within a particular division might impact 
average (overall) trade costs or empire effects. 
15In Appendix E, we demonstrate the robustness of our results to using total British exports to destination 
j in year t. 

are appropriately adjusted for arbitrary, within destination-division serial correlation.16

Turning to the main variables of interest in Equation (4), ln(DISTjt) is the logarithm of bilateral distance between Britain and each of the export destinations in our sample. This is computed as the minimum maritime distance between either London or Liverpool and the nearest relevant port in each destination.17 We will begin by obtaining a single estimate of the impact of distance across divisions and over time. However, our main analysis will explore the evolution of distance effects over time. The other main variable of interest is EMP IREjt - an indicator variable that takes a value of one if destination j is a contemporaneous member of the British Empire and equal to zero otherwise.18 Similar to the analysis of the impact of distance, we will first obtain a single estimate of the empire effect that is common across divisions and years, but our main analysis will emphasize empire’s effect over time. Finally, we also control for wars with an indicator variable (W ARjt) that takes a value of one in the presence of war between Britain and the destinations in our sample and is equal to zero otherwise. In Appendix E we find that including the first lag of W ARjt, that is, war ten years previously, or alternatively accounting for the presence of war in any of the previous ten years, has no impact on our results.19

16In Appendix E, we also report equivalent OLS estimates which are consistent with those reported here. 17Distances in nautical miles were obtained from searoutes.com, in all cases specifying that the Kiel and Panama canals were not open. For pre-1870 distances, we further assumed that the Suez Canal was not open. A list of the ports concerned, together with the related distances, is provided in Appendix C. 18Appendix C summarizes for each imperial destination in our sample the year in which it was incorporated into the British Empire. Our use of consistent geographical destinations over time creates some problems in classifying countries as being in the empire or not. This is particularly true for British India and Canada. We classify British India as being in the empire throughout our period while Canada is classified as being in the empire from 1763. In any case, our main results are not affected by these choices. 19The wars considered are the Great Northern War (1700-1721), the War of the Spanish Succession (1701-1714), the War of the Quadruple Alliance (1718-1720), the Anglo-Spanish War (1727-1729), the War of Jenkins Ear (1739-1748), the War of the Austrian Succession (1740-1748), the Seven Years War (1756-1763), the U.S. Revolutionary and associated wars (1775-1784), the Fourth Anglo-Dutch War (1780-83), the French Revolutionary/Napoleonic and associated wars (1793-1815), the War of 1812 (1812-1815), the Battle of Navarino (1827), the Aden expedition (1839), the Egyptian-Ottoman War (1839-1840), the First Opium War (1839-1842), the Crimean War (1853-1856), the Second Opium War (1856-1860), the Anglo-Persian War (1856-1857), and the Anglo-Zanzibar War (1896). Appendix E also provides some late 19th century

#### 5 Empirical findings

Our analysis proceeds in three steps. First, we obtain panel estimates of the effects of distance and empire that are constrained to be common across all divisions and years in our data. Then, our main results explore the evolution of the distance and empire effects over the course of the 18th and 19th centuries. Finally, we obtain estimates of the heterogeneous effects of distance and empire across the ten SITC one-digit sections.

##### 5.1 Common panel gravity estimates

Table 1 includes panel estimates obtained from variants of Equation (4) which differ in 
their use of fixed effects. This analysis serves three purposes: (1) it provides benchmark 
estimates for the key covariates in our model; (2) it clarifies some features of the data; and 
(3) it illustrates the benefits and costs of using different sets of fixed effects. 
The results in column (1) of Table 1 are obtained without any fixed effects. 
Encouragingly, the coefficients on all five covariates are statistically significant and have 
the expected signs. Specifically, we obtain negative, sizable, and statistically significant 
estimates of the effects on trade of distance and wars, and positive, sizable, and statistically 
significant estimates of the effects of empire and GDP. Finally, consistent with expectations, 
the estimate on our proxy for inward multilateral resistance, ln(DGECjt), is positive and 
marginally statistically significant. Intuitively, the more remote a given country is from 
the center of world economic activity, the more it will import from Britain (as P k 
j increases 
in Equation (1) x k 
ij rises), holding all else constant. 
The results in column (2) of Table 1 are obtained with division-year (kt) fixed effects. As 
discussed earlier, these control for relative price changes before 1813 and must therefore 

evidence that including other control variables like gold standard adherence or tariffs does not materially affect our results.

Table 1: Panel Gravity Estimates, 1700-1899 
(1) (2) (3) (4) 
No FEs kt FEs kt & j FEs kt & jk FEs 
ln(DISTjt) -0.429 -0.397 -0.886 -1.103 
(0.063)∗∗∗ (0.086)∗∗∗ (0.339)∗∗∗ (0.316)∗∗∗ 
EMP IREjt 1.245 1.105 0.361 0.369 
(0.346)∗∗∗ (0.156)∗∗∗ (0.175)∗∗ (0.180)∗∗ 
ln(GDPjt) 0.712 0.589 0.239 0.199 
(0.099)∗∗∗ (0.041)∗∗∗ (0.128)∗ (0.132) 
ln(DGECjt) 0.620 0.478 0.486 0.610 
(0.376)∗ (0.193)∗∗ (0.193)∗∗ (0.186)∗∗∗ 
W ARjt -1.942 -0.752 -0.637 -0.654 
(0.427)∗∗∗ (0.364)∗∗ (0.290)∗∗ (0.285)∗∗ 
Constant -8.822 
(5.110)∗ 
N 102,942 79,034 79,034 64,447 

Notes: This table reports estimates that are obtained from Equation (2). The estimator is PPML, and the dependent variable is bilateral exports at the 2-digit SITC-2 level over 21 years during the period from 1700 to 1899. The differences between the three columns are in the fixed effects used. Specifically, no fixed effects are used in column (1). Column (2) uses division-year fixed effects. Column (3) uses division-year and destination fixed effects. Column (4) uses division-year and destination-division fixed effects. The standard errors in each specification are clustered by destination-division and are reported in parentheses. ∗ p < .1,∗∗ p < .05, ∗∗∗ p < .01.

be included in our baseline specification. The main changes resulting from their inclusion are that the estimate on W ARjt becomes smaller and less statistically insignificant and the positive estimate on our proxy for multilateral resistance, ln(DGECjt), becomes smaller and more statistically significant.20

The results in column (3) of Table 1 are obtained with division-year (kt) and destination (j) fixed effects. Three main changes in the results stand out. First, the estimate of the impact of distance is still negative and statistically significant but is much larger than in

20The reason for the decrease in the number of observations in column (2) is the inclusion of the fixed effects. Specifically, all observations that are fully explained by the fixed effects are statistically irrelevant and are therefore automatically dropped from the estimating sample. In the robustness analysis in Appendix E, we re-estimate the specification from column (1) based on the sample from column (2) and confirm that the differences between the two columns are indeed driven by the division-year fixed effects and not by the different number of observations.

column (2). This estimate should be interpreted with caution because, by construction, it 
is identified exclusively from the variation in distance over time for the 25 destinations 
in our sample whose trade with Britain was affected by the opening of the Suez Canal. 
Consequently, the related standard errors are also larger in magnitude. The distance 
coefficient in column (2) of -0.397 is comparable to the average distance coefficient for 
1870 of -0.540 in the meta-analysis of Disdier and Head (2008) while the coefficient in 
column (3) of -0.886 is much larger. This is perhaps not surprising since, as noted earlier, 
the coefficient in column (3) is not strictly comparable to most distance coefficients in the 
literature which do not include country-pair fixed effects.21 
The other notable difference between the estimates in columns (2) and (3) is that, 
once destination fixed effects are added, the coefficient on EMP IREjt – now identified 
exclusively from entries into and out of empire – falls from 1.105 to 0.361. What is more, 
the precision of these results also declines. However, our results are quite similar to those 
in Mitchener and Weidenmier (2008): they obtain empire elasticities of 1.29 to 1.46 with 
country fixed effects and 1.77 to 1.78 with country-year fixed effects which decline to 
only 0.36 to 0.39 when country pair or country pair-year fixed effects are included. The 
implication is that the destination fixed effects – which are equivalent to country pair 
fixed effects in our single-country context – absorb most of the variation here. We will, 
therefore, obtain our main results without destination fixed effects but include these in 
robustness exercises in Appendix E.22 
Finally, column (4) includes both division-year (kt) and destination-division (jk) fixed 
effects. As can be seen, the results are similar to those in column (3): it is the inclusion of 
destination fixed effects that really makes the difference. In any case, Appendix E presents 

21For instance, Mitchener and Weidenmier (2008) obtain distance elasticities for 1870-1913 of -0.52 to -0.56, rising to -0.72 to -0.75 when country or country-year (but not country pair) fixed effects are included. 22An important difference between our results and those of Mitchener and Weidenmier (2008) is that while they are estimating a general empire effect, our data only allow us to estimate the impact of empire on British exports.

results including destination-division fixed effects.

##### 5.2 Evolution of the impact of distance and empire over time

The results in Figure 6 below are obtained from the following version of Equation (4) which includes division-year fixed effects and allows for the estimated effects of distance and empire to vary over time:

x k jt = exp[ψ k t +

1899 X T =1700 α1T ln(DISTjT ) + 1899

X T =1700 α2T EMP IREjT ] × exp[α3ln(GDPjt) + α4ln(DECGjt) + α5W ARjt] × ϵ k jt. (5)

Given the fixed effects in our model and the fact that both distance and empire are time-varying, we are able to calculate the level of both coefficients in each year as opposed to deviations from a baseline value. These levels are plotted in Figure 6 below. They are thus comparable (and similar) to coefficients generated from a series of cross-sectional regressions as shown in Appendix E. The left-hand panel of Figure 6 reports the evolution of the distance effects while the right-hand panel reports the corresponding empire effects. Each of the two panels plots the coefficient point estimates and associated 95% confidence intervals.

Figure 6: Evolution of Distance and Empire Effects on British Exports

-1.5 -1 -.5

0

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Distance Estimate 95% Confidence Interval

Evolution of the effects of Distance

0

1

2

3

4

5

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Empire Estimate 95% Confidence Interval

Evolution of the effects of Empire

Notes: This figure reports estimates of the evolution over time of the effects of distance and empire. The estimator is PPML, and the dependent variable is bilateral exports at the SITC division level over 21 years during the period from 1700 to 1899. The left panel of the figure reports the evolution of the effects of distance, and the right panel of the figure reports the corresponding effects for empire. Each of the two panels includes the point estimates and associated 95% confidence intervals. The standard errors are clustered by

destination-division.

Two findings stand out from the distance estimates in the left panel of Figure 6. First, the distance estimates are all negative and statistically significant as expected. Second, our distance coefficients can be grouped into three eras. During the first period from 1700 to

1780, the effects of distance are the largest, varying between roughly -0.7 and -1.0. During the second period from 1780 to 1820, the effect of distance is roughly -0.5. The negative distance effects are even lower (in absolute value) during the third period from 1820 to

1899 at a value of roughly -0.3, a result which is consistent with the findings for British

exports in Jacks and Pendakur (2010).

The estimated empire coefficients in the right panel of Figure 6 are all large, positive, and statistically significant. We again identify three eras in their evolution. The first period from 1700 to 1780 sees a gradual increase in the empire effect. It then declined dramatically in 1790 and remained stable until 1820 before declining again. The empire effects remained stable between 1850 and 1899. The empire effect was huge throughout these two centuries. The early 18th century coefficients, with a value of around two, imply a six-fold increase in exports to destinations in the British Empire, and the late

18th century coefficients with a value of around three imply a 19-fold increase. Even the late 19th century coefficients with a value of around one imply an increase in trade of

170%: nowhere near as high as during the heyday of mercantilist regulation but hardly

insignificant.

The sharp drop during the 1780s in both the distance and empire effects coincided with the independence of the United States, and the reader might suspect that there is some connection between these observations. Figure 7 therefore repeats the analysis of Figure 6 but excludes the United States (and the colonies that preceded it) from the analysis. As can be seen, the distance coefficient again begins to fall in absolute value during the 1780s.

This is the beginning of a declining trend in distance coefficients that continues until the

1860s. This contrasts with the steep decline seen in Figure 6. However, the total decline is of the same order of magnitude in the two figures.

Figure 7: Evolution of Distance and Empire Effects on British Exports without the US

-1.5 -1 -.5

0

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Distance Estimate 95% Confidence Interval

Evolution of the effects of Distance

0

1

2

3

4

5

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Empire Estimate 95% Confidence Interval

Evolution of the effects of Empire

Notes: This figure reports estimates of the evolution over time of the effects of distance and empire, excluding the United States. The estimator is PPML, and the dependent variable is bilateral exports at the SITC division level over 21 years during the period from 1700 to 1899. The left panel of the figure reports the evolution of the effects of distance, and the right panel of the figure reports the corresponding effects for empire. Each of the two panels includes the point estimates and associated 95% confidence intervals. The

standard errors are clustered by destination-division.

The empire effects in Figure 7 are, if anything, somewhat higher than in Figure 6, but instead of a steep decline in the 1780s, there is now a steep decline in the 1810s

coinciding with the end of the Napoleonic Wars.23 Since trade with the United States 
quickly recovered after the 1783, it makes sense that American independence should have 
weakened the association between empire and exports and lowered the empire coefficient. 
Once the United States is removed from the analysis, however, empire continued to exert 
an extremely high impact on exports until the 1810s. 
Finally, Appendix E shows that the time pattern of the distance and empire effects 
remains the same if we add destination-division fixed effects to our model. However, in 
line with Table 1, the whole distribution of distance effects shifts up in absolute terms, 
while the whole distribution of empire estimates shifts down. 

##### 5.3 Sectoral heterogeneity

Trade theory suggests that the effects of commercial policy and other determinants of trade costs may be very different across industries. Thus, the structural gravity model of trade is separable and allows for heterogeneous trade elasticities across products. From an empirical perspective, it is natural to expect that the effects of trade costs may vary across commodity categories. Against this backdrop, we explore variation in the effects of distance and the empire along these lines. The results in Figure 8 are obtained from the following version of Equation (4) that includes section-year fixed effects and allows for the estimates of the effects of distance and empire to vary across the ten SITC one-digit sections in our data:

x k jt = exp[ψ k

## t +X

10

S=1

α1S ln(DIST S jt) +X

10

S=1 α2SEMP IRE S jt] × exp[α3ln(GDPjt) + α4ln(DECGjt) + α5W ARjt] × ϵ k jt . (6)

23As a reminder, we control for these wars in our regressions.

Figure 8: Heterogeneity in Distance and Empire Effects on British Exports across Sectors

-1 -.5

0 .5

0 1 2 3 4 5 6 7 8 9 Broad Sectors Distance Estimate 95% Confidence Interval

Heterogeneity of the effects of Distance

-1

0

1

2

3

0 1 2 3 4 5 6 7 8 9 Broad Sectors Empire Estimate 95% Confidence Interval

Heterogeneity of the effects of Empire

Notes: This figure reports estimates of the heterogeneous effects of distance and empire across the ten SITC sections in our sample. The estimator is PPML, and the dependent variable is bilateral exports at the one-digit (section) level over the period from 1700 to 1899. The left panel of the figure reports the heterogeneous effects of distance, and the right panel of the figure reports the corresponding estimates for empire. Each of the two panels includes the coefficient point estimates and associated 95% confidence intervals. The

standard errors are clustered by destination-section.

The left panel of Figure 8 depicts the disaggregated distance effects and the right panel reports the corresponding empire effects. Each of the two panels include the coefficient point estimates and associated 95% confidence intervals. The main results from the left panel of Figure 8 can be summarized as follows. First, all but one of the estimated distance effects are negative and statistically significant (the exception being that for (1)

Beverages and tobacco). The rest of the distance estimates can be split in two groups.

First, there are large distance effects for (0) Food and live animals chiefly for food; (2)

Crude materials, inedible, except fuels; (3) Mineral fuels, lubricants and related; and (4)

Animal and vegetable oils, fats, waxes. Second, there are small distance effects for (5)

Chemicals and related products; (6) Goods classified chiefly by materials; (7) Machinery and transport equipment; (8) Miscellaneous manufactured articles; and (9) Commodities not classified elsewhere. Based on the fact that transportation costs are usually higher for sectors that are more resource oriented, we find the differences in the distance effects

between the two groups intuitive.

The results in the right panel of Figure 8 suggest that while the empire effects were

positive in all sectors, they were largest for (0) Food and live animals chiefly for food, (1) Beverages and tobacco, (8) Miscellaneous manufactured articles, and (9) Commodities not classified elsewhere. They were smaller for (5) Chemicals and related products, (6) Goods classified chiefly by materials, and (7) Machinery and transport equipment. And they were even smaller and statistically insignificant for (2) Crude materials, inedible, except fuels, (3) Mineral fuels and lubricants, and (4) Animal and vegetable oils, fats, waxes. The fact that the effects were so large for food, beverages, and tobacco and so much smaller for crude materials, fuels, and oils is consistent with the argument of Magee and Thompson (2010) that consumer preferences drove intra-imperial trade during the late 19th century. As they write, "it was emigration that conditioned consumption habits within the colonies such that their tastes, expectations and values were readily familiar, communicable and comprehensible to manufacturers back in Britain" (p. 118). Further unpacking the sources of heterogeneity across goods and time represents a promising avenue for future research.

#### 6 Historical discussion and conclusion

In this paper, we introduce a new dataset on the universe of British exports at the bilateral, commodity-level for the period from 1700 to 1899. Our hope is that the data will be useful to other economic historians exploring the causes and consequences of trade flows during a period of enormous technological and political change. Furthermore, we have used the data to explore the changing impacts of distance and empire on British exports over time. We have documented three striking empirical patterns. First, the British Empire was a powerful export-promoting force throughout these two centuries. At its height in the late 18th century the impact was huge. Any account of British trade during this period, and particularly in the decades prior to 1815, has to take seriously the impact of mercantilist legislation and overseas colonies: trade was a largely

political phenomenon during this period as has long been emphasized by a large scholarly 
literature on mercantilism. 
Second, this impact of empire declined in the 1780s as a result of the War of American 
Independence which led to a large and persistent trade flow being diverted to outside the 
empire. Setting aside that major shock to the imperial system, the link between empire 
and exports fell in the 1810s. This marked a transition away from mercantilism and 
protectionism which was largely completed by the 1840s. By the late 19th century, our 
main results imply that empire was still boosting British exports by roughly 170%, a 
sizable effect, but just a fraction of what the impact had been under the old mercantilist 
system. 
Finally, the negative impact of distance fell sharply from the 1780s onward. The timing 
corresponds with recent scholarship documenting an increase in shipping speeds from 
that decade, well before the onset of the steam technology associated with the Industrial 
Revolution. We view our results as providing support for authors such as Solar (2013), 
Kelly and Ó Gráda (2019), and others who have emphasized the role of copper sheathing, 
improved rigging, and other innovations in reducing sailing costs in the late 18th and 
early 19th centuries. 
These two centuries saw enormous changes in commercial policy, geopolitics, and 
technology. Thus, it would perhaps have been more surprising if the impact of distance 
and empire had remained constant throughout such a period of flux. An economist 
estimating gravity models in 1800 would have been wrong to assume that their lessons 
would hold a century or two later, and there may be a lesson there for economists today. 

#### References

Allen, R. C. (2003), “Progress and Poverty in Early Modern Europe.” Economic History Review 56(3): 
403–443. 
Anderson, J. E., and E. van Wincoop (2003), “Gravity with Gravitas: A Solution to the Border 
Puzzle.” American Economic Review 93(1): 170–192. 
Barjamovic, G., T. Chaney, K. Coşar, and A. Hortaçsu (2019), “Trade, Merchants, and the Lost Cities 
of the Bronze Age.” Quarterly Journal of Economics 134(3): 1455–1503. 
de Bromhead, A., A. Fernihough, M. Lampe and K.H. O’Rourke (2019), “When Britain Turned 
Inward.” American Economic Review 109(2): 325-352. 
Clark, G. N. (1938), Guide to English Commercial Statistics, 1696–1782. London: Royal Historical 
Society. 
Coe, D.T., A. Subramanian and N.T. Tamirisa (2007), “The Missing Globalization Puzzle: Evidence 
of the Declining Importance of Distance.” IMF Staff Papers 54(1): 34-58. 
Crafts, N.F.R. and T.C. Mills (2020), “Sooner than You Think: The Pre-1914 UK Productivity 
Slowdown was Victorian not Edwardian.” European Review of Economic History 24(4): 736– 
748. 
Dal Bo, E., K. Hutkova, L. Leucht, and N. Yuchtman (2025), “Dissecting the Sinews of Power: 
International Trade and the Rise of Britain’s Fiscal Military State, 1689–1823.”Journal of 
Economic History 85(2): 336–369. 
Davis, R. (1979), The Industrial Revolution and British Overseas Trade. Leicester: Leicester University 
Press. 
Deane, P. and W. A. Cole (1962), British Economic Growth, 1688–1959: Trends and Structure. 
Cambridge: Cambridge University Press. 
Disdier, A.-C. and K. Head (2008). “The Puzzling Persistence of the Distance Effect on Bilateral 
Trade.” Review of Economics and Statistics 90(1): 37-48. 
Eichengreen, B. and D.A.Irwin (1995), “Trade Blocs, Currency Blocs and the Reorientation of World 
Trade in the 1930s.” Journal of International Economics 38(1–2): 1-24. 

Fally, T. (2015), “Structural Gravity and Fixed Effects.” Journal of International Economics 97(1): 
76–85. 
Findlay, R. (1982), “Trade and Growth in the Industrial Revolution.” In C.P. Kindleberger and G. di 
Tella (eds.), Economics in the Long View: Essays in Honour of W. W. Rostow. London: Palgrave 
Macmillan, 178-188. 
Fletcher, M. E. (1958), “The Suez Canal and World Shipping, 1869-1914.” Journal of Economic 
History 18(4): 556–573. 
Flueckiger, M., E. Hornung, M. Larch, M. Ludiwg, and A. Mees (2022), “Roman Transport Network 
Connectivity and Economic Integration.” Review of Economic Studies 89(2): 774–810. 
Gowa, J. and R. Hicks (2013), “Politics, Institutions, and Trade: Lessons of the Interwar Era." 
International Organization 67(3): 439–467. 
Harley, C. K. (1988), “Ocean Freight Rates and Productivity, 1740-1913 - the Primacy of Mechanical 
Invention Reaffirmed.” Journal of Economic History 48(4): 851–876. 
Harley, C. K. and N. F. R. Crafts (2000), “Simulating the Two Views of the British Industrial 
Revolution.” Journal of Economic History 60(3): 819–841. 
Hatton, T. J. (2024), “Sailing Ship Technology, Navigation and the Duration of Voyages to Australia, 
1848-85.” Centre for Economic Policy Research Discussion Paper 19342. 
Head, K. and T. Mayer (2014), “Gravity Equations: Workhorse,Toolkit, and Cookbook.” In G. 
Gopinath, E. Helpman and K. Rogoff (eds.), Handbook of International Economics, Vol. 4. 
Amsterdam: Elsevier, 131-195. 
Head, K., T. Mayer, and J. Ries (2010), “The Erosion of Colonial Trade Linkages after Independence.” 
Journal of International Economics 81(1): 1–14. 
Imlah, A.H. (1948), “Real Values in British Foreign Trade, 1793-1853.” Journal of Economic History 
8(2): 133–152. 
Imlah, A.H. (1958), Economic Elements in the Pax Brittanica. Cambridge: Harvard University Press. 
Jacks, D. S., C. M. Meissner, and D. Novy (2011), “Trade Booms, Trade Busts, and Trade Costs.” 
Journal of International Economics 83(2): 185–201. 

Jacks, D. S., C. M. Meissner and N. Wolf (2024), “Suez.” NBER Working Paper No. 33250. 
Jacks, D. S., and D. Novy (2020), “Trade Blocs and Trade Wars during the Interwar Period.” Asian 
Economic Policy Review 15(1): 119–136. 
Jacks, D. S. and K. Pendakur (2010), “Global Trade and the Maritime Transport Revolution.” Review 
of Economics and Statistics 92(4): 745-755. 
Kelly, M. and C. Ó Gráda (2019), “Speed under Sail during the Early Industrial Revolution (c. 
1750–1830).” Economic History Review 72(2): 459–480. 
Kelly, M., C. Ó Gráda and P. M. Solar (2021), “Safety at Sea during the Industrial Revolution.” 
Journal of Economic History 81(1): 239–275. 
Larch, M., S. Shikher, and Y.V. Yotov (2025), “Estimating Gravity Equations: Theory Implications, 
Econometric Developments, and Practical Recommendations.” Review of International 
Economics. 33(5): 1066-1092. 
López-Córdova,J.E. and C.M. Meissner (2003), “Exchange-Rate Regimes and International Trade: 
Evidence from the Classical Gold Standard Era.” American Economic Review 93(1): 344-353. 
Magee, G.B. and A.S. Thompson (2010), Empire and Globalisation: Networks of People, Goods and 
Capital in the British World, c.1850-1914. Cambridge: Cambridge University Press. 
McCloskey, D.N. (1970), “Did Victorian Britain Fail?” Economic History Review 23(3): 446-459. 
Meyer, J.R. (1955), “An Input-Output Approach to Evaluating the Influence of Exports on British 
Industrial Production in the Late Nineteenth Century.” Explorations in Entrepreneurial 
History 8: 12-34. 
Mitchell, B.R. (1962), Abstract of British Historical Statistics. Cambridge: Cambridge University 
Press. 
Mitchener, K.J. and M. Weidenmier (2008), “Trade and Empire.” Economic Journal 118: 1805–1834. 
North, D. (1958), “Ocean Freight Rates and Economic Development 1730-1913.” Journal of Economic 
History 18(4): 537–555. 
North, D. C. (1968), “Sources of Productivity Change in Ocean Shipping, 1600-1850.” Journal of 
Political Economy 76(5): 953–970. 

O’Brien, P. K. (1988), “The Political Economy of British Taxation, 1660–1815.” Economic History 
Review 41(1): 1–32. 
O’Brien, P. K. and S. L. Engerman (1991), “Exports and the Growth of the British Economy from 
the Glorious Revolution to the Peace of Amiens.” In B.L. Solow (ed.), Slavery and the Rise of 
the Atlantic System. Cambridge: Cambridge University Press, 177–209. 
Ormrod, D. (2003), The Rise of Commercial Empires: England and the Netherlands in the Age of 
Mercantilism, 1650-1770. Cambridge: Cambridge University Press. 
Quah, D. (2011), “The Global Economy’s Shifting Centre of Gravity.” Global Policy 2(1): 3–9. 
Redding, S. J., and D. E. Weinstein (2019), “Aggregation and the Gravity Equation.” American 
Economic Review Papers and Proceedings 109: 450–455. 
Rönnbäck, K. (2012), “The Speed of Ships and Shipping Productivity in the Age of Sail.” European 
Review of Economic History 16(4): 469–489. 
Santos Silva, J. M. C., and S. Tenreyro (2006), “The Log of Gravity.” Review of Economics and 
Statistics 88(4): 641–658. 
Schlote, W. (1952), British Overseas Trade from 1700 to the 1930s. Oxford: Basil Blackwell. 
Schumpeter, E. B. (1960), English Overseas Trade Statistics, 1697–1808. Oxford: Clarendon Press. 
Solar, P. M. (2013). “Opening to the East: Shipping Between Europe and Asia, 1770–1830.” Journal 
of Economic History 73(3): 625–661. 
Solar, P. M. and L. Hens (2016), “Ship Speeds during the Industrial Revolution: East India Company 
Ships, 1770–1828.” European Review of Economic History 20(1): 66–78. 
Solar, P. M. and K. Rönnbäck (2015), “Copper Sheathing and the British Slave Trade.” Economic 
History Review 68(3): 806–829. 
Temin, P. (1997), “Two Views of the British Industrial Revolution.” Journal of Economic History 
57(1): 63–82. 
Wilson, C. (1978), Profit and Power: A Study of England and the Dutch Wars. The Hague: M. Nijhoff. 
Xu, C. (2022), “Reshaping Global Trade: The Immediate & Long-Term Effects of Bank Failures.” 
Quarterly Journal of Economics 137(4): 2107–2161. 

Yotov, Y.V. (2012), “A Simple Solution to the Distance Puzzle in International Trade.” Economics Letters 117(3): 794-798.

### Online Appendices

#### A Sources of British trade dataset by year

All sources are held by UK National Archives, as follows: 1700: Ledgers of Imports and Exports, CUST 3/4 1710: Ledgers of Imports and Exports, CUST 3/13 1720: Ledgers of Imports and Exports, CUST 3/22 1730: Ledgers of Imports and Exports, CUST 3/30 1740: Ledgers of Imports and Exports, CUST 3/40 1750: Ledgers of Imports and Exports, CUST 3/50 1760: Ledgers of Imports and Exports, CUST 3/60 1770: Ledgers of Imports and Exports, CUST 3/70 1780: Ledgers of Imports and Exports, CUST 3/80 1790: States of Navigation, Commerce and Revenue, CUST 17/12 1800: States of Navigation, Commerce and Revenue, CUST 17/22 1807: States of Navigation, Commerce and Revenue, CUST 17/29 1820: Ledgers of Exports of British Merchandise under Countries, CUST 8/11 1830: Ledgers of Exports of British Merchandise under Countries, CUST 8/31-32 1840: Ledgers of Exports of British Merchandise under Countries, CUST 8/51-52 1850: Ledgers of Exports of British Merchandise under Countries, CUST 8/71-72 1860: Ledgers of Exports of British Merchandise under Countries, CUST 8/91-92 1869: Ledgers of Exports of British Merchandise under Countries, CUST 8/109-110 1880: Ledgers of Exports of British Merchandise under Countries, CUST 8/121 1890: Ledgers of Exports of British Merchandise under Countries, CUST 8/131 1899: Ledgers of Exports of British Merchandise under Countries, CUST 8/140

A1

#### B Coverage of British trading partners in the dataset

Our sample includes the following 86 trading partners recorded as export destinations in the British customs ledgers from 1700 to 1899:

Abyssinia, Aden, Algeria, Arabia, Argentina, Australia, Austria-Hungary, Belgium, Bermuda, Bolivia, Brazil, British Borneo, British East Africa, British Guiana, British Honduras, British India, British New Guinea, British South Africa, British West Africa, British West Indies, Bulgaria, Canada, Central America, Chile, China, Colombia, Congo Free State, Cyprus, Danish West Indies, Denmark, Dutch East Indies, Dutch Guiana, Dutch West Indies, Ecuador, Egypt, Falkland Islands, Fiji Islands, France, French Guiana, French India, French Indochina, French West Africa, French West Indies, German East Africa, German New Guinea, German West Africa, Germany, Gibraltar, Greece, Haiti and Dominican Republic, Italy, Japan, Korea, Liberia, Madagascar, Malta, Mauritius, Mexico, Montenegro, Morocco, Netherlands, New Zealand, Norway, Paraguay, Persia, Peru, Philippine Islands, Portugal, Portuguese East Africa, Portuguese India, Portuguese West Africa, Reunion Island, Romania, Russia, Siam, Spain, Spanish Africa, Spanish West Indies, Straits Settlements, Sweden, Tripoli and Tunis, Turkey, United States, Uruguay, Venezuela, and Zanzibar.

The map in Figure A1 shows these destinations.

Figure A1: British export destinations, 1700–1899

##### 4.2 PPMLandtheintensivemarginofBritishexports

Themoststraightforwardwaytoproceedisin estimating equation(5),usingvariationintheintensivemarginofBritishexports(thatis,howmuchBritainexportstothe99countriesacrossthe57 industriesinourdata). Asmentionedbefore,wesimultaneouslyobtaintimevaryingdistanceandempirecoefficientsby runningaseries ofannual (benchmark-year)cross-sectiongravityregressionswith

PPML.Figure5depictsthecoefficientpointestimatesandassociated95%standarderrorbands for the two key dependent variables: bilateral distance (log, continuous) andmembershipintheBritishEmpire (binaryindicator).Turningfirsttobilateraldistance,theelasticityofBritishexportsisfirstestimatedin1700tobeequalto-1.11 and,thus,closely inlinewithresultsfor thepost-WorldWarIIera(HeadandMayer,2014).Thispointestimateis also precisely estimated and statistically significant at conventional levels (z =

3.53).Abstractingawayfromthevaluesofthestandarderrorbands,weseethatthisisfollowedbyaroughconstancy inthedistanceelasticity from1710to1780,withanaveragevalueof-1.03.Fromthispointonthingsdramaticallychange,andthe distanceelasticitycollapsesinabsolutevalue,averagingjust-0.11 overtheentire19th century.Itisalsogrosslystatisticallyinsignificantthroughoutthisperiod.Thus,weareconfrontedwiththecuriousresultthatthe

A2

#### C Imperial status and maritime distances

Table A1 gives for each destination in our sample the year in which it was incorporated into the British Empire while Table A2 gives for each destination its principal port and the distance in nautical miles to London or Liverpool (whichever is shorter), before and after the opening of the Suez Canal.

| | Destination | | Year | | |
| --- | --- | --- | --- | --- | --- |
| | Aden | | 1839 | | |
| | Australia | | 1788 | | |
| | Bermuda | | 1684 | | |
| | British Borneo | | 1888 | | |
| | British East | Africa | 1888 | | |
| | British Guiana | | 1796 | | |
| | British Honduras | | 1749 | | |
| | British India | | 1608 | | |
| | British New | Guinea | 1888 | | |
| | British South | Africa | 1795 | | |
| | British West | Africa | 1821 | | |
| | British West | Indies | 1623 | | |
| | Canada | | 1763 | | |
| | Cyprus | | 1878 | | |
| | Egypt | | 1882 | | |
| | Falkland Islands | | 1765 | | |
| | Fiji Islands | | 1840 | | |
| | Gibraltar | | 1704 | | |
| | Malta | | 1800 | | |
| | Mauritius | | 1810 | | |
| | New Zealand | | 1841 | | |
| | Straits Settlements | | 1786 | | |
| | United States | | 1607 | | |

Table A1: Year of incorporation into the British Empire

A3

Table A2: Maritime distances before and after the opening of the Suez Canal

| Destination | | | | | | | Pre-Suez | | | | | | PortCode | | | Distance | | | Post-Suez | | | | | | PortCode | | | Distance | | | Difference | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Abyssinia | | | | | | | Massawa | | | | | | ERMSW | | | 10645.1 | | | Massawa | | | | | | ERMSW | | | 4314.3 | | | -6330.8 | | |
| Aden | | | | | | | Aden | | | | | | YEADE | | | 10297.2 | | | Aden | | | | | | YEADE | | | 4720.8 | | | -5576.4 | | |
| Algeria | | | | | | | Algiers | | | | | | DZALG | | | 1755.3 | | | Algiers | | | | | | DZALG | | | 1755.3 | | | 0.0 | | |
| Arabia | | | | | | | Muscat | | | | | | OMMCT | | | 10594.2 | | | Jeddah | | | | | | SAJED | | | 3974.4 | | | -6619.8 | | |
| Argentina | | | | | | | Buenos | | Aires | | | | ARBUE | | | 6294.9 | | | Buenos | | Aires | | | | ARBUE | | | 6294.9 | | | 0.0 | | |
| Australia | | | | | | | Perth | | | | | | AUPER | | | 10908.6 | | | Perth | | | | | | AUPER | | | 9599.6 | | | -1309.0 | | |
| Austria | | | Hungary | | | | Split | | | | | | HRSPU | | | 2865.6 | | | Split | | | | | | HRSPU | | | 2865.6 | | | 0.0 | | |
| Belgium | | | | | | | Antwerp | | | | | | BEANR | | | 193.3 | | | Antwerp | | | | | | BEANR | | | 193.3 | | | 0.0 | | |
| Bermuda | | | | | | | Hamilton | | | | | | BMBDA | | | 2975.3 | | | Hamilton | | | | | | BMBDA | | | 2975.3 | | | 0.0 | | |
| Bolivia | | | | | | | Antofagasta | | | | | | CLANF | | | 9355.7 | | | Antofagasta | | | | | | CLANF | | | 9355.7 | | | 0.0 | | |
| Brazil | | | | | | | Belem | | | | | | BRBEL | | | 4053.9 | | | Belem | | | | | | BRBEL | | | 4053.9 | | | 0.0 | | |
| British | | Borneo | | | | | Muara | | | | | | BNMUA | | | 12176.3 | | | Muara | | | | | | BNMUA | | | 9058.2 | | | -3118.1 | | |
| British | | East | | Africa | | | Mombasa | | | | | | KEMBA | | | 8605.1 | | | Mombasa | | | | | | KEMBA | | | 6507.7 | | | -2097.4 | | |
| British | | Guiana | | | | | Georgetown | | | | | | GYGEO | | | 3918.0 | | | Georgetown | | | | | | GYGEO | | | 3918.0 | | | 0.0 | | |
| British | | Honduras | | | | | Belize | | | | | | BZBZE | | | 4540.0 | | | Belize | | | | | | BZBZE | | | 4540.0 | | | 0.0 | | |
| British | | India | | | | | Colombo | | | | | | LKCMB | | | 10466.6 | | | Mumbai | | | | | | INBOM | | | 6342.9 | | | -4123.8 | | |
| British | | New | | Guinea | | | Port | Moresby | | | | | PGPOM | | | 13271.8 | | | Port | Moresby | | | | | PGPOM | | | 11077.4 | | | -2194.4 | | |
| British | | South | | Africa | | | Cape | Town | | | | | ZACPT | | | 6082.1 | | | Cape | Town | | | | | ZACPT | | | 6082.1 | | | 0.0 | | |
| British | | West | | Africa | | | Banjul | | | | | | GMBJL | | | 2604.0 | | | Banjul | | | | | | GMBJL | | | 2604.0 | | | 0.0 | | |
| British | | West | | Indies | | | Kingston | | | | | | JMKIN | | | 4104.6 | | | Kingston | | | | | | JMKIN | | | 4104.6 | | | 0.0 | | |
| Bulgaria | | | | | | | Varna | | | | | | BGVAR | | | 3310.1 | | | Varna | | | | | | BGVAR | | | 3310.1 | | | 0.0 | | |
| Canada | | | | | | | Halifax | | | | | | CAHAL | | | 2486.8 | | | Halifax | | | | | | CAHAL | | | 2486.8 | | | 0.0 | | |
| Central | | | America | | | | Puerto | | Barrios | | | | GTPBR | | | 4636.9 | | | Puerto | | Barrios | | | | GTPBR | | | 4636.9 | | | 0.0 | | |
| Chile | | | | | | | Valparaiso | | | | | | CLVAP | | | 8819.6 | | | Valparaiso | | | | | | CLVAP | | | 8819.6 | | | 0.0 | | |
| China | | | | | | | Canton | | | | | | CNCAN | | | 13043.2 | | | Canton | | | | | | CNCAN | | | 9787.3 | | | -3255.9 | | |
| Colombia | | | | | | | Cartagena | | | | | | COCTG | | | 4379.0 | | | Cartagena | | | | | | COCTG | | | 4379.0 | | | 0.0 | | |
| Congo | | Free | | State | | | Matadi | | | | | | CDMAT | | | 4851.8 | | | Matadi | | | | | | CDMAT | | | 4851.8 | | | 0.0 | | |
| Cyprus | | | | | | | Larnaca | | | | | | CYLCA | | | 3298.4 | | | Larnaca | | | | | | CYLCA | | | 3298.4 | | | 0.0 | | |
| Danish | | | West | Indies | | | Charlotte | | | Amalie | | | VICHA | | | 3617.3 | | | Charlotte | | | Amalie | | | VICHA | | | 3617.3 | | | 0.0 | | |
| Denmark | | | | | | | Copenhagen | | | | | | DKCPH | | | 737.0 | | | Copenhagen | | | | | | DKCPH | | | 737.0 | | | 0.0 | | |
| Dutch | | East | | Indies | | | Jakarta | | | | | | IDJKT | | | 11284.8 | | | Jakarta | | | | | | IDJKT | | | 8593.8 | | | -2691.0 | | |
| Dutch | | Guiana | | | | | Paramaribo | | | | | | SRPBM | | | 3877.9 | | | Paramaribo | | | | | | SRPBM | | | 3877.9 | | | 0.0 | | |
| Dutch | | West | | Indies | | | Willemstad | | | | | | CWWIL | | | 4100.4 | | | Willemstad | | | | | | CWWIL | | | 4100.4 | | | 0.0 | | |
| Ecuador | | | | | | | Guayaquil | | | | | | ECGYE | | | 10666.4 | | | Guayaquil | | | | | | ECGYE | | | 10666.4 | | | 0.0 | | |
| Egypt | | | | | | | Alexandria | | | | | | EGALY | | | 3133.2 | | | Alexandria | | | | | | EGALY | | | 3133.2 | | | 0.0 | | |
| Falkland | | | Islands | | | | Port | Stanley | | | | | FKPSY | | | 6968.6 | | | Port | Stanley | | | | | FKPSY | | | 6968.6 | | | 0.0 | | |
| Fiji | Islands | | | | | | Suva | | | | | | FJSUV | | | 12938.1 | | | Suva | | | | | | FJSUV | | | 12938.1 | | | 0.0 | | |
| France | | | | | | | Dunkirk | | | | | | FRIRK | | | 111.4 | | | Dunkirk | | | | | | FRIRK | | | 111.4 | | | 0.0 | | |
| French | | | Guiana | | | | Cayenne | | | | | | GFCAY | | | 3856.5 | | | Cayenne | | | | | | GFCAY | | | 3856.5 | | | 0.0 | | |
| French | | | India | | | | Pondicherry | | | | | | INPNY | | | 10843.7 | | | Pondicherry | | | | | | INPNY | | | 7241.3 | | | -3602.4 | | |
| French | | | Indochina | | | | Saigon | | | | | | VNSIT | | | 12267.6 | | | Saigon | | | | | | VNSIT | | | 8948.4 | | | -3319.2 | | |
| French | | | West | Africa | | | Dakar | | | | | | SNDKR | | | 2509.9 | | | Dakar | | | | | | SNDKR | | | 2509.9 | | | 0.0 | | |
| French | | | West | Indies | | | Pointe-à-Pitre | | | | | | GPPTP | | | 3743.0 | | | Pointe-à-Pitre | | | | | | GPPTP | | | 3743.0 | | | 0.0 | | |
| German | | | East | Africa | | | Dar | es | Salaam | | | | TZDAR | | | 8466.2 | | | Dar | es | Salaam | | | | TZDAR | | | 6598.3 | | | -1867.9 | | |
| German | | | New | Guinea | | | Finschhafen | | | | | | PGFIN | | | 13985.3 | | | Finschhafen | | | | | | PGFIN | | | 11321.7 | | | -2663.6 | | |
| German | | | West | Africa | | | Lomé | | | | | | TGLFW | | | 4014.8 | | | Lomé | | | | | | TGLFW | | | 4014.8 | | | 0.0 | | |
| Germany | | | | | | | Bremerhaven | | | | | | DEBRV | | | 412.9 | | | Bremerhaven | | | | | | DEBRV | | | 412.9 | | | 0.0 | | |
| Gibraltar | | | | | | | Gibraltar | | | | | | GIGIB | | | 1339.8 | | | Gibraltar | | | | | | GIGIB | | | 1339.8 | | | 0.0 | | |
| Greece | | | | | | | Piraeus | | | | | | GRPIR | | | 2780.7 | | | Piraeus | | | | | | GRPIR | | | 2780.7 | | | 0.0 | | |
| Haiti | | & | Dominican | | | Republic | Port-au-Prince | | | | | | HTPAP | | | 4005.8 | | | Port-au-Prince | | | | | | HTPAP | | | 4005.8 | | | 0.0 | | |
| Italy | | | | | | | Genoa | | | | | | ITGOA | | | 2204.3 | | | Genoa | | | | | | ITGOA | | | 2204.3 | | | 0.0 | | |
| Japan | | | | | | | Nagasaki | | | | | | JPNGS | | | 14010.2 | | | Nagasaki | | | | | | JPNGS | | | 10755.7 | | | -3254.5 | | |
| Korea | | | | | | | Busan | | | | | | KRPUS | | | 14115.2 | | | Busan | | | | | | KRPUS | | | 10839.0 | | | -3276.1 | | |
| Liberia | | | | | | | Monrovia | | | | | | LRMLW | | | 3211.2 | | | Monrovia | | | | | | LRMLW | | | 3211.2 | | | 0.0 | | |
| Madagascar | | | | | | | Toamasina | | | | | | MGTOA | | | 8233.9 | | | Toamasina | | | | | | MGTOA | | | 6966.3 | | | -1267.6 | | |
| Malta | | | | | | | Valletta | | | | | | MTMLA | | | 2321.8 | | | Valletta | | | | | | MTMLA | | | 2321.8 | | | 0.0 | | |
| Mauritius | | | | | | | Port | Louis | | | | | MUPLU | | | 8380.7 | | | Port | Louis | | | | | MUPLU | | | 7046.5 | | | -1334.2 | | |
| Mexico | | | | | | | Veracruz | | | | | | MXVER | | | 4808.2 | | | Veracruz | | | | | | MXVER | | | 4808.2 | | | 0.0 | | |
| Morocco | | | | | | | Safi | | | | | | MASFI | | | 1388.7 | | | Safi | | | | | | MASFI | | | 1388.7 | | | 0.0 | | |
| Montenegro | | | | | | | Bar | | | | | | MEBAR | | | 2745.7 | | | Bar | | | | | | MEBAR | | | 2745.7 | | | 0.0 | | |
| Netherlands | | | | | | | Amsterdam | | | | | | NLAMS | | | 208.3 | | | Amsterdam | | | | | | NLAMS | | | 208.3 | | | 0.0 | | |
| New | Zealand | | | | | | Auckland | | | | | | NZAKL | | | 12412.4 | | | Auckland | | | | | | NZAKL | | | 12412.4 | | | 0.0 | | |
| Norway | | | | | | | Bergen | | | | | | NOBGO | | | 634.2 | | | Bergen | | | | | | NOBGO | | | 634.2 | | | 0.0 | | |
| Paraguay | | | | | | | Asuncion | | | | | | PYASU | | | 7120.4 | | | Asuncion | | | | | | PYASU | | | 7120.4 | | | 0.0 | | |
| Persia | | | | | | | Bushehr | | | | | | IRBUZ | | | 11191.3 | | | Bushehr | | | | | | IRBUZ | | | 6519.9 | | | -4671.4 | | |
| Peru | | | | | | | Callao | | | | | | PECLL | | | 10015.9 | | | Callao | | | | | | PECLL | | | 10015.9 | | | 0.0 | | |
| Philippine | | | | Islands | | | Manila | | | | | | PHMNL | | | 12819.0 | | | Manila | | | | | | PHMNL | | | 9669.3 | | | -3149.7 | | |
| Portugal | | | | | | | Lisbon | | | | | | PTLIS | | | 1035.0 | | | Lisbon | | | | | | PTLIS | | | 1035.0 | | | 0.0 | | |
| Portuguese | | | | East | Africa | | Maputo | | | | | | MZMPM | | | 7189.8 | | | Maputo | | | | | | MZMPM | | | 7189.8 | | | 0.0 | | |
| Portuguese | | | | India | | | Panaji | | Port | | | | INPAN | | | 10587.8 | | | Panaji | | Port | | | | INPAN | | | 6373.7 | | | -4214.1 | | |
| Portuguese | | | | West | Africa | | Mindelo | | | | | | CVMIN | | | 2467.5 | | | Mindelo | | | | | | CVMIN | | | 2467.5 | | | 0.0 | | |
| Reunion | | | Island | | | | Pointe | | des | | Galets | | REPDG | | | 8248.5 | | | Pointe | | des | | Galets | | REPDG | | | 7069.9 | | | -1178.6 | | |
| Romania | | | | | | | Constanta | | | | | | ROCND | | | 3354.7 | | | Constanta | | | | | | ROCND | | | 3354.7 | | | 0.0 | | |
| Russia | | | | | | | Saint | Petersburg | | | | | RULED | | | 1441.7 | | | Saint | Petersburg | | | | | RULED | | | 1441.7 | | | 0.0 | | |
| Siam | | | | | | | Bangkok | | | | | | THBKK | | | 12456.6 | | | Bangkok | | | | | | THBKK | | | 9136.0 | | | -3320.6 | | |
| Spain | | | | | | | Bilbao | | | | | | ESBIO | | | 719.0 | | | Bilbao | | | | | | ESBIO | | | 719.0 | | | 0.0 | | |
| Spanish | | | Africa | | | | Port | Clarence | | | | | GQSSG | | | 4414.6 | | | Port | Clarence | | | | | GQSSG | | | 4414.6 | | | 0.0 | | |
| Spanish | | | West | Indies | | | San | Juan | | | | | PRSJU | | | 3641.9 | | | San | Juan | | | | | PRSJU | | | 3641.9 | | | 0.0 | | |
| Straits | | Settlements | | | | | Singapore | | | | | | SGSIN | | | 11730.1 | | | Singapore | | | | | | SGSIN | | | 8321.4 | | | -3408.8 | | |
| Sweden | | | | | | | Gothenburg | | | | | | SEGOT | | | 629.0 | | | Gothenburg | | | | | | SEGOT | | | 629.0 | | | 0.0 | | |
| Tripoli | | and | | Tunis | | | Tunis | | | | | | TNTUN | | | 2134.5 | | | Tunis | | | | | | TNTUN | | | 2134.5 | | | 0.0 | | |
| Turkey | | | | | | | Izmir | | | | | | TRIZM | | | 3013.9 | | | Izmir | | | | | | TRIZM | | | 3013.9 | | | 0.0 | | |
| United | | | States | | | | New | York | | | | | USNYC | | | 3040.0 | | | New | York | | | | | USNYC | | | 3040.0 | | | 0.0 | | |
| Uruguay | | | | | | | Montevideo | | | | | | UYMVD | | | 6183.2 | | | Montevideo | | | | | | UYMVD | | | 6183.2 | | | 0.0 | | |
| Venezuela | | | | | | | La | Guaira | | | | | VELAG | | | 4098.1 | | | La | Guaira | | | | | VELAG | | | 4098.1 | | | 0.0 | | |
| Zanzibar | | | | | | | Zanzibar | | | | | | TZZNZ | | | 8500.7 | | | Zanzibar | | | | | | TZZNZ | | | 6632.9 | | | -1867.9 | | |

A4

#### D Proxy for GDP

Table A3 reports the coverage for estimates of GDP per capita in the Maddison Project Database 2020 for our dataset’s destinations and years. “/” represents recorded observations while “-” represents linear interpolations. Empty cells represent missing observations. Thus, we have 537 observations for GDP per capita with interpolation over 1806 possible destination-year combinations (i.e., a coverage ratio of 30%).

Table A4 reports the estimates of population from the Our World in Data website for our dataset’s destinations and years. “/” represents recorded observations while “-” represents linear interpolations. Thus, we have 1806 observations for population with interpolation over 1806 possible destination-year combinations (i.e., a coverage ratio of 100%).

Table A5 summarizes the consequent coverage for the GDP proxy for our dataset’s destinations and years. Cells in dark grey are those for which we have both estimates of GDP per capita and population. Cells in light grey are those for which we only have estimates of population and to which we assign a "representative" value of GDP per capita equal to that for Turkey from 1700 to 1899 as discussed in the text.

A5

Table A3: GDP per capita (Maddison Project Database 2020)

17 18 00 10 20 30 40 50 60 70 80 90 00 07 20 30 40 50 60 69 80 90 99

Abyssinia 
Aden / - - - - / - - / 
Algeria 
Arabia 
Argentina / - / - - / / / / / / 
Australia / / / / / / / / / 
Austria Hungary / / / / / / / / / 
Belgium / - - - - / - - - - - - / - - / / / / / / 
Bermuda 
Bolivia / - - / - / - / / 
Brazil / - / - - / / / / / / 
British Borneo 
British East Africa 
British Guiana 
British Honduras 
British India / - - - - / - - - - - - - - - / - / - / / 
British New Guinea 
British South Africa / / / / / / / / / / / / / / / / / / / / / 
British West Africa 
British West Indies / - - / / / / / / 
Bulgaria 
Canada / / / / / / / / / 
Central America 
Chile / / / / / / / / / / / 
China / / / / / / / / / / / / / / / / - / - / / 
Colombia / - / - - / / / / / / 
Congo Free State 
Cyprus 
Danish West Indies 
Denmark / / / / / / / / / 
Dutch East Indies / / / / / / / / / 
Dutch Guiana 
Dutch West Indies 
Ecuador / / / / 
Egypt / - - - - / - - / 
Falkland Islands 
Fiji Islands 
France / / / / / / / / / / / / / / / / / / / / / 
French Guiana 
French India 
French Indochina 
French West Africa 
French West Indies 
German East Africa 
German New Guinea 
German West Africa 
Germany / - - - - / - - - - / - / - - / / / / / / 
Gibraltar 
Greece / / / / / / / 
Haiti and Dominican Republic 
Italy / / / / / / / / / / / / / / / / / / / / / 
Japan / - - - - / - - - - / - / - - / - / - / / 
Korea 
Liberia 
Madagascar 
Malta 
Mauritius 
Mexico / / / / / / / / / / / / / / / / / / / / / 
Montenegro 
Morocco / - - - - / - - / 
Netherlands / / / / / / / / / / / / / / / / / / / / / 
New Zealand / - - / / / / / / 
Norway / / / / / / / / / 
Paraguay 
Persia 
Peru / / / / / / / / / / / / / / / / / / / / / 
Philippine Islands / - - - - / - - / 
Portugal / / / / / / / / / / / / / / / / / / / / / 
Portuguese East Africa 
Portuguese India 
Portuguese West Africa 
Reunion Island 
Romania / / / / 
Russia / / 
Siam / - - - - / - - / 
Spain / - - / / / / / / 
Spanish Africa 
Spanish West Indies 
Straits Settlements / - - / 
Sweden / / / / / / / / / / / / / / / / / / / / / 
Tripoli and Tunis 
Turkey / - - - - / - - - - - - / - - - - / - - / 
United States / - / - - - - - - - / / / / / / / / / / / 
Uruguay / - / - - / / / / / / 
Venezuela / - / / / / / / / / / 
Zanzibar 

A6

Table A4: Population (Our World in Data)

17 18 00 10 20 30 40 50 60 70 80 90 00 07 20 30 40 50 60 69 80 90 99 Abyssinia / / / / / / / / / / / / / / / / / / / / / Aden / / / / / / / / / / / / / / / / / / / / / Algeria / / / / / / / / / / / / / / / / / / / / / Arabia / / / / / / / / / / / / / / / / / / / / / Argentina / / / / / / / / / / / / / / / / / / / / / Australia / / / / / / / / / / / / / / / / / / / / / Austria Hungary / / / / / / / / / / / / / / / / / / / / / Belgium / / / / / / / / / / / / / / / / / / / / / Bermuda / - - / - - - - - - / - - - - - - - - - / Bolivia / / / / / / / / / / / / / / / / / / / / / Brazil / / / / / / / / / / / / / / / / / / / / / British Borneo / / / / / / / / / / / / / / / / / / / / / British East Africa / / / / / / / / / / / / / / / / / / / / / British Guiana / / / / / / / / / / / / / / / / / / / / / British Honduras / / / / / / / / / / / / / / / / / / / / / British India / / / / / / / / / / / / / / / / / / / / / British New Guinea / / / / / / / / / / / / / / / / / / / / / British South Africa / / / / / / / / / / / / / / / / / / / / / British West Africa / / / / / / / / / / / / / / / / / / / / / British West Indies / / / / / / / / / / / / / / / / / / / / / Bulgaria / / / / / / / / / / / / / / / / / / / / / Canada / / / / / / / / / / / / / / / / / / / / / Central America / / / / / / / / / / / / / / / / / / / / / Chile / / / / / / / / / / / / / / / / / / / / / China / / / / / / / / / / / / / / / / / / / / / Colombia / / / / / / / / / / / / / / / / / / / / / Congo Free State / / / / / / / / / / / / / / / / / / / / / Cyprus / / / / / / / / / / / / / / / / / / / / / Danish West Indies / - - - - - - - - - / - - - - - - - - - / Denmark / / / / / / / / / / / / / / / / / / / / / Dutch East Indies / / / / / / / / / / / / / / / / / / / / / Dutch Guiana / / / / / / / / / / / / / / / / / / / / / Dutch West Indies / / / / / / / / / / / / / / / / / / / / / Ecuador / / / / / / / / / / / / / / / / / / / / / Egypt / / / / / / / / / / / / / / / / / / / / / Falkland Islands / / / / / / / / / / / / / / / / / / / / / Fiji Islands / / / / / / / / / / / / / / / / / / / / / France / / / / / / / / / / / / / / / / / / / / / French Guiana / / / / / / / / / / / / / / / / / / / / / French India / - - - - - - - - - / - - - - - - - - - / French Indochina / / / / / / / / / / / / / / / / / / / / / French West Africa / / / / / / / / / / / / / / / / / / / / / French West Indies / / / / / / / / / / / / / / / / / / / / / German East Africa / / / / / / / / / / / / / / / / / / / / / German New Guinea / / / / / / / / / / / / / / / / / / / / / German West Africa / / / / / / / / / / / / / / / / / / / / / Germany / / / / / / / / / / / / / / / / / / / / / Gibraltar / - - - - - - - - - / - - - - - - - - - / Greece / / / / / / / / / / / / / / / / / / / / / Haiti and Dominican Republic / / / / / / / / / / / / / / / / / / / / / Italy / / / / / / / / / / / / / / / / / / / / / Japan / / / / / / / / / / / / / / / / / / / / / Korea / / / / / / / / / / / / / / / / / / / / / Liberia / / / / / / / / / / / / / / / / / / / / / Madagascar / / / / / / / / / / / / / / / / / / / / / Malta / / / / / / / / / / / / / / / / / / / / / Mauritius / / / / / / / / / / / / / / / / / / / / / Mexico / / / / / / / / / / / / / / / / / / / / / Montenegro / / / / / / / / / / / / / / / / / / / / / Morocco / / / / / / / / / / / / / / / / / / / / / Netherlands / / / / / / / / / / / / / / / / / / / / / New Zealand / / / / / / / / / / / / / / / / / / / / / Norway / / / / / / / / / / / / / / / / / / / / / Paraguay / / / / / / / / / / / / / / / / / / / / / Persia / / / / / / / / / / / / / / / / / / / / / Peru / / / / / / / / / / / / / / / / / / / / / Philippine Islands / / / / / / / / / / / / / / / / / / / / / Portugal / / / / / / / / / / / / / / / / / / / / / Portuguese East Africa / / / / / / / / / / / / / / / / / / / / / Portuguese India / - - - - - - - - - / - - - - - - - - - / Portuguese West Africa / / / / / / / / / / / / / / / / / / / / / Reunion Island / / / / / / / / / / / / / / / / / / / / / Romania / / / / / / / / / / / / / / / / / / / / / Russia / / / / / / / / / / / / / / / / / / / / / Siam / / / / / / / / / / / / / / / / / / / / / Spain / / / / / / / / / / / / / / / / / / / / / Spanish Africa / - - - - - - - - - / - - - - - - - - - / Spanish West Indies / / / / / / / / / / / / / / / / / / / / / Straits Settlements / / / / / / / / / / / / / / / / / / / / / Sweden / / / / / / / / / / / / / / / / / / / / / Tripoli and Tunis / / / / / / / / / / / / / / / / / / / / / Turkey / / / / / / / / / / / / / / / / / / / / / United States / / / / / / / / / / / / / / / / / / / / / Uruguay / / / / / / / / / / / / / / / / / / / / / Venezuela / / / / / / / / / / / / / / / / / / / / / Zanzibar / - - - - - - - - - / - - - - - - - - - /

A7

Table A5: Proxy for GDP

17 18 00 10 20 30 40 50 60 70 80 90 00 07 20 30 40 50 60 69 80 90 99

Abyssinia 
Aden 
Algeria 
Arabia 
Argentina 
Australia 
Austria Hungary 
Belgium 
Bermuda 
Bolivia 
Brazil 
British Borneo 
British East Africa 
British Guiana 
British Honduras 
British India 
British New Guinea 
British South Africa 
British West Africa 
British West Indies 
Bulgaria 
Canada 
Central America 
Chile 
China 
Colombia 
Congo Free State 
Cyprus 
Danish West Indies 
Denmark 
Dutch East Indies 
Dutch Guiana 
Dutch West Indies 
Ecuador 
Egypt 
Falkland Islands 
Fiji Islands 
France 
French Guiana 
French India 
French Indochina 
French West Africa 
French West Indies 
German East Africa 
German New Guinea 
German West Africa 
Germany 
Gibraltar 
Greece 
Haiti and Dominican Republic 
Italy 
Japan 
Korea 
Liberia 
Madagascar 
Malta 
Mauritius 
Mexico 
Montenegro 
Morocco 
Netherlands 
New Zealand 
Norway 
Paraguay 
Persia 
Peru 
Philippine Islands 
Portugal 
Portuguese East Africa 
Portuguese India 
Portuguese West Africa 
Reunion Island 
Romania 
Russia 
Siam 
Spain 
Spanish Africa 
Spanish West Indies 
Straits Settlements 
Sweden 
Tripoli and Tunis 
Turkey 
United States 
Uruguay 
Venezuela 
Zanzibar 

A8

#### E Robustness exercises

| | ln(DISTjt) | | | -0.397 | | | | -0.422 | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | (0.087)∗∗∗ | | | | (0.063)∗∗∗ | | | | |
| | EMP | IREjt | | 1.105 | | | | 1.237 | | | |
| | | | (0.331)∗∗∗ | | | | (0.343)∗∗∗ | | | | |
| | ln(GDPjt) | | | 0.589 | | | | 0.708 | | | |
| | | | (0.083)∗∗∗ | | | | (0.098)∗∗∗ | | | | |
| | ln(DECGjt) | | | 0.478 | | | | 0.609 | | | |
| | | | | (0.290)∗ | | | | (0.371) | | | |
| | W ARjt | | | -0.752 | | | | -1.816 | | | |
| | | | | (0.519) | | | (0.422)∗∗∗ | | | | |
| | Constant | | | -4.507 | | | | -8.439 | | | |
| | | | | (3.671) | | | | (5.033)∗ | | | |
| | N | | | 102,942 | | | | 79,034 | | | |
| | .1, p < ∗ | .05, p < ∗∗ | ∗∗∗ | p | .01. < | | | | | | |

This section of the appendix includes all the robustness exercises that we refer to in the main text.

• The first column of Table A6 replicates the results from column (2) of Table 1 but with only time fixed effects. The results demonstrate that due to lack of enough variation in the data the impact of wars (W ARjt) is less precisely estimated once time fixed effects are included. The second column of Table A6 replicates the estimates from column (1) of Table 1 but based on the sample from column (2) of Table 1. These estimates confirm that the differences between the first two columns of Table 1 are indeed driven by the division-year fixed effects and not by the different numbers of observations. Table A6: Panel Gravity Estimates, 1700-1899 (1) (2) Time FEs Same Sample 

A9

• Figure A2 replicates the results from Figure 6 but based on a series of cross-section estimates.

The cross-section results are consistent with our main panel estimates. The only outlier is

the estimate on distance in 1800.

Figure A2: Evolution of Distance and Empire Effects (annual cross-sections)

-2 -1.5 -1 -.5

0

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900

year

Distance Estimate 95% Confidence Interval

Evolution of the effects of Distance

0

1

2

3

4

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900

year

Empire Estimate 95% Confidence Interval

Evolution of the effects of Empire

• Figure A3 replicates the results from Figure 6 but after allowing for division-specific GDP effects. Once again, the new results are consistent with our main estimates.

Figure A3: Evolution of Distance and Empire Effects (division-specific GDP effects)

-1.5 -1 -.5

0

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900

year

Distance Estimate 95% Confidence Interval

Evolution of the effects of Distance

0

1

2

3

4

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900

year

Empire Estimate 95% Confidence Interval

Evolution of the effects of Empire

A10

• Figure A4 replicates the results from Figure 6 but using (the log of) population to control for country size. The new results are consistent with our main estimates.

Figure A4: Evolution of Distance and Empire Effects (population as size control)

-1.5 -1 -.5

0

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900

year Distance Estimate 95% Confidence Interval

Evolution of the effects of Distance

0

1

2

3

4

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900

year Empire Estimate 95% Confidence Interval

Evolution of the effects of Empire

• The results in Figure A5 replicate the results from Figure 6 but after adding destination fixed effects. Two main messages stand out from Figure A5. First, the magnitudes of our estimates of the effects of distance and the empire change. This is consistent with the results from

Table 1 and the accompanying discussion. Second, and more important for our purposes, the evolution over time of the distance and empire estimates remains similar to our main

findings.

Figure A5: Evolution of Distance and Empire Effects (destination fixed effects)

-3 -2 -1

0

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900

year Distance Estimate 95% Confidence Interval

Evolution of the effects of Distance

-1

0

1

2

3

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900

year Empire Estimate 95% Confidence Interval

Evolution of the effects of Empire

A11

• The results in Figure A6 replicate the results from Figure 6 but with destination-product fixed effects. The results from this specification are very similar to those from Figure A5 which were obtained with destination fixed effects only. 

Figure A6: Evolution of Distance and Empire Effects (destination-product fixed effects)

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Distance Estimate 95% Confidence Interval

Evolution of the effects of Distance

-1

0

1

2

3

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Empire Estimate 95% Confidence Interval

Evolution of the effects of Empire

• Figure A7 replicates the results from Figure 6 but using OLS. In terms of average magnitude, the OLS estimates of the effects of distance are similar to our main results. However, their evolution over time is quite different. The evolution of the empire effects in Figure A7 is 

similar to our main findings, but the OLS empire estimates are significantly larger than the corresponding PPML estimates in the 1800s and there are a few outliers, e.g., the estimate on distance in 1780 and the empire estimates in 1770 and 1790. As argued by Santos Silva and

Tenreyro (2006), the OLS gravity estimates are inconsistent and, therefore, we rely on the PPML estimator to obtain our main results.

Figure A7: Evolution of Distance and Empire Effects (estimation via OLS)

-1.5 -1 -.5

0

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Distance Estimate 95% Confidence Interval

Evolution of the effects of Distance

1

2

3

4

5

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Empire Estimate 95% Confidence Interval

Evolution of the effects of Empire

• Figure A8 replicates the results from Figure 6, but instead of using distance from the global economic center of gravity as a proxy for multilateral resistance, it uses remoteness indices for each destination. These are constructed as GDP-weighted, great-circle distances between each destination and all of its trading partners. The evolution over time of the distance and empire estimates remains very similar to our main findings.

A12

Figure A8: Evolution of Distance and Empire Effects (IMR controls)

-1.5 -1 -.5

0

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Distance Estimate 95% Confidence Interval

Evolution of the effects of Distance

0

1

2

3

4

5

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Empire Estimate 95% Confidence Interval

Evolution of the effects of Empire

• Figure A9 replicates the results from Figure 6 but instead aggregates the export data at the destination-division level to the destination level. The evolution over time of the distance and empire estimates remains similar to our main findings. The main difference is that the estimates of the evolution of the effects of distance over time are less precisely estimated.

Figure A9: Evolution of Distance and Empire Effects (aggregate data)

-1.5 -1 -.5

0

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Distance Estimate 95% Confidence Interval

Evolution of the effects of Distance

0

1

2

3

4

5

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Empire Estimate 95% Confidence Interval

Evolution of the effects of Empire

• Figures A10 and A11 replicate the results from Figure 6 with the inclusion of lags for the war variables. The results in Figure A10 are obtained by simply considering the lags of war based on our interval data. Given that our data was collected at ten-year intervals, we note that the minimum lag length is then ten years. Nevertheless, we consider the first and second lags of 

the war indicator. As seen in Figure A10, the coefficient estimates for distance and empire over time are very similar to our main results.

We also experiment with an alternative definition of the lag of war. Specifically, the results in Figure A11 are obtained with a lagged war variable which is defined as being equal to one if there was a war between Britain and the destination in question in any of the previous ten years. Once again, our main results remain robust in this specification.

A13

Figure A10: Evolution of Distance and Empire Effects (first & second lags of war)

-1.5 -1 -.5

0

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Distance Estimate 95% Confidence Interval

Evolution of the effects of Distance

0

1

2

3

4

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Empire Estimate 95% Confidence Interval

Evolution of the effects of Empire

Figure A11: Evolution of Distance and Empire Effects (ten-year window of war)

-1.5 -1 -.5

0

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Distance Estimate 95% Confidence Interval

Evolution of the effects of Distance

0

1

2

3

4

1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 year Empire Estimate 95% Confidence Interval

Evolution of the effects of Empire

• Finally, adding more historical variables to our specification might strengthen the analysis. However, given the long span of our trade data, collecting additional data on historical control variables over 86 destinations and 200 years is not an easy task (and perhaps, not even a feasible one). For instance, a common proxy for tariff policy is the ratio of customs revenue to the declared value of imports. In this case, the largest known collection of this measure of tariff intensity comes from the work of Jeffrey Williamson, but it comprises observations for only 23 destinations and four years in our sample (1869, 1880, 1890, and 1899). We introduced the following control variables along these lines:

1. An indicator variable for financial crises (FIN_CRISISjt) drawn from the Jorda Schularick-Taylor database (1869-1899) and from which we were able to match 56 observations in our dataset across destinations and years. Only five of these observations are equal to one.

2. An indicator variable for external default (DEFAULTjt) from the Reinhart-Rogoff database (1800-1899) and from which we were able to match 539 observations in our dataset across destinations and years. Only nine of these observations are equal to one.

3. An indicator variable for gold standard adoption (GOLD_ST RDjt) from the Meissner database (1850-1899) and from which we were able to match 474 observations in our

A14

dataset across destinations and years. While roughly one-third of the observations are equal to one, this variable is also highly correlated with the indicator variable for the British Empire. 4. The logged ratio of customs revenue-to-import values as a proxy for tariffs ln(T ARIFFjt) from the Williamson database (1869-1899) and from which we were able to match 87 observations in our dataset across destinations and years.

Overall, there are fewer than 50 observations across destination-years where there are overlapping observations across all four control variables. Nevertheless, we merged these with our data on exports by SITC division and were able to obtain the estimates reported in Table A7. The results in column (1) of A7 are obtained with our main specification (PPML with division-year fixed effects) and all new control variables. Four things stand out. First, the number of observations for the new analysis is less than 2% of our full sample. Second, we cannot obtain estimates of the effects of war and external default for the simple reason that Britain was not at war in the period from 1869 to 1899 nor were there any episodes of external default in our sample. Third, the estimates of the original variables in our model have the expected signs with three of them being statistically significant (Empire is the exception). Finally, as expected, we obtain a positive and significant estimate for gold standard adherence and a negative but statistically insignificant estimate for financial crises. However, our estimate for tariffs is positive, albeit very small in value and statistically insignificant.

The limited number of observations likely explains some of the (non)results in column (1) of Table A7. Therefore, in column (2) of this table, we only retain gold standard adherence as a control variable as this allows us to extend the analysis to a larger set of destinations and back to 1850. Accordingly, the number of observations in column (2) increases significantly, but it is still less than 25% of that of our full sample. Despite this limitation, all estimates in column (2) have the expected signs, plausible magnitudes, and statistical significance. To gauge the independent contribution of the gold standard, we use the same sample from column (2) but exclude the associated indicator to obtain the results in column (3) of Table A7. While we observe some small differences in the magnitudes of coefficient estimates between columns (2) and (3), they are not statistically different from each other.

A15

| EMP IREjt | 0.355 | | 0.796 | | | 0.931 | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | (0.280) | | (0.177)∗∗∗ | | | (0.161)∗∗∗ | | |
| ln(GDPjt) | 0.585 | | 0.645 | | | 0.623 | | |

| ln(DGECjt) | 0.394 | | 0.380 | | | 0.424 | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | (0.190)∗∗ | | (0.179)∗∗ | | | (0.188)∗∗ | | |
| W ARjt | 0.000 | | -0.545 | | | -0.408 | | |
| | (.) | | (0.295)∗ | | | (0.294) | | |
| GOLD_ST | 0.446 RDjt | | 0.407 | | | | | |

Table A7: Panel Gravity Estimates, 1700-1899 (1) (2) (3) value value value ln(DISTjt) -0.196 -0.264 -0.328 (0.074)∗∗∗ (0.094)∗∗∗ (0.083)∗∗∗ EMP IREjt 0.355 0.796 0.931 (0.280) (0.177)∗∗∗ (0.161)∗∗∗ ln(GDPjt) 0.585 0.645 0.623 (0.072)∗∗∗ (0.036)∗∗∗ (0.041)∗∗∗ (0.152)∗∗∗ (0.170)∗∗ DEFAULTjt 0.000 (.) FIN_CRISISjt -0.211 (0.208) ln(T ARIFFjt) 0.061 (0.081) N 1,506 18,723 18,723 ∗ p < .1, ∗∗ p < .05, ∗∗∗ p < .01.

| FIN_CRISISjt | -0.211 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | (0.208) | | | | | | | |
| ARIFFjt) ln(T | 0.061 | | | | | | | |
| | (0.081) | | | | | | | |
| N | 1,506 | | 18,723 | | | 18,723 | | |

A16



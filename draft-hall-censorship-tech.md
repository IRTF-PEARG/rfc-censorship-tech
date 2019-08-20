---
title: A Survey of Worldwide Censorship Techniques
abbrev: draft-hall-censorship-tech
docname: draft-hall-censorship-tech-latest
category: info

ipr: trust200902
area: General
workgroup:
keyword: Internet-Draft

stand_alone: yes
pi: [toc, sortrefs, symrefs]

author:
 -
    ins: J.L. Hall
    name: Joseph Lorenzo Hall
    organization: CDT
    email: joe@cdt.org
 -
    ins: M.D. Aaron
    name: Michael D. Aaron
    organization: CU Boulder
    email: michael.aaron@colorado.edu
 -
    ins: S. Adams
    name: Stan Adams
    organization: CDT
    email: sadams@cdt.org
 -
    ins: B. Jones
    name: Ben Jones
    organization: Princeton
    email: bj6@cs.princeton.edu
 -
    ins: N. Feamster
    name: Nick Feamster
    organization: Princeton
    email: feamster@cs.princeton.edu

normative:

informative:

  RFC0793:
  RFC7754:
  RFC7624:
  RFC6066:

  Glanville-2008:
    target: http://www.theguardian.com/commentisfree/2008/nov/17/censorship-internet
    title: The Big Business of Net Censorship
    author:
      name: Jo Glanville
      ins: J. Glanville
    date: 2008

  Verkamp-2012:
    target: https://www.usenix.org/system/files/conference/foci12/foci12-final1.pdf
    title: Inferring Mechanics of Web Censorship Around the World
    author:
    -
      name: John-Paul Verkamp
      ins: J.P. Verkamp
    -
      name: Minaxi Gupta
      ins: M. Gupta
    date: 2012

  Nabi-2013:
    target: http://0b4af6cdc2f0c5998459-c0245c5c937c5dedcca3f1764ecc9b2f.r43.cf2.rackcdn.com/12387-foci13-nabi.pdf
    title: The Anatomy of Web Censorship in Pakistan
    author:
      name: Zubair Nabi
      ins: Z. Nabi
    date: 2013

  Tang-2016:
    target: https://www.cs.tufts.edu/comp/116/archive/fall2016/ctang.pdf
    title: In-depth analysis of the Great Firewall of China
    author:
      name: Chao Tang
      ins: C. Tang
    date: 2016

  Aryan-2012:
    target: https://jhalderm.com/pub/papers/iran-foci13.pdf
    title: "Internet Censorship in Iran: A First Look"
    author:
    -
      name: Simurgh Aryan
      ins: S. Aryan
    -
      name: Homa Aryan
      ins: H. Aryan
    -
      name: J. Alex Halderman
      ins: J.A. Halderman
    date: 2012

  Husak-2016:
    target: https://link.springer.com/article/10.1186/s13635-016-0030-7
    title: HTTPS traffic analysis and client identification using passive SSL/TLS fingerprinting
    author:
    -
      name: Martin Husak
      ins: M. Husak
    -
      name: Milan Cermak
      ins: M. Cermak
    -
      name: Tomas Jirsik
      ins: T. Jirsik
    -
      name: Pavel Celeda
      ins: P. Celeda
    date: 2016

  Dalek-2013:
    target: http://www.cs.stonybrook.edu/~phillipa/papers/imc112s-dalek.pdf
    title: A Method for Identifying and Confirming the Use of URL Filtering Products for Censorship
    author:
      name: Jakub Dalek
      ins: J. Dalek
    date: 2013

  Jones-2014:
    target: http://conferences2.sigcomm.org/imc/2014/papers/p299.pdf
    title: Automated Detection and Fingerprinting of Censorship Block Pages
    author:
      name: Ben Jones
      ins: B. Jones
    date: 2014

  Crandall-2010:
    target: http://www.cs.unm.edu/~crandall/icdcs2010.pdf
    title: "Empirical Study of a National-Scale Distributed Intrusion Detection System: Backbone-Level Filtering of HTML Responses in China"
    author:
      name: Jedediah Crandall
      ins: J. Crandall
    date: 2010

  Senft-2013:
    target: https://citizenlab.org/2013/11/asia-chats-analyzing-information-controls-privacy-asian-messaging-applications/
    title: "Asia Chats: Analyzing Information Controls and Privacy in Asian Messaging Applications"
    author:
      name: Adam Senft
      ins: A. Senft
    date: 2013

  Rushe-2015:
    target: http://www.theguardian.com/technology/2014/feb/11/bing-censors-chinese-language-search-results
    title: Bing censoring Chinese language search results for users in the US
    author:
      name: Dominic Rushe
      ins: D. Rushe
    date: 2013

  Cheng-2010:
    target: http://arstechnica.com/tech-policy/2010/06/google-tweaks-china-to-hong-kong-redirect-same-results/
    title: Google stops Hong Kong auto-redirect as China plays hardball
    author:
      name: Jacqui Cheng
      ins: J. Cheng
    date: 2010

  Whittaker-2013:
    target: http://www.zdnet.com/1168-keywords-skype-uses-to-censor-monitor-its-chinese-users-7000012328/
    title: 1,168 keywords Skype uses to censor, monitor its Chinese users
    author:
      name: Zach Whittaker
      ins: Z. Whittaker
    date: 2013

  BBC-2013:
    target: http://www.bbc.com/news/uk-24980765
    title: Google and Microsoft agree steps to block abuse images
    author:
      org: BBC News
    date: 2013

  Condliffe-2013:
    target: http://gizmodo.com/google-announces-massive-new-restrictions-on-child-abus-1466539163
    title: Google Announces Massive New Restrictions on Child Abuse Search Terms
    author:
      name: Jamie Condliffe
      ins: J. Condliffe
    date: 2013

  Zhu-2011:
    target: http://arxiv.org/ftp/arxiv/papers/1107/1107.3794.pdf
    title: An Analysis of Chinese Search Engine Filtering
    author:
      name: Tao Zhu
      ins: T. Zhu
    date: 2011

  Wagner-2009:
    target: http://advocacy.globalvoicesonline.org/wp-content/uploads/2009/06/deeppacketinspectionandinternet-censorship2.pdf
    title: "Deep Packet Inspection and Internet Censorship: International Convergence on an ‘Integrated Technology of Control'"
    author:
      name: Ben Wagner
      ins: B. Wagner
    date: 2009

  Porter-2010:
    target: http://www.symantec.com/connect/articles/perils-deep-packet-inspection
    title: The Perils of Deep Packet Inspection
    author:
      name: Thomas Porter
      ins: T. Porter
    date: 2010

  Clayton-2006:
    target: http://link.springer.com/chapter/10.1007/11957454_2
    title: Ignoring the Great Firewall of China
    author:
      name: Richard Clayton
      ins: R. Clayton
    date: 2006

  Anonymous-2014:
    target: https://www.usenix.org/system/files/conference/foci14/foci14-anonymous.pdf
    title: Towards a Comprehensive Picture of the Great Firewall's DNS Censorship
    author:
      org: Anonymous
    date: 2014

  Khattak-2013:
    target: http://0b4af6cdc2f0c5998459-c0245c5c937c5dedcca3f1764ecc9b2f.r43.cf2.rackcdn.com/12389-foci13-khattak.pdf
    title: Towards Illuminating a Censorship Monitor's Model to Facilitate Evasion
    author:
      name: Sheharbano Khattak
      ins: S. Khattak
    date: 2013

  Wilde-2012:
    target: https://blog.torproject.org/blog/knock-knock-knockin-bridges-doors
    title: Knock Knock Knockin' on Bridges Doors
    author:
      name: Tim Wilde
      ins: T. Wilde
    date: 2012

  Wagstaff-2013:
    target: http://www.reuters.com/article/2013/05/04/uk-malaysia-election-online-idUKBRE94309G20130504
    title: In Malaysia, online election battles take a nasty turn
    author:
      name: Jeremy Wagstaff
      ins: J. Wagstaff
    date: 2013

  Hepting-2011:
    target: https://www.eff.org/cases/hepting
    title: Hepting vs. AT&T
    author:
      org: Electronic Frontier Foundation
    date: 2011

  Hjelmvik-2010:
    target: https://www.iis.se/docs/hjelmvik_breaking.pdf
    title: Breaking and Improving Protocol Obfuscation
    author:
      name: Erik Hjelmvik
      ins: E. Hjelmvik
    date: 2010

  Sandvine-2014:
    target: https://www.sandvine.com/downloads/general/technology/sandvine-technology-showcases/sandvine-technology-showcase-traffic-classification.pdf
    title: "Technology Showcase on Traffic Classification: Why Measurements and Freeform Policy Matter"
    author:
      org: Sandvine
    date: 2014

  Winter-2012:
    target: http://arxiv.org/pdf/1204.0447v1.pdf
    title: How China is Blocking Tor
    author:
      name: Phillip Winter
      ins: P. Winter
    date: 2012

  Anonymous-2007:
    target: https://torrentfreak.com/how-to-bypass-comcast-bittorrent-throttling-071021
    title: How to Bypass Comcast's Bittorrent Throttling
    author:
      org: Anonymous
    date: 2012

  Anonymous-2013:
    target: https://en.greatfire.org/blog/2013/jan/github-blocked-china-how-it-happened-how-get-around-it-and-where-it-will-take-us
    title: GitHub blocked in China - how it happened, how to get around it, and where it will take us
    author:
      org: Anonymous
    date: 2013

  Ensafi-2013:
    target: http://arxiv.org/pdf/1312.5739v1.pdf
    title: Detecting Intentional Packet Drops on the Internet via TCP/IP Side Channels
    author:
      name: Roya Ensafi
      ins: R. Ensafi
    date: 2013

  Weaver-2009:
    target: http://www.icir.org/vern/papers/reset-injection.ndss09.pdf
    title: Detecting Forged TCP Packets
    author:
    -
      name: Nicholas Weaver
      ins: N. Weaver
    -
      name: Robin Sommer
      ins: R. Sommer
    -
      name: Vern Paxson
      ins: V. Paxson
    date: 2009

  Netsec-2011:
    target: https://nets.ec/TCP-RST_Injection
    title: TCP-RST Injection
    author:
      org: n3t2.3c
    date: 2011

  Schoen-2007:
    target: https://www.eff.org/deeplinks/2007/10/eff-tests-agree-ap-comcast-forging-packets-to-interfere
    title: "EFF tests agree with AP: Comcast is forging packets to interfere with user traffic"
    author:
      name: Seth Schoen
      ins: S. Schoen
    date: 2007

  VonLohmann-2008:
    target: https://www.eff.org/deeplinks/2008/08/fcc-rules-against-comcast-bit-torrent-blocking
    title: FCC Rules Against Comcast for BitTorrent Blocking
    author:
      name: Fred VonLohmann
      ins: F. VonLohmann
    date: 2008

  Halley-2008:
    target: https://www.networkworld.com/article/2277316/tech-primers/tech-primers-how-dns-cache-poisoning-works.html
    title: How DNS cache poisoning works
    author:
      name: Bob Halley
      ins: B. Halley
    date: 2014

  Zmijewki-2014:
    target: http://www.renesys.com/2014/03/turkish-internet-censorship/
    title: Turkish Internet Censorship Takes a New Turn
    author:
      name: Earl Zmijewki
      ins: E. Zmijewki
    date: 2014

  AFP-2014:
    target: http://www.businessinsider.com/chinas-internet-breakdown-reportedly-caused-by-censoring-tools-2014-1
    title: China Has Massive Internet Breakdown Reportedly Caused By Their Own Censoring Tools
    author:
      org: AFP
    date: 2014

  Anon-SIGCOMM12:
    target: http://www.sigcomm.org/sites/default/files/ccr/papers/2012/July/2317307-2317311.pdf
    title: The Collateral Damage of Internet Censorship by DNS Injection
    author:
      org: Anonymous
    date: 2012

  Albert-2011:
    target: https://opennet.net/blog/2011/06/dns-tampering-and-new-icann-gtld-rules
    title: DNS Tampering and the new ICANN gTLD Rules
    author:
      name: Kendra Albert
      ins: K. Albert
    date: 2011

  Wikip-DoS:
    target: https://en.wikipedia.org/w/index.php?title=Denial-of-service_attack&amp;oldid=710558258
    title: Denial of Service Attacks
    author:
      org: Wikipedia
    date: 2016

  Schone-2014:
    target: http://www.nbcnews.com/feature/edward-snowden-interview/exclusive-snowden-docs-show-uk-spies-attacked-anonymous-hackers-n21361
    title: Snowden Docs Show UK Spies Attacked Anonymous, Hackers
    author:
    -
      name: Mark Schone
      ins: M. Schone
    -
      name: Richard Esposito
      ins: R. Esposito
    -
      name: Matthew Cole
      ins: M. Cole
    -
      name: Glenn Greenwald
      ins: G. Greenwald
    date: 2014

  CERT-2000:
    target: http://www.cert.org/historical/advisories/CA-1996-21.cfm
    title: TCP SYN Flooding and IP Spoofing Attacks
    author:
      org: CERT
    date: 2000

  Kravtsova-2012:
    target: http://www.themoscowtimes.com/news/article/cyberattacks-disrupt-oppositions-election/470119.html
    title: Cyberattacks Disrupt Opposition's Election
    author:
      name: Yekaterina Kravtsova
      ins: Y. Kravtsova
    date: 2012

  Villeneuve-2011:
    target: http://access.opennet.net/wp-content/uploads/2011/12/accesscontested-chapter-08.pdf
    title: "Open Access: Chapter 8, Control and Resistance, Attacks on Burmese Opposition Media"
    author:
      name: Nart Villeneuve
      ins: N. Villeneuve
    date: 2011

  Orion-2013:
    target: http://www.theinquirer.net/inquirer/news/2287433/zimbabwe-election-hit-by-hacking-and-ddos-attacks
    title: Zimbabwe election hit by hacking and DDoS attacks
    author:
      name: Egan Orion
      ins: E. Orion
    date: 2013

  Muncaster-2013:
    target: http://www.theregister.co.uk/2013/05/09/malaysia_fraud_elections_ddos_web_blocking/
    title: Malaysian election sparks web blocking/DDoS claims
    author:
      name: Phil Muncaster
      ins: P. Muncaster
    date: 2013

  Dobie-2007:
    target: http://news.bbc.co.uk/2/hi/asia-pacific/7016238.stm
    title: Junta tightens media screw
    author:
      name: Michael Dobie
      ins: M. Dobie
    date: 2007

  Heacock-2009:
    target: https://opennet.net/blog/2009/07/china-shuts-down-internet-xinjiang-region-after-riots
    title: China Shuts Down Internet in Xinjiang Region After Riots
    author:
      name: Rebekah Heacock
      ins: R. Heacock
    date: 2009

  Cowie-2011b:
    target: http://www.renesys.com/2011/02/libyan-disconnect-1/
    title: Libyan Disconnect
    author:
      name: Jim Cowie
      ins: J. Cowie
    date: 2011

  Cowie-2011:
    target: http://www.renesys.com/2011/01/egypt-leaves-the-internet/
    title: Egypt Leaves the Internet
    author:
      name: Jim Cowie
      ins: J. Cowie
    date: 2011

  Thomson-2012:
    target: http://www.theregister.co.uk/2012/11/29/syria_internet_blackout/
    title: Syria Cuts off Internet and Mobile Communication
    author:
      name: Iain Thomson
      ins: I. Thomson
    date: 2012

  Thomson-2012:
    target: http://www.theregister.co.uk/2012/11/29/syria_internet_blackout/
    title: Syria Cuts off Internet and Mobile Communication
    author:
      name: Iain Thomson
      ins: I. Thomson
    date: 2012

  BBC-2013b:
    target: http://www.bbc.com/news/world-asia-china-2439695
    title: China employs two million microblog monitors state media say
    author:
      org: BBC
    date: 2013

  Calamur-2013:
    target: http://www.npr.org/blogs/thetwo-way/2013/11/29/247820503/prominent-egyptian-blogger-arrested
    title: Prominent Egyptian Blogger Arrested
    author:
      name: Krishnadev Calamur
      ins: K. Calamur
    date: 2013

  AP-2012:
    target: http://www.huffingtonpost.com/2012/12/03/sattar-beheshit-iran_n_2233125.html
    title: Sattar Beheshit, Iranian Blogger, Was Beaten In Prison According To Prosecutor
    author:
      org: Associated Press
    date: 2012

  Hopkins-2011:
    target: http://readwrite.com/2011/03/03/communications_blocked_in_libya_this_week_in_onlin
    title: "Communications Blocked in Libya, Qatari Blogger Arrested: This Week in Online Tyranny"
    author:
      name: Curt Hopkins
      ins: C. Hopkins
    date: 2011

  Guardian-2014:
    target: http://www.theguardian.com/world/2014/apr/17/chinese-blogger-jailed-crackdown-internet-rumours-qin-zhihui
    title: Chinese blogger jailed under crackdown on 'internet rumours'
    author:
      org: The Gaurdian
    date: 2014

  Johnson-2010:
    target: http://seattlepostglobe.org/2010/02/05/torture-feared-in-arrest-of-iraqi-blogger/
    title: Torture feared in arrest of Iraqi blogger
    author:
      name: Larry Johnson
      ins: L. Johnson
    date: 2011

  Bristow-2013:
    target: http://news.bbc.co.uk/2/hi/asia-pacific/7783640.stm
    title: China's internet 'spin doctors‘
    author:
      name: Michael Bristow
      ins: M. Bristow
    date: 2013

  Fareed-2008:
    target: http://www.theguardian.com/media/2008/sep/22/chinathemedia.marketingandpr
    title: China joins a turf war
    author:
      name: Malik Fareed
      ins: M. Fareed
    date: 2008

  Gao-2014:
    target: http://www.nytimes.com/2014/06/04/opinion/tiananmen-forgotten.html
    title: Tiananmen, Forgotten
    author:
      name: Helen Gao
      ins: H. Gao
    date: 2014

  Anderson-2011:
    target: http://access.opennet.net/wp-content/uploads/2011/12/accessdenied-chapter-3.pdf
    title: "Access Denied: Tools and Technology of Internet Filtering"
    author:
    -
      name: Ross Anderson
      ins: R. Anderson
    -
      name: Steven J. Murdoch
      ins: S.J. Murdoch
    date: 2011

  AFNIC-2013:
    target: http://www.afnic.fr/medias/documents/conseilscientifique/SC-consequences-of-DNS-based-Internet-filtering.pdf
    title: "Report of the AFNIC Scientific Council: Consequences of DNS-based Internet filtering"
    author:
      org: AFNIC
    date: 2013

  ICANN-SSAC-2012:
    target: https://www.icann.org/en/system/files/files/sac-056-en.pdf
    title: "SAC 056: SSAC Advisory on Impacts of Content Blocking via the Domain Name System"
    author:
      org: ICANN Security and Stability Advisory Committee (SSAC)
    date: 2012

  Ding-1999:
    target: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.132.3302&amp;rep=rep1&amp;type=pdf
    title: "Centralized Content-Based Web Filtering and Blocking: How Far Can It Go?"
    author:
    -
      name: Chen Ding
      ins: C. Ding
    -
      name: Chi-Hung Chi
      ins: C.H. Chi
    -
      name: Jing Deng
      ins: J. Deng
    -
      name: Chun-Lei Dong
      ins: C.L. Dong
    date: 1999

  Trustwave-2015:
    target: https://www3.trustwave.com/software/8e6/hlp/r3000/files/1system_filter.html
    title: "Filter: SNI extension feature and HTTPS blocking"
    author:
      org: Trustwave
    date: 2015

  Sophos-2015:
    target: https://www.sophos.com/en-us/support/knowledgebase/115865.aspx
    title: Understanding Sophos Web Filtering
    author:
      org: Sophos
    date: 2015

  Shbair-2015:
    target: https://hal.inria.fr/hal-01202712/document
    title: Efficiently Bypassing SNI-based HTTPS Filtering
    author:
    -
      name: Wazen M. Shbair
      ins: W.M. Shbair
    -
      name: Thibault Cholez
      ins: T. Cholez
    -
      name: Antoine Goichot
      ins: A. Goichot
    -
      name: Isabelle Chrisment
      ins: I. Chrisment
    date: 2015

  RSF-2005:
    target: http://archives.rsf.org/print-blogs.php3?id_article=15013
    title: Technical ways to get around censorship
    author:
      org: Reporters Sans Frontieres
    date: 2005

  Marczak-2015:
    target: https://www.usenix.org/system/files/conference/foci15/foci15-paper-marczak.pdf
    title: An Analysis of China’s “Great Cannon”
    author:
    -
      name: Bill Marczak
      ins: B. Marczak
    -
      name: Nicholas Weaver
      ins: N. Weaver
    -
      name: Jakub Dalek
      ins: J. Dalek
    -
      name: Roya Ensafi
      ins: R. Ensafi
    -
      name: David Fifield
      ins: D. Fifield
    -
      name: Sarah McKune
      ins: S. McKune
    -
      name: Arn Rey
      ins: A. Rey
    -
      name: John Scott-Railton
      ins: J. Scott-Railton
    -
      name: Ron Deibert
      ins: R. Deibert
    -
      name: Vern Paxson
      ins: V. Paxson
    date: 2015

  Fifield-2015:
    target: https://petsymposium.org/2015/papers/03_Fifield.pdf
    title: Blocking-resistant communication through domain fronting
    author:
    -
      name: David Fifield
      ins: D. Fifield
    -
      name: Chang Lan
      ins: C. Lan
    -
      name: Rod Hynes
      ins: R. Hynes
    -
      name: Percy Wegmann
      ins: P. Wegmann
    -
      name: Vern Paxson
      ins: V. Paxson
    date: 2015

  Google-RTBF:
    target: https://support.google.com/legal/contact/lr_eudpa?product=websearch
    title: Search removal request under data protection law in Europe
    author:
      org: Google, Inc.
    date: 2015

  DMLP-512:
    target: http://www.dmlp.org/legal-guide/protecting-yourself-against-copyright-claims-based-user-content
    title: Protecting Yourself Against Copyright Claims Based on User Content
    author:
      org: Digital Media Law Project
    date: 2012

  Kopel-2013:
    target: http://dx.doi.org/doi:10.15779/Z384Q3M
    title: "Operation Seizing Our Sites: How the Federal Government is Taking Domain Names Without Prior Notice"
    author:
      name: Karen Kopel
      ins: K. Kopel
    date: 2013

  Bortzmayer-2015:
    target: https://labs.ripe.net/Members/stephane_bortzmeyer/dns-censorship-dns-lies-seen-by-atlas-probes
    title: "DNS Censorship (DNS Lies) As Seen By RIPE Atlas"
    author:
      name: Stephane Bortzmayer
      ins: S. Bortzmayer
    date: 2015


--- abstract

This document describes the technical mechanisms used by censorship
regimes around the world to block or impair Internet traffic. It aims
to make designers, implementers, and users of Internet protocols aware
of the properties being exploited and mechanisms used to censor
end-user access to information.  This document makes no suggestions on
individual protocol considerations, and is purely informational,
intended to be a reference.

--- middle


Introduction {#intro}
============

Censorship is where an entity in a position of power -- such as a
government, organization, or individual -- suppresses communication
that it considers objectionable, harmful, sensitive, politically
incorrect or inconvenient. (Although censors that engage in censorship
must do so through legal, military, or
other means, this document focuses largely on technical
mechanisms used to achieve network censorship.)

This document describes the technical mechanisms that censorship
regimes around the world use to block or degrade Internet traffic (see
{{RFC7754}} for a discussion of Internet blocking and filtering
in terms of implications for Internet architecture, rather than end-user access to content and services).

We describe three elements of Internet censorship: prescription,
identification, and interference. Prescription is the process by which
censors determine what types of material they should block, i.e. they
decide to block a
list of pornographic websites. Identification is the process by which
censors classify specific traffic to be blocked or impaired, i.e. the
censor blocks or impairs
all webpages containing "sex" in the title or traffic to www.sex.example.
Interference is the process
by which the censor intercedes in communication and prevents access to
censored materials by blocking access or impairing the connection.


Technical Prescription {#tech-prescrip}
=====================

Prescription is the process of figuring out what censors would like to
block {{Glanville-2008}}. Generally, censors aggregate
information "to block" in blacklists or using real-time heuristic assessment of
content {{Ding-1999}}. There are indications that online censors
are starting to use machine learning techniques as well {{Tang-2016}}.

There are typically three types of blacklists: Keyword, domain name,
or Internet Protocol (IP) address. Keyword and domain name blocking take place at the application
level (e.g. HTTP), whereas IP blocking tends to take place using
routing data in TCP/IP headers. The mechanisms for building up these
blacklists are varied. Censors can purchase from private industry
"content control" software, such as SmartFilter, which allows
filtering from broad categories that they would like to block, such as
gambling or pornography.  In these cases, these private services
attempt to categorize every semi-questionable website as to allow for
meta-tag blocking (similarly, they tune real-time content heuristic
systems to map their assessments onto categories of objectionable
content).

Countries that are more interested in
retaining specific political control, a desire which requires swift
and decisive action, often have ministries or organizations, such as
the Ministry of Industry and Information Technology in China or the
Ministry of Culture and Islamic Guidance in Iran, which maintain their
own blacklists.


Technical Identification {#tech-id}
========================


Points of Control {#poc}
-----------------

Internet censorship, necessarily, takes place over a network. Network
design gives censors a number of different points-of-control where
they can identify the content they are interested in filtering. An
important aspect of pervasive technical interception is the necessity
to rely on software or hardware to intercept the content the censor is
interested in. This requirement, the need to have the interception
mechanism located somewhere, logically or physically, implicates various
general points-of-control:

* __Internet Backbone:__ If a censor controls the gateways into a region,
  they can filter undesirable traffic that is traveling into and out
  of the region by packet sniffing and port mirroring at the relevant exchange
  points. Censorship at this point of control is most effective at
  controlling the flow of information between a region and the rest of
  the Internet, but is ineffective at identifying content traveling
  between the users within a region.

* __Internet Service Providers:__ Internet Service Providers are perhaps
  the most natural point of control. They have a benefit of being
  easily enumerable by a censor paired with the ability to identify
  the regional and international traffic of all their users. The
  censor's filtration mechanisms can be placed on an ISP via
  governmental mandates, ownership, or voluntary/coercive influence.

* __Institutions:__ Private institutions such as corporations, schools,
  and cyber cafes can put filtration mechanisms in place. These
  mechanisms are occasionally at the request of a censor, but are more
  often implemented to help achieve institutional goals, such as to
  prevent the viewing of pornography on school computers.

* __Personal Devices:__ Censors can mandate censorship software be
  installed on the device level. This has many disadvantages in terms
  of scalability, ease-of-circumvention, and operating system
  requirements. The emergence of mobile devices exacerbate these
  feasibility problems.

* __Services:__ Application service providers can be pressured, coerced,
  or legally required to censor specific content or flows of
  data. Service providers naturally face incentives to maximize their
  potential customer base and potential service shutdowns or legal
  liability due to censorship efforts may seem much less attractive
  than potentially excluding content, users, or uses of their service.

* __Certificate Authorities:__ Authorities that issue cryptographically
  secured resources can be a significant point of control. Certificate
  Authorities that issue certificates to domain holders for TLS/HTTPS
  or Regional/Local Internet Registries that issue Route Origination
  Authorizations to BGP operators can be forced to issue rogue
  certificates that may allow compromises in confidentiality
  guarantees -- allowing censorship software to engage in
  identification and interference where not possible before -- or
  integrity guarantees -- allowing, for example, adversarial routing of
  traffic.

* __Content Distribution Networks (CDNs):__ CDNs seek to collapse network
  topology in order to better locate content closer to the service's
  users in order to improve quality of service. These can be powerful
  points of control for censors, especially if the location of a CDN
  results in easier interference.

At all levels of the network hierarchy, the filtration mechanisms used
to detect undesirable traffic are essentially the same: a censor
sniffs transmitting packets and identifies undesirable content, and
then uses a blocking or shaping mechanism to prevent or impair
access.  Identification of undesirable traffic can occur at the
application, transport, or network layer of the IP stack. Censors are
almost always concerned with web traffic, so the relevant protocols
tend to be filtered in predictable ways. For example, a subversive
image would always make it past a keyword filter, but the IP address
of the site serving the image may be blacklisted when identified as a
provider of undesirable content.


Application Layer {#app-layer}
-----------------


### HTTP Request Header Identification

An HTTP header contains a lot of useful information for traffic
identification; although "host" is the only required field in an HTTP
request header (for HTTP/1.1 and later), an HTTP method field is necessary
to do anything
useful. As such, "method" and "host" are the two fields used
most often for ubiquitous censorship. A censor can sniff traffic and
identify a specific domain name (host) and usually a page name (GET
/page) as well. This identification technique is usually paired with
TCP/IP header identification (see [](#sec_tcpid)) for a more robust
method.

__Tradeoffs:__ Request Identification is a technically straight-forward
identification method that can be easily implemented at the Backbone
or ISP level. The hardware needed for this sort of identification is
cheap and easy-to-acquire, making it desirable when budget and scope
are a concern. HTTPS will encrypt the relevant request and response
fields, so pairing with TCP/IP identification (see [](#sec_tcpid)) is
necessary for filtering of HTTPS. However, some countermeasures such
as URL obfuscation {{RSF-2005}} can trivially defeat simple forms of
HTTP Request Header Identification.

__Empirical Examples:__ Studies exploring censorship mechanisms have found
evidence of HTTP header/ URL filtering in many countries, including
Bangladesh, Bahrain, China, India, Iran, Malaysia, Pakistan, Russia,
Saudi Arabia, South Korea, Thailand, and Turkey
{{Verkamp-2012}} {{Nabi-2013}} {{Aryan-2012}}. Commercial technologies
such as the McAfee SmartFilter and NetSweeper are often purchased by
censors {{Dalek-2013}}.  These commercial technologies use a
combination of HTTP Request Identification and TCP/IP Header
Identification to filter specific URLs. Dalek et al. and Jones et
al. identified the use of these products in the wild
{{Dalek-2013}} {{Jones-2014}}.


### HTTP Response Header Identification

While HTTP Request Header Identification relies on the information
contained in the HTTP request from client to server, response
identification uses information sent in response by the server to
client to identify undesirable content.

__Tradeoffs:__ As with HTTP Request Header Identification, the techniques
used to identify HTTP traffic are well-known, cheap, and relatively
easy to implement, but is made useless by HTTPS, because the response
in HTTPS is encrypted, including headers.

The response fields are also less helpful for identifying content than
request fields, as "Server" could easily be identified using HTTP
Request Header identification, and "Via" is rarely relevant.  HTTP
Response censorship mechanisms normally let the first n packets
through while the mirrored traffic is being processed; this may allow
some content through and the user may be able to detect that the
censor is actively interfering with undesirable content.

__Empirical Examples:__ In 2009, Jong Park et al. at the University of New
Mexico demonstrated that the Great Firewall of China (GFW) has used this
technique {{Crandall-2010}}. However, Jong Park et al. found that the
GFW discontinued this practice during the course of the study. Due to
the overlap in HTTP response filtering and keyword filtering (see
[](#kw-filt)), it is likely that most censors rely on keyword
filtering over TCP streams instead of HTTP response filtering.


### Instrumenting Content Providers {#kw-filt}

In addition to censorship by the state, many governments pressure
content providers to censor themselves. Due to the extensive reach of
government censorship, we need to define content provider as any
service that provides utility to users, including everything from web
sites to locally installed programs. The defining factor of keyword
identification by content providers is the choice of content providers
to detect restricted terms on their platform. The terms to look for
may be provided by the government or the content provider may be
expected to come up with their own list.

__Tradeoffs:__ By instrumenting content providers to identify restricted
content, the censor can gain new information at the cost of political
capital with the companies it forces or encourages to participate in
censorship. For example, the censor can gain insight about the content
of encrypted traffic by coercing web sites to identify restricted
content, but this may drive away potential investment. Coercing
content providers may encourage self-censorship, an additional
advantage for censors. The tradeoffs for instrumenting content
providers are highly dependent on the content provider and the
requested assistance.

__Empirical Examples:__ Researchers have discovered keyword identification
by content providers on platforms ranging from instant messaging
applications {{Senft-2013}} to search engines
{{Rushe-2015}} {{Cheng-2010}} {{Whittaker-2013}} {{BBC-2013}} {{Condliffe-2013}}. To
demonstrate the prevalence of this type of keyword identification, we
look to search engine censorship.

Search engine censorship demonstrates keyword identification by
content providers and can be regional or worldwide.  Implementation is
occasionally voluntary, but normally is based on laws and regulations
of the country a search engine is operating in. The keyword blacklists
are most likely maintained by the search engine provider. China is known to
require search engine providers to "voluntarily" maintain search term
blacklists to acquire/keep an Internet content provider (ICP) license
{{Cheng-2010}}.  It is clear these blacklists are maintained by each
search engine provider based on the slight variations in the
intercepted searches {{Zhu-2011}} {{Whittaker-2013}}. The United
Kingdom has been pushing search engines to self-censor with the threat
of litigation if they don't do it themselves: Google and Microsoft
have agreed to block more than 100,000 queries in U.K. to help combat
abuse {{BBC-2013}} {{Condliffe-2013}}.

Depending on the output, search engine keyword identification may be
difficult or easy to detect. In some cases specialized or blank
results provide a trivial enumeration mechanism, but more subtle
censorship can be difficult to detect. In February 2015, Microsoft's search
engine, Bing, was accused of censoring Chinese content outside of
China {{Rushe-2015}} because Bing returned different results for
censored terms in Chinese and English. However, it is possible that
censorship of the largest base of Chinese search users, China, biased
Bing's results so that the more popular results in China (the
uncensored results) were also more popular for Chinese speakers
outside of China.


### Deep Packet Inspection (DPI) Identification {#dpi}

Deep Packet Inspection has become computationally feasible as a
censorship mechanism in recent years {{Wagner-2009}}. Unlike other
techniques, DPI reassembles network flows to examine the application
"data" section, as opposed to only the header, and is therefore often
used for keyword identification. DPI also differs from other
identification technologies because it can leverage additional packet
and flow characteristics, i.e. packet sizes and timings, to identify
content. To prevent substantial quality of service (QoS) impacts, DPI
normally analyzes a copy of data while the original packets continue
to be routed. Typically, the traffic is split using either a mirror
switch or fiber splitter, and analyzed on a cluster of machines
running Intrusion Detection Systems (IDS) configured for censorship.

__Tradeoffs:__ DPI is one of the most expensive identification mechanisms
and can have a large QoS impact {{Porter-2010}}.  When used as a
keyword filter for TCP flows, DPI systems can cause also major
overblocking problems. Like other techniques, DPI is less useful
against encrypted data, though DPI can leverage unencrypted elements
of an encrypted data flow (e.g., the Server Name Indicator (SNI) sent
in the clear for TLS) or statistical information about an encrypted
flow (e.g., video takes more bandwidth than audio or textual forms of
communication) to identify traffic.

Other kinds of information can be inferred by comparing certain unencrypted elements
exchanged during TLS handshakes to similar data points from known sources.
This practice, called TLS fingerprinting, allows a probabilistic identification of
a party's operating system, browser, or application based on a comparison of the
specific combinations of TLS version, ciphersuites, compression options, etc.
sent in the ClientHello message to similar signatures found in unencrypted traffic {{Husak-2016}}.

Despite these problems, DPI is the most powerful identification method
and is widely used in practice. The Great Firewall of China (GFW), the
largest censorship system in the world, has used DPI to identify
restricted content over HTTP and DNS and inject TCP RSTs and bad DNS
responses, respectively, into connections
{{Crandall-2010}} {{Clayton-2006}} {{Anonymous-2014}}.

__Empirical Examples:__ Several studies have found evidence of DPI being
used to censor content and tools. Clayton et al. Crandal et al.,
Anonymous, and Khattak et al., all explored the GFW and Khattak et
al. even probed the firewall to discover implementation details like
how much state it stores
{{Crandall-2010}} {{Clayton-2006}} {{Anonymous-2014}} {{Khattak-2013}}. The
Tor project claims that China, Iran, Ethiopia, and others must have used
DPI to block the obfs2 protocol {{Wilde-2012}}.  Malaysia has
been accused of using targeted DPI, paired with DDoS, to identify and
subsequently knockout pro-opposition material {{Wagstaff-2013}}.  It
also seems likely that organizations not so worried about blocking
content in real-time could use DPI to sort and categorically search
gathered traffic using technologies such as NarusInsight
{{Hepting-2011}}.


#### Server Name Indication {#sni}

In encrypted connections using Transport Layer Security (TLS), there may be
servers that host multiple "virtual servers" at a given network
address, and the client will need to specify in the (unencrypted)
Client Hello message which domain name it seeks to connect to (so that
the server can respond with the appropriate TLS certificate) using the
Server Name Indication (SNI) TLS extension {{RFC6066}}. Since SNI is
sent in the clear, censors and filtering software can use it as a
basis for blocking, filtering, or impairment by dropping connections
to domains that match prohibited content (e.g., bad.foo.example may be
censored while good.foo.example is not) {{Shbair-2015}}.

Domain fronting has been one popular way to avoid identification by censors {{Fifield-2015}}.
To avoid identification by censors, applications using domain fronting put a different
domain name in the SNI extension than the one encrypted by HTTPS. The visible
SNI would indicate an unblocked domain, while the blocked domain remains hidden
in the encrypted application header.
Some encrypted messaging services relied on domain fronting to enable their
provision in countries employing SNI-based filtering. These services used the
cover provided by domains for which blocking at the domain level would be
undesirable to hide their true domain names. However, the companies holding the
most popular domains have since reconfigured their software to prevent this practice.
It may be possible to achieve similar results using potential future options to encrypt SNI in
TLS 1.3.

__Tradeoffs:__ Some clients do not send the SNI extension (e.g., clients
that only support versions of SSL and not TLS) or will fall back to
SSL if a TLS connection fails, rendering this method ineffective. In
addition, this technique requires deep packet inspection techniques
that can be computationally and infrastructurally expensive and
improper configuration of an SNI-based block can result in significant
overblocking, e.g., when a second-level domain like populardomain.example is
inadvertently blocked. In the case of encrypted SNI, pressure to censor may
transfer to other points of intervention, such as content and application providers.

__Empirical Examples:__ While there are many examples of security firms
that offer SNI-based filtering {{Trustwave-2015}} {{Sophos-2015}}
{{Shbair-2015}}, the government of South Korea was recently observed using SNI-based filtering. Cite to Gatlan https://www.bleepingcomputer.com/news/security/south-korea-is-censoring-the-internet-by-snooping-on-sni-traffic/


Transport Layer {#transport}
---------------

### Shallow Packet Inspection and TCP/IP Header Identification {#sec_tcpid}

Of the various shallow packet inspection methods, TCP/IP Header Identification is the most pervasive, reliable, and
predictable type of identification.  TCP/IP headers contain a few
invaluable pieces of information that must be transparent for traffic
to be successfully routed: destination and source IP address and port.
Destination and Source IP are doubly useful, as not only does it allow
a censor to block undesirable content via IP blacklisting, but also
allows a censor to identify the IP of the user making the
request. Port is useful for whitelisting certain applications.

__Trade-offs:__ TCP/IP identification is popular due to its simplicity,
availability, and robustness.

TCP/IP identification is trivial to implement, but is difficult to
implement in backbone or ISP routers at scale, and is therefore
typically implemented with DPI. Blacklisting an IP is equivalent to
installing a /32 route on a router and due to limited flow table
space, this cannot scale beyond a few thousand IPs at most. IP
blocking is also relatively crude, leading to overblocking, and cannot
deal with some services like Content Distribution Networks (CDN), that
host content at hundreds or thousands of IP addresses. Despite these
limitations, IP blocking is extremely effective because the user needs
to proxy their traffic through another destination to circumvent this
type of identification.

Port-blocking is generally not useful because many types of content
share the same port and it is possible for censored applications to
change their port. For example, most HTTP traffic goes over port 80,
so the censor cannot differentiate between restricted and allowed
content solely on the basis of port. Port whitelisting is occasionally
used, where a censor limits communication to approved ports, such as
80 for HTTP traffic and is most effective when used in conjunction with
other identification mechanisms. For example, a censor could block the
default HTTPS port, port 443, thereby forcing most users to fall back
to HTTP.

### Protocol Identification {#prot-id}

Censors sometimes identify entire protocols to be blocked using a
variety of traffic characteristics.  For example, Iran impairs the
performance of HTTPS traffic, a protocol that prevents further
analysis, to encourage users to switch to HTTP, a protocol that they
can analyze {{Aryan-2012}}. A simple protocol identification
would be to recognize all TCP traffic over port 443 as HTTPS, but more
sophisticated analysis of the statistical properties of payload data
and flow behavior, would be more effective, even when port 443 is not
used {{Hjelmvik-2010}} {{Sandvine-2014}}.

If censors can detect circumvention tools, they can block them, so
censors like China are extremely interested in identifying the
protocols for censorship circumvention tools. In recent years, this
has devolved into an arms race between censors and circumvention tool
developers. As part of this arms race, China developed an extremely
effective protocol identification technique that researchers call
active probing or active scanning.

In active probing, the censor determines whether hosts are running a
circumvention protocol by trying to initiate communication using the
circumvention protocol. If the host and the censor successfully
negotiate a connection, then the censor conclusively knows that host
is running a circumvention tool. China has used active scanning to
great effect to block Tor {{Winter-2012}}.

__Trade-offs:__ Protocol Identification necessarily only provides insight
into the way information is traveling, and not the information itself.

Protocol identification is useful for detecting and blocking
circumvention tools, like Tor, or traffic that is difficult to
analyze, like VoIP or SSL, because the censor can assume that this
traffic should be blocked. However, this can lead to over-blocking
problems when used with popular protocols.  These methods are
expensive, both computationally and financially, due to the use of
statistical analysis, and can be ineffective due to its imprecise
nature.

__Empirical Examples:__ Protocol identification can be easy to detect if
it is conducted in real time and only a particular protocol is
blocked, but some types of protocol identification, like active
scanning, are much more difficult to detect. Protocol identification
has been used by Iran to identify and throttle SSH traffic to make it
unusable {{Anonymous-2007}} and by China to identify and block Tor
relays {{Winter-2012}}. Protocol Identification has also been used for
traffic management, such as the 2007 case where Comcast in the United
States used RST injection to interrupt BitTorrent Traffic
{{Winter-2012}}.


Technical Interference {#tech-interference}
====================

Application Layer
-------------------

### DNS Interference {#dns-mangling}


There are a variety of mechanisms that censors can use to block or
filter access to content by altering responses from the DNS
{{AFNIC-2013}} {{ICANN-SSAC-2012}}, including blocking the response,
replying with an error message, or responding with an
incorrect address.

"DNS mangling" is a network-level technique where an incorrect IP
address is returned in response to a DNS query to a censored
destination. An example of this is what some Chinese networks do (we
are not aware of any other wide-scale uses of mangling). On those
Chinese networks, every DNS request in transit is examined (presumably
by network inspection technologies such as DPI) and, if it matches a
censored domain, a false response is injected. End users can see this
technique in action by simply sending DNS requests to any unused IP
address in China (see example below). If it is not a censored name,
there will be no response. If it is censored, an erroneous response
will be returned. For example, using the command-line dig utility to
query an unused IP address in China of 192.0.2.2 for the name
"www.uncensored.example"  compared with
"www.censored.example" (censored at the time of writing), we get an
erroneous IP address "198.51.100.0" as a response:

    % dig +short +nodnssec @192.0.2.2 A www.uncensored.example
    ;; connection timed out; no servers could be reached

    % dig +short +nodnssec @192.0.2.2 A www.censored.example
    198.51.100.0

There are also cases of what is colloquially called "DNS lying", where
a censor mandates that the DNS responses provided -- by an operator of
a recursive resolver such as an Internet access provider -- be
different than what authoritative resolvers would provide
{{Bortzmayer-2015}}.

DNS cache poisoning refers to a mechanism where a censor interferes
with the response sent by an authoritative DNS resolver to a recursive
resolver by responding more quickly than the authoritative resolver
can respond with an alternative IP address {{Halley-2008}}.
Cache poisoning occurs
after the requested site's name servers resolve the request and
attempt to forward the true IP back to the requesting device; on the
return route the resolved IP is recursively cached by each DNS server
that initially forwarded the request. During this caching process if
an undesirable keyword is recognized, the resolved IP is "poisoned"
and an alternative IP (or NXDOMAIN error) is returned more quickly
than the upstream resolver can respond, causing an erroneous IP
address to be cached (and potentially recursively so). The alternative
IPs usually direct to a nonsense domain or a warning page.
Alternatively, Iranian censorship appears to prevent the communication
en-route, preventing a response from ever being sent {{Aryan-2012}}.

__Trade-offs:__
These forms of DNS interference
require the censor to force a user to traverse a controlled DNS
hierarchy (or intervening network on which the censor serves as a
Active Pervasive Attacker {{RFC7624}} to rewrite DNS responses)
for the mechanism to be effective. It can be circumvented
by a technical savvy user that opts to use alternative DNS resolvers
(such as the public DNS resolvers provided by
Google, OpenDNS, Telcomix, or FDN) or Virtual Private Network technology. DNS mangling and cache poisoning
also imply returning an incorrect IP to
those attempting to resolve a domain name, but in some cases the destination
may be
technically accessible;  over HTTP, for example, the user may have another
method of obtaining the IP
address of the desired site and may be able to access it if the site
is configured to be the
default server listening at this IP address.  Target blocking has
also been a
problem, as occasionally users outside of the censors region will be
directed through DNS servers or DNS-rewriting network equipment
controlled by a censor, causing the
request to fail. The ease of circumvention paired with the large risk
of content blocking and target blocking make DNS interference a
partial, difficult, and less than ideal censorship mechanism. Additionally, the above mechanisms rely on DNSSEC not being deployed or DNSSEC validation not being active on the client or recursive resolver.

__Empirical Examples:__ DNS interference, when properly implemented, is
easy to identify based on the shortcomings identified above. Turkey
relied on DNS interference for its country-wide block of websites
such Twitter and YouTube for almost week in March of 2014 but the ease
of circumvention resulted in an increase in the popularity of Twitter
until Turkish ISPs implementing an IP blacklist to achieve the
governmental mandate {{Zmijewki-2014}}.
Ultimately, Turkish ISPs started hijacking all requests to Google and
Level 3's international DNS resolvers {{Zmijewki-2014}}. DNS
interference, when incorrectly implemented, has resulted in some
of the largest "censorship disasters".  In January 2014, China started
directing all requests passing through the Great Fire Wall to a single
domain, dongtaiwang.com, due to an improperly configured DNS
poisoning attempt; this incident is thought to be the largest
Internet-service outage in history
{{AFP-2014}} {{Anon-SIGCOMM12}}. Countries such as China, Iran, Turkey,
and the United States have discussed blocking entire TLDs as well, but
only Iran has acted by blocking all Israeli (.il) domains
{{Albert-2011}}.


Transport Layer
----------------------

### Performance Degradation


While other interference techniques outlined in this section mostly
focus on blocking or preventing access to content, it can be an
effective censorship strategy in some cases to not entirely block
access to a given destination, or service but instead degrade the
performance of the relevant network connection.  The resulting user
experience for a site or service under performance degradation can be
so bad that users opt to use a different site, service, or method of
communication, or may not engage in communication at all if there are
no alternatives.  Traffic shaping techniques that rate-limit the
bandwidth available to certain types of traffic is one example of a
performance degradation.

__Trade offs:__ While implementing a performance degradation will not
always eliminate the ability of people to access a desire resource, it
may force them to use other means of communication where censorship
(or surveillance) is more easily accomplished.

__Empirical Examples:__ Iran has been known to shape the bandwidth available to
HTTPS traffic to encourage unencrypted HTTP traffic {{Aryan-2012}}.

### Packet Dropping


Packet dropping is a simple mechanism to prevent undesirable
traffic. The censor identifies undesirable traffic and chooses to not
properly forward any packets it sees associated with the traversing
undesirable traffic instead of following a normal routing
protocol. This can be paired with any of the previously described
mechanisms so long as the censor knows the user must route traffic
through a controlled router.

__Trade offs:__ Packet Dropping is most successful when every traversing
packet has transparent information linked to undesirable content, such
as a Destination IP. One downside Packet Dropping suffers from is the
necessity of blocking all content from otherwise allowable IPs
based on a single subversive sub-domain; blogging services and github
repositories are good examples. China famously dropped all github
packets for three days based on a single repository hosting
undesirable content {{Anonymous-2013}}.  The need to inspect every
traversing packet in close to real time also makes Packet Dropping
somewhat challenging from a QoS perspective.

__Empirical Examples:__ Packet Dropping is a very common form of technical
interference and lends itself to accurate detection given the unique
nature of the time-out requests it leaves in its wake. The Great
Firewall of China has been observed using packet dropping as one of its primary
mechanisms of technical censorship {{Ensafi-2013}}. Iran has also used
Packet Dropping as the mechanisms for throttling SSH
{{Aryan-2012}}. These are but two examples of a ubiquitous censorship
practice.


### RST Packet Injection {#rst-inject}


Packet injection, generally, refers to a man-in-the-middle (MITM)
network interference technique that spoofs packets in an established
traffic stream. RST packets are normally used to let one side of TCP
connection know the other side has stopped sending information, and
thus the receiver should close the connection. RST Packet Injection is
a specific type of packet injection attack that is used to interrupt
an established stream by sending RST packets to both sides of a TCP
connection; as each receiver thinks the other has dropped the
connection, the session is terminated.

__Trade-offs:__ RST Packet Injection has a few advantages that make it
extremely popular as a censorship technique. RST Packet Injection is
an out-of-band interference mechanism, allowing the avoidance of the the
QoS bottleneck one can encounter with inline techniques such as Packet
Dropping. This out-of-band property allows a censor to inspect a copy
of the information, usually mirrored by an optical splitter, making it
an ideal pairing for DPI and Protocol Identification
{{Weaver-2009}} (this asynchronous version of a MITM is often called a
Man-on-the-Side (MOTS)).
RST Packet Injection also has the advantage of only
requiring one of the two endpoints to accept the spoofed packet for
the connection to be interrupted.

The difficult part of RST Packet
Injection is spoofing "enough" correct information to ensure one
end-point accepts a RST packet as legitimate; this generally implies a
correct IP, port, and (TCP) sequence number. Sequence number is the
hardest to get correct, as {{RFC0793}} specifies an RST Packet should
be in-sequence to be accepted, although the RFC also recommends
allowing in-window packets as "good enough". This in-window
recommendation is important, as if it is implemented it allows for
successful Blind RST Injection attacks {{Netsec-2011}}.  When
in-window sequencing is allowed, It is trivial to conduct a Blind RST
Injection, a blind injection implies the censor doesn't know any
sensitive (encrypted) sequencing information about the TCP stream they
are injecting into, they can simply enumerate the ~70000 possible
windows; this is particularly useful for interrupting
encrypted/obfuscated protocols such as SSH or Tor. RST Packet
Injection relies on a stateful network, making it useless against UDP
connections. RST Packet Injection is among the most popular censorship
techniques used today given its versatile nature and effectiveness
against all types of TCP traffic.

__Empirical Examples:__ RST Packet Injection, as mentioned above, is most
often paired with identification techniques that require splitting,
such as DPI or Protocol Identification. In 2007, Comcast was accused of
using RST Packet Injection to interrupt traffic it identified as
BitTorrent {{Schoen-2007}}, this later led to a US Federal
Communications Commission ruling against Comcast
{{VonLohmann-2008}}. China has also been known to use RST Packet
Injection for censorship purposes. This interference is especially
evident in the interruption of encrypted/obfuscated protocols, such as
those used by Tor {{Winter-2012}}.


Multi-layer and Non-layer
-------------------------


### Distributed Denial of Service (DDoS) {#ddos}


Distributed Denial of Service attacks are a common attack mechanism
used by "hacktivists" and malicious hackers, but censors have used
DDoS in the past for a variety of reasons. There is a huge variety of
DDoS attacks {{Wikip-DoS}}, but on a high level two possible impacts
tend to occur; a flood attack results in the service being unusable
while resources are being spent to flood the service, a crash attack
aims to crash the service so resources can be reallocated elsewhere
without "releasing" the service.

__Trade-offs:__ DDoS is an appealing mechanism when a censor would like to
prevent all access to undesirable content, instead of only access in
their region for a limited period of time, but this is really the only
uniquely beneficial feature for DDoS as a censorship technique. The
resources required to carry out a successful DDoS against major
targets are computationally expensive, usually requiring renting or
owning a malicious distributed platform such as a botnet, and
imprecise. DDoS is an incredibly crude censorship technique, and
appears to largely be used as a timely, easy-to-access mechanism for
blocking undesirable content for a limited period of time.

__Empirical Examples:__ In 2012 the U.K.'s GCHQ used DDoS to temporarily
shutdown IRC chat rooms frequented by members of Anonymous using the
Syn Flood DDoS method; Syn Flood exploits the handshake used by TCP to
overload the victim server with so many requests that legitimate
traffic becomes slow or impossible
{{Schone-2014}} {{CERT-2000}}. Dissenting opinion websites are
frequently victims of DDoS around politically sensitive events in
Burma {{Villeneuve-2011}}. Controlling parties in Russia
{{Kravtsova-2012}}, Zimbabwe {{Orion-2013}}, and Malaysia
{{Muncaster-2013}} have been accused of using DDoS to interrupt
opposition support and access during elections.
In 2015, China launched a DDoS attack using a true MITM system
collocated with the Great Firewall, dubbed "Great Cannon", that was
able to inject JavaScript code into web visits to a Chinese search
engine that commandeered those user agents to send DDoS traffic to
various sites {{Marczak-2015}}.


### Network Disconnection or Adversarial Route Announcement {#discon}


While it is perhaps the crudest of all censorship techniques, there is
no more effective way of making sure undesirable information isn't
allowed to propagate on the web than by shutting off the network. The
network can be logically cut off in a region when a censoring body
withdraws all of the Boarder Gateway Protocol (BGP) prefixes routing
through the censor's country.

__Trade-offs:__ The impact to a network disconnection in a region is huge
and absolute; the censor pays for absolute control over digital
information with all the benefits the Internet brings; this is never a
long-term solution for any rational censor and is normally only used
as a last resort in times of substantial unrest.

__Empirical Examples:__ Network Disconnections tend to only happen in
times of substantial unrest, largely due to the huge social,
political, and economic impact such a move has. One of the first,
highly covered occurrences was with the Junta in Myanmar employing
Network Disconnection to help Junta forces quash a rebellion in 2007
{{Dobie-2007}}. China disconnected the network in the Xinjiang region
during unrest in 2009 in an effort to prevent the protests from
spreading to other regions {{Heacock-2009}}. The Arab Spring saw the
the most frequent usage of Network Disconnection, with events in Egypt
and Libya in 2011 {{Cowie-2011}} {{Cowie-2011b}}, and Syria in 2012
{{Thomson-2012}}. Russia has indicated that it will attempt to disconnect all Russian networks from the global internet in April 2019 as part of a test of the nation's network independence. Reports also indicate that, as part of the test disconnect, Russian telecom firms must route all traffic to state-operated monitoring points. cite ZD Net https://www.zdnet.com/article/russia-to-disconnect-from-the-internet-as-part-of-a-planned-test/


Non-Technical Prescription {#nontechag}
=========================

As the name implies, sometimes manpower is the easiest way to figure
out which content to block.  Manual Filtering differs from the common
tactic of building up blacklists in that it doesn't necessarily target
a specific IP or DNS, but instead removes or flags content.  Given the
imprecise nature of automatic filtering, manually sorting through
content and flagging dissenting websites, blogs, articles and other
media for filtration can be an effective technique.  This filtration
can occur on the Backbone/ISP level -- China's army of monitors is a
good example {{BBC-2013b}} -- but more commonly manual filtering
occurs on an institutional level.  Internet Content Providers such as
Google or Weibo, require a business license to operate in China.  One
of the prerequisites for a business license is an agreement to sign a
"voluntary pledge" known as the "Public Pledge on Self-discipline for
the Chinese Internet Industry".  The failure to "energetically
uphold" the pledged values can lead to the ICPs being held liable for
the offending content by the Chinese government {{BBC-2013b}}.


Non-Technical Interference {#nontechint}
========================


Self-Censorship {#selfcensor}
---------------

Self-censorship is one of the most interesting and effective types of
censorship; a mix of Bentham's Panopticon, cultural manipulation,
intelligence gathering, and offline enforcement. Simply put, self-censorship is when a censor creates an atmosphere where users censor
themselves. This can be achieved through controlling information,
intimidating would-be dissidents, swaying public thought, and creating
apathy. Self-censorship is difficult to document, as when it is
implemented effectively the only noticeable tracing is a lack of
undesirable content; instead one must look at the tools and techniques
used by censors to encourage self-censorship. Controlling Information
relies on traditional censorship techniques, or by forcing all users
to connect through an intranet, such as in North Korea.  Intimidation
is often achieved through allowing Internet users to post "whatever
they want," but arresting those who post about dissenting views, this
technique is incredibly common
{{Calamur-2013}} {{AP-2012}} {{Hopkins-2011}} {{Guardian-2014}} {{Johnson-2010}}.
A good example of swaying public thought is China's "50-Cent Party,"
reported to be composed of somewhere between 20,000 {{Bristow-2013}} and 300,000
{{Fareed-2008}} contributors who are paid to "guide public thought" on
local and regional issues as directed by the Ministry of
Culture. Creating apathy can be a side-effect of successfully
controlling information over time and is ideal for a censorship regime
{{Gao-2014}}.


Domain Name Reallocation {#dnrealloc}
------------------------

Because domain names are resolved recursively, if a root name server reassigns or delists a
domain, all other DNS servers will be unable to properly forward and
cache the site. Domain name registration is only really a risk where
undesirable content is hosted on TLD controlled by the censoring
country, such as .cn or .ru {{Anderson-2011}} or where legal processes
in countries like the United States result in domain name seizures
and/or DNS redirection by the government {{Kopel-2013}}.


Server Takedown {#serverko}
---------------

Servers must have a physical location somewhere in the world. If
undesirable content is hosted in the censoring country the servers can
be physically seized or the hosting provider can be required to
prevent access {{Anderson-2011}}.


Notice and Takedown {#notice}
-------------------

In some countries, legal mechanisms exist where an individual can
issue a legal request to a content host that requires the host to take
down content. Examples include the voluntary systems employed by
companies like Google to comply with "Right to be Forgotten" policies
in the European Union {{Google-RTBF}} and the copyright-oriented
notice and takedown regime of the United States Digital Millennium
Copyright Act (DMCA) Section 512 {{DMLP-512}}.

Contributors {#Contributors}
============

This document benefited from discussions with Stephane Bortzmeyer,
Nick Feamster, and Martin Nilsson.

--- back

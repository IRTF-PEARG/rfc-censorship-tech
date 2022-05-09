---
title: A Survey of Worldwide Censorship Techniques
abbrev: draft-irtf-pearg-censorship
docname: draft-irtf-pearg-censorship-05
category: info

ipr: trust200902
area: General
workgroup: pearg
keyword: Internet-Draft

stand_alone: yes
pi: [toc, sortrefs, symrefs]

author:
 -
    ins: J.L. Hall
    name: Joseph Lorenzo Hall
    organization: Internet Society
    email: hall@isoc.org
 -
    ins: M.D. Aaron
    name: Michael D. Aaron
    organization: CU Boulder
    email: michael.drew.aaron@gmail.com
 -
    ins: A. Andersdotter
    name: Amelia Andersdotter
    organization:
    email: amelia.ietf@andersdotter.cc
 -
    ins: B. Jones
    name: Ben Jones
    organization: Princeton
    email: bj6@cs.princeton.edu
 -
    ins: N. Feamster
    name: Nick Feamster
    organization: U Chicago
    email: feamster@uchicago.edu
 -
    ins: M. Knodel
    name: Mallory Knodel
    organization: Center for Democracy & Technology
    email: mknodel@cdt.org


normative:

informative:

  RFC0793:
  RFC7754:
  RFC7624:
  RFC6066:
  RFC8484:
  RFC7858:
  I-D.ietf-tls-sni-encryption:
  I-D.ietf-tls-esni:
  I-D.ietf-quic-transport:

  RWB2020:
    target: https://rsf.org/en/2020-world-press-freedom-index-entering-decisive-decade-journalism-exacerbated-coronavirus
    title: "2020 World Press Freedom Index: Entering a decisive decade for journalism, exacerbated by coronavirus"
    author:
      org: Reporters Without Borders
    date: 2020

  HADOPI-2020:
    target: https://www.hadopi.fr/en/node/3668
    title: "Présentation"
    author:
      org: Haute Autorité pour la Diffusion des oeuvres et la Protection des Droits sur Internet
    date: 2020

  SSAC-109-2020:
    target: https://www.icann.org/en/system/files/files/sac-109-en.pdf
    title: "SAC109: The Implications of DNS over HTTPS and DNS over TLS"
    author:
      org: ICANN Security and Stability Advisory Committee
    date: 2020

  ICANN2012:
    target: https://www.icann.org/en/system/files/files/guidance-domain-seizures-07mar12-en.pdf
    title: "Guidance for Preparing Domain Name Orders, Seizures & Takedowns"
    author:
      org: ICANN Security and Stability Advisory Committee
    date: 2012

  Tor-2020:
    target: https://2019.www.torproject.org/docs/pluggable-transports.html.en
    title: "Tor: Pluggable Transports"
    author:
      org: The Tor Project
    date: 2020

  WP-Def-2020:
    target: https://en.wikipedia.org/w/index.php?title=Censorship&oldid=943938595
    title: "Censorship"
    author:
      org: Wikipedia contributors
    date: 2020

  EC-gambling-2012:
    target: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52012SC0345
    title: "Online gambling in the Internal Market"
    author:
      org: European Commission
    date: 2012

  EC-gambling-2019:
    target: https://ec.europa.eu/growth/content/evaluation-regulatory-tools-enforcing-online-gambling-rules-and-channelling-demand-towards-1_en
    title: "Evaluation of regulatory tools for enforcing online gambling rules and channeling demand towards controlled offers"
    author:
      org: European Commission
    date: 2019

  EC-2012:
    target: https://ec.europa.eu/information_society/newsroom/image/document/2017-4/consultation_summary_report_en_2010_42070.pdf
    title: "Summary of the results of the Public Consultation on the future of electronic commerce in the Internal Market and the implementation of the Directive on electronic commerce (2000/31/EC)"
    author:
      org: European Commission
    date: 2012

  Bentham-1791:
    target: https://www.google.com/books/edition/_/Ec4TAAAAQAAJ?hl=en
    title: "Panopticon Or the Inspection House"
    author:
      name: Jeremy Bentham
      ins: J. Bentham
    date: 1791

  Ellul-1973:
    target: https://www.penguinrandomhouse.com/books/46234/propaganda-by-jacques-ellul/
    title: "Propaganda: The Formation of Men's Attitudes"
    author:
      name: Jacques Ellul
      ins: J. Ellul
    date: 1973

  Reda-2017:
    target: https://juliareda.eu/2017/11/eu-website-blocking/
    title: "New EU law prescribes website blocking in the name of 'consumer protection'"
    author:
      name: Julia Reda
      ins: J. Reda
    date: 2017

  Knight-2005:
    target: https://www.newscientist.com/article/dn7589-iranian-net-censorship-powered-by-us-technology/
    title: "Iranian net censorship powered by US technology"
    author:
      name: Will Knight
      ins: W. Knight
    date: 2005

  SIDN2020:
    target: https://labs.ripe.net/Members/giovane_moura/detecting-and-taking-down-fraudulent-webshops-at-a-cctld
    title: "Detecting and Taking Down Fraudulent Webshops at the .nl ccTLD"
    author:
      name: Giovane Moura
      ins: G. Moura
    date: 2020

  Cimpanu-2019:
    target: https://www.zdnet.com/article/russia-to-disconnect-from-the-internet-as-part-of-a-planned-test/
    title: "Russia to disconnect from the internet as part of a planned test"
    author:
      name: Catalin Cimpanu
      ins: C. Cimpanu
    date: 2019

  Hertel-2015:
    target: https://www.sciencesetavenir.fr/high-tech/comment-les-autorites-peuvent-bloquer-un-site-internet_35828
    title: "Comment les autorités peuvent bloquer un site Internet"
    author:
      name: Olivier Hertel
      ins: O. Hertel
    date: 2015

  Eneman-2010:
    target: https://www.gu.se/forskning/publikation/?publicationId=96592
    title: "ISPs filtering of child abusive material: A critical reflection of its effectiveness"
    author:
      name: Marie Eneman
      ins: M. Eneman
    date: 2010

  Gatlan-2019:
    target: https://www.bleepingcomputer.com/news/security/south-korea-is-censoring-the-internet-by-snooping-on-sni-traffic/
    title: "South Korea is Censoring the Internet by Snooping on SNI Traffic"
    author:
      name: Sergiu Gatlan
      ins: S. Gatlan
    date: 2019

  Lomas-2019:
    target: https://techcrunch.com/2019/10/30/github-removes-tsunami-democratics-apk-after-a-takedown-order-from-spain/
    title: "Github removes Tsunami Democràtic’s APK after a takedown order from Spain"
    author:
      name: Natasha Lomas
      ins: N. Lomas
    date: 2019

  Victor-2019:
    target: https://www.nytimes.com/2019/10/09/world/asia/blizzard-hearthstone-hong-kong.html
    title: "Blizzard Sets Off Backlash for Penalizing Hearthstone Gamer in Hong Kong"
    author:
      name: Daniel Victor
      ins: D. Victor
    date: 2019

  Glanville-2008:
    target: http://www.theguardian.com/commentisfree/2008/nov/17/censorship-internet
    title: The Big Business of Net Censorship
    author:
      name: Jo Glanville
      ins: J. Glanville
    date: 2008

  EFF2017:
    target: https://www.eff.org/files/2017/08/02/domain_registry_whitepaper.pdf
    title: "Which Internet registries offer the best protection for domain owners?"
    author:
    -
      name: Jeremy Malcolm
      ins: J. Malcom
    -
      name: Mitch Stoltz
      ins: M. Stoltz
    -
      name: Gus Rossi
      ins: G. Rossi
    -
      name: Vern Paxson
      ins: V. Paxson
    date: 2017

  Tschantz-2016:
    target: https://oaklandsok.github.io/papers/tschantz2016.pdf
    title: "SoK: Towards Grounding Censorship Circumvention in Empiricism"
    author:
    -
      name: Michael Carl Tschantz
      ins: M. Tschantz
    -
      name: Sadia Afroz
      ins: S. Afroz
    -
      name: Anonymous
      ins: A. Anonymous
    -
      name: Vern Paxson
      ins: V. Paxson
    date: 2016

  Cao-2016:
    target: https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_cao.pdf
    title: "Off-Path TCP Exploits: Global Rate Limit Considered Dangerous"
    author:
    -
      name: Yue Cao
      ins: Y. Cao
    -
      name: Zhiyun Qian
      ins: Z. Qian
    -
      name: Zhongjie Wang
      ins: Z. Wang
    -
      name: Tuan Dao
      ins: T. Dao
    -
      name: Srikanth V. Krishnamurthy
      ins: S. Krishnamurthy
    -
      name: Lisa M. Marvel
      ins:  L. Marvel
    date: 2016

  Leyba-2019:
    target: https://forrest.biodesign.asu.edu/data/publications/2019-compass-chokepoints.pdf
    title: "Borders and Gateways: Measuring and Analyzing National AS Chokepoints"
    author:
    -
      name: Kirtus G. Leyba
      ins: K. Leyba
    -
      name: Benjamin Edwards
      ins: B. Edwards
    -
      name: Cynthia Freeman
      ins: C. Freeman
    -
      name: Jedidiah R. Crandall
      ins: J. Crandall
    -
      name: Stephanie Forrest
      ins: S. Forrest
    date: 2019

  Chai-2019:
    target: https://www.usenix.org/system/files/foci19-paper_chai_update.pdf
    title: "On the Importance of Encrypted-SNI (ESNI) to Censorship Circumvention"
    author:
    -
      name: Zimo Chai
      ins: Z. Chai
    -
      name: Amirhossein Ghafari
      ins: A. Ghafari
    -
      name: Amir Houmansadr
      ins: A. Houmansadr
    date: 2019

  Patil-2019:
    target: https://irtf.org/anrw/2019/anrw2019-final44-acmpaginated.pdf
    title: "What Can You Learn from an IP?"
    author:
    -
      name: Simran Patil
      ins: S. Patil
    -
      name: Nikita Borisov
      ins: N. Borisov
    date: 2019

  Wright-2013:
    target: https://policyreview.info/articles/analysis/internet-filtering-trends-liberal-democracies-french-and-german-regulatory-debates
    title: "Internet filtering trends in liberal democracies: French and German regulatory debates"
    author:
    -
      name: Joss Wright
      ins: J. Wright
    -
      name: Yana Breindl
      ins: Y. Breindl
    date: 2013

  Grover-2019:
    target: https://cis-india.org/internet-governance/blog/reliance-jio-is-using-sni-inspection-to-block-websites
    title: "Reliance Jio is using SNI inspection to block websites"
    author:
    -
      name: Gurshabad Grover
      ins: G. Grover
    -
      name: Kushagra Singh
      ins: K. Singh
    -
      name: Elonnai Hickok
      ins: E. Hickok
    date: 2019

  Singh-2019:
    target: https://arxiv.org/abs/1912.08590
    title: "How India Censors the Web"
    author:
    -
      name: Kushagra Singh
      ins: K. Singh
    -
      name: Gurshabad Grover
      ins: G. Grover
    -
      name: Varun Bansal
      ins: V. Bansal
    date: 2019

  NA-SK-2019:
    target: https://www.newamerica.org/cybersecurity-initiative/c2b/c2b-log/analysis-south-koreas-sni-monitoring/
    title: "Analysis: South Korea's New Tool for Filtering Illegal Internet Content"
    author:
    -
      name: Robert Morgus
      ins: R. Morgus
    -
      name: Justin Sherman
      ins: J. Sherman
    -
      name: Seonghyun Nam
      ins: S. Nam
    date: 2019

  CitizenLab-2018:
    target: https://citizenlab.ca/2018/03/bad-traffic-sandvines-packetlogic-devices-deploy-government-spyware-turkey-syria/
    title: "Bad Traffic: Sandvine’s PacketLogic Devices Used to Deploy Government Spyware in Turkey and Redirect Egyptian Users to Affiliate Ads?"
    author:
    -
      name: Bill Marczak
      ins: B. Marczak
    -
      name: Jakub Dalek
      ins: J. Dalek
    -
      name: Sarah McKune
      ins: S. McKune
    -
      name: Adam Senft
      ins: A. Senft
    -
      name: John Scott-Railton
      ins: J. Scott-Railton
    -
      name: Ron Deibert
      ins: R. Deibert
    date: 2018

  OONI-2019:
    target: https://ooni.org/post/2019-china-wikipedia-blocking/
    title: "China is now blocking all language editions of Wikipedia"
    author:
    -
      name: Sukhbir Singh
      ins: S. Singh
    -
      name: Arturo Filastò
      ins: A. Filastò
    -
      name: Maria Xynou
      ins: M. Xynou
    date: 2019

  OONI-2018:
    target: https://ooni.org/post/2018-iran-protests-pt2/
    title: "Iran Protests: DPI blocking of Instagram (Part 2)"
    author:
      name: Leonid Evdokimov
      ins: L. Evdokimov
    date: 2018

  Dada-2017:
    target: https://www.accessnow.org/keepiton-shutdown-tracker/
    title: "Launching STOP: the #KeepItOn internet shutdown tracker"
    author:
    -
      name: Tinuola Dada
      ins: T. Dada
    -
      name: Peter Micek
      ins: P. Micek
    date: 2017

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
    target: http://conferences.sigcomm.org/imc/2013/papers/imc112s-dalekA.pdf
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

  Boyle-1997:
    target: https://scholarship.law.duke.edu/faculty_scholarship/619/
    title: "Foucault in Cyberspace: Surveillance, Sovereignty, and Hardwired Censors"
    author:
      name: James Boyle
      ins: J. Boyle
    date: 1997

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

  Zmijewski-2014:
    target: https://blogs.oracle.com/internetintelligence/turkish-internet-censorship-takes-a-new-turn
    title: Turkish Internet Censorship Takes a New Turn
    author:
      name: Earl Zmijewski
      ins: E. Zmijewski
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

  Cowie-2011:
    target: https://archive.nanog.org/meetings/nanog51/presentations/Tuesday/LT-Cowie-Egypt%20Leaves%20The%20Internet.pdf
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

  Murdoch-2011:
    target: http://access.opennet.net/wp-content/uploads/2011/12/accessdenied-chapter-3.pdf
    title: "Access Denied: Tools and Technology of Internet Filtering"
    author:
    -
      name: Steven J. Murdoch
      ins: S.J. Murdoch
    -
      name: Ross Anderson
      ins: R. Anderson
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

  Bortzmeyer-2015:
    target: https://labs.ripe.net/Members/stephane_bortzmeyer/dns-censorship-dns-lies-seen-by-atlas-probes
    title: "DNS Censorship (DNS Lies) As Seen By RIPE Atlas"
    author:
      name: Stephane Bortzmeyer
      ins: S. Bortzmeyer
    date: 2015

  Wang-2017:
    target: https://www.cs.ucr.edu/~zhiyunq/pub/imc17_censorship_tcp.pdf
    title: "Your State is Not Mine: A Closer Look at Evading Stateful Internet Censorship"
    author:
    -
      name: Zhongjie Wang
      ins: Z. Wang
    - 
      name: Yue Cao
      ins: Y. Cao
    -
      name: Zhiyun Qian
      ins: Z. Qian
    - 
      name: Chengyu Song
      ins: C. Song
    - 
      name: Srikanth V. Krishnamurthy
      ins: S. Krishnamurthy
    date: 2017

  Wang-2020:
    target: https://www.cs.ucr.edu/~zhiyunq/pub/ndss20_symtcp.pdf
    title: "SYMTCP: Eluding Stateful Deep Packet Inspection with Automated Discrepancy Discovery"
    author:
    -
      name: Zhongjie Wang
      ins: Z. Wang
    - 
      name: Shitong Zhu
      ins: S. Zhu
    - 
      name: Yue Cao
      ins: Y. Cao
    -
      name: Zhiyun Qian
      ins: Z. Qian
    - 
      name: Chengyu Song
      ins: C. Song
    - 
      name: Srikanth V. Krishnamurthy
      ins: S. Krishnamurthy
    - 
      name: Kevin S. Chan
      ins: K. Chan
    - 
      name: Tracy D. Braun
      ins: T. Braun
    date: 2020

  Li-2017:
    target: https://david.choffnes.com/pubs/liberate-imc17.pdf
    title: "lib•erate, (n) : A library for exposing (traffic-classification) rules and avoiding them efficiently"
    author:
    -
      name: Fangfan Li
      ins: F. Li
    - 
      name: Abbas Razaghpanah
      ins: A. Razaghpanah
    -
      name: Arash Molavi Kakhki
      ins: A. Kakhki
    - 
      name: Arian Akhavan Niaki 
      ins: A. Niaki
    - 
      name: David Choffnes
      ins: D. Choffnes
    - 
      name: Phillipa Gill
      ins: P. Gill
    - 
      name: Alan Mislove
      ins: A. Mislove
    date: 2017

  Bock-2019:
    target: https://geneva.cs.umd.edu/papers/geneva_ccs19.pdf
    title: "Geneva: Evolving Censorship Evasion Strategies"
    author:
    -
      name: Kevin Bock
      ins: K. Bock
    - 
      name: George Hughey
      ins: G. Hughey
    - 
      name: Xiao Qiang
      ins: X. Qiang
    - 
      name: Dave Levin
      ins: D. Levin
    date: 2019

  Bock-2020:
    target: https://geneva.cs.umd.edu/papers/evading-censorship-in-depth.pdf
    title: "Detecting and Evading Censorship-in-Depth: A Case Study of Iran’s Protocol Filter"
    author:
    -
      name: Kevin Bock
      ins: K. Bock
    - 
      name: Yair Fax
      ins: Y. Fax
    -
      name: Kyle Reese
      ins: K. Reese
    - 
      name: Jasraj Singh
      ins: J. Singh
    - 
      name: Dave Levin
      ins: D. Levin
    date: 2020
 
  Bock-2020b:
    target: https://geneva.cs.umd.edu/posts/china-censors-esni/esni/
    title: "Exposing and Circumventing China's Censorship of ESNI"
    author:
    -
      name: Kevin Bock
      ins: K. Bock
    - 
      name: iyouport
      ins: iyouport
    -
      name: Anonymous
      ins: Anonymous
    - 
      name: Louis-Henri Merino
      ins: L. Merino
    - 
      name: David Fifield
      ins: D. Fifield
    - 
      name: Amir Houmansadr
      ins: A. Houmansadr
    -
      name: Dave Levin
      ins: D. Levin
    date: 2020

  Rambert-2021:
    target: https://www.andrew.cmu.edu/user/nicolasc/publications/Rambert-WWW21.pdf
    title: "Chinese Wall or Swiss Cheese? Keyword filtering in the Great Firewall of China"
    author:
    -
      name: Raymond Rampert
      ins: R. Rampert
    - 
      name: Zachary Weinberg
      ins: Z. Weinberg
    -
      name: Diogo Barradas
      ins: D. Barradas
    - 
      name: Nicolas Christin
      ins: N. Christin
    date: 2021

  Knockel-2021:
    target: https://dl.acm.org/doi/10.1145/3473604.3474560
    title: "Measuring QQMail's automated email censorship in China"
    author:
    -
      name: Jeffery Knockel
      ins: J. Knockel
    - 
      name: Lotus Ruan
      ins: L. Ruan
    date: 2021

  Bock-2021:
    target: https://geneva.cs.umd.edu/papers/woot21-weaponizing-availability.pdf
    title: "Your Censor is My Censor: Weaponizing Censorship Infrastructure for Availability Attacks"
    author:
    -
      name: Kevin Bock
      ins: K. Bock
    - 
      name: Pranav Bharadwaj
      ins: P. Bharadwaj
    -
      name: Jasraj Singh
      ins: J. Singh
    - 
      name: Dave Levin
      ins: D. Levin
    date: 2021

  Bock-2021b:
    target: https://geneva.cs.umd.edu/papers/foci21.pdf
    title: "Even Censors Have a Backup: Examining China’s Double HTTPS Censorship Middleboxes"
    author:
    -
      name: Kevin Bock
      ins: K. Bock
    - 
      name: Gabriel Naval
      ins: G. Naval
    -
      name: Kyle Reese
      ins: K. Reese
    - 
      name: Dave Levin
      ins: D. Levin
    date: 2021

  Satija-2021:
    target: https://sambhav.info/files/blindtls-foci21.pdf
    title: "BlindTLS: Circumventing TLS-based HTTPS censorship"
    author:
    -
      name: Sambhav Satija
      ins: S. Satija
    - 
      name: Rahul Chatterjee
      ins: R. Chatterjee
    date: 2021

  Elmenhorst-2021:
    target: https://dl.acm.org/doi/pdf/10.1145/3487552.3487836
    title: "Web Censorship Measurements of HTTP/3 over QUIC"
    author:
    -
      name: Kathrin Elmenhorst
      ins: K. Elmenhorst
    - 
      name: Bertram Schuetz
      ins: B. Schuetz
    - 
      name: Simone Basso
      ins: S. Basso
    -
      name: Nils Aschenbruck
      ins: N. Aschenbruck
    date: 2021

  Elmenhorst-2022:
    target: https://www.opentech.fund/news/a-quick-look-at-quic/
    title: "A Quick Look at QUIC Censorship"
    author:
    -
      name: Kathrin Elmenhorst
      ins: K. Elmenhorst
    date: 2022

  Gilad:
    target: https://doi.org/10.1145/2597173
    title: "Off-Path TCP Injection Attacks"
    author:
    -
      name: Yossi Gilad
      ins: Y. Gilad
    -
      name: Amir Herzberg
      ins: A. Herzberg
    date: 2014

  MANRS:
    target: https://www.manrs.org/2022/03/lesson-learned-twitter-shored-up-its-routing-security/
    title: "Lesson Learned: Twitter Shored Up Its Routing Security"
    author:
    -
      name: Aftab Siddiqui
      ins: A. Siddiqui
    date: 2022

  Google-2018:
    target: https://status.cloud.google.com/incident/cloud-networking/18018
    title: "Google Cloud Networking Incident #18018"
    author:
    -
      name:
      ins:
    date: 2018

--- abstract

This document describes technical mechanisms employed in network censorship that regimes around
the world use for blocking or impairing Internet traffic. It aims
to make designers, implementers, and users of Internet protocols aware
of the properties exploited and mechanisms used for censoring
end-user access to information.  This document makes no suggestions on
individual protocol considerations, and is purely informational,
intended as a reference.

--- middle


Introduction {#intro}
============

Censorship is where an entity in a position of power -- such as a
government, organization, or individual -- suppresses communication
that it considers objectionable, harmful, sensitive, politically
incorrect or inconvenient {{WP-Def-2020}}. Although censors that engage in censorship
must do so through legal, military, or
other means, this document focuses largely on technical
mechanisms used to achieve network censorship.

This document describes technical mechanisms that censorship regimes
around the world use for blocking or impairing Internet traffic.  See
{{RFC7754}} for a discussion of Internet blocking and filtering in
terms of implications for Internet architecture, rather than end-user
access to content and services. There is also a growing field of
academic study of censorship circumvention (see the review article of
{{Tschantz-2016}}), results from which we seek to make relevant here
for protocol designers and implementers.

Terminology {#terms}
===========

We describe three elements of Internet censorship: prescription,
identification, and interference. The document contains three major
sections, each corresponding to one of these elements. Prescription is
the process by which censors determine what types of material they
should censor, e.g., classifying pornographic websites as undesirable.
Identification is the process by which censors classify specific
traffic or traffic identifiers to be blocked or impaired, e.g.,
deciding that webpages containing "sex" in an HTTP Header or that
accept traffic through the URL wwww.sex.example are likely to be
undesirable.  Interference is the process by which censors intercede
in communication and prevents access to censored materials by blocking
access or impairing the connection, e.g., implementing a technical
solution capable of identifying HTTP headers or URLs and ensuring they
are rendered wholly or partially inaccessible.


Technical Prescription {#tech-prescrip}
=====================

Prescription is the process of figuring out what censors would like to
block {{Glanville-2008}}. Generally, censors aggregate information "to
block" in blocklists or use real-time heuristic assessment of content
{{Ding-1999}}. Some national networks are designed to more naturally
serve as points of control {{Leyba-2019}}. There are also indications
that online censors use probabilistic machine learning techniques
{{Tang-2016}}. Indeed, web crawling and machine learning techniques
are an active research idea in the effort to identify content deemed
as morally or commercially harmful to companies or consumers in some
jurisdictions {{SIDN2020}}.

There are typically a few types of blocklist elements: Keyword, domain
name, protocol, or Internet Protocol (IP) address. Keyword and domain name
blocking take place at the application level, e.g., HTTP; protocol blocking
often occurs using Deep Packet Inspection to identify a forbidden protocol;
IP blocking tends to take place using IP addresses in IPv4/IPv6 headers.
Some censors also use the presence of certain keywords to enable more
aggressive blocklists {{Rambert-2021}} or to be more permissive with
content {{Knockel-2021}}. 

The mechanisms for building up these blocklists vary. Censors can purchase
from private industry "content control" software, such as SmartFilter,
which lets censors filter traffic from broad categories they would like to
block, such as gambling or pornography {{Knight-2005}}. In these cases,
these private services attempt to categorize every semi-questionable
website as to allow for meta-tag blocking. Similarly, they tune real-time
content heuristic systems to map their assessments onto categories of
objectionable content.

Countries that are more interested in retaining specific political control
typically have ministries or organizations that maintain blocklists. Examples
include the Ministry of Industry and Information Technology in China, Ministry of
Culture and Islamic Guidance in Iran, and specific to copyright in France {{HADOPI-2020}}
and across the EU for consumer protection law {{Reda-2017}}.


Technical Identification {#tech-id}
========================


Points of Control {#poc}
-----------------

Internet censorship takes place in all parts of the network
topology. It may be implemented in the network itself (e.g. local loop
or backhaul), on the services side of communication (e.g. web hosts,
cloud providers or content delivery networks), in the ancillary
services eco-system (e.g. domain name system or certificate
authorities) or on the end-client side (e.g. in an end-user device
such as a smartphone, laptop or desktop or software executed on such
devices).  An important aspect of pervasive technical interception is
the necessity to rely on software or hardware to intercept the content
the censor is interested in. There are various logical and physical
points-of-control censors may use for interception mechanisms,
including, though not limited to, the following.

* Internet Backbone: If a censor controls the gateways into a region,
  they can filter undesirable traffic that is traveling into and out
  of the region by packet sniffing and port mirroring at the relevant
  exchange points. Censorship at this point of control is most
  effective at controlling the flow of information between a region
  and the rest of the Internet, but is ineffective at identifying
  content traveling between the users within a region. Some national
  network designs naturally serve as more effective chokepoints and
  points of control {{Leyba-2019}}.

* Internet Service Providers: Internet Service Providers are
  frequently exploited points of control. They
  have the benefit of being easily enumerable by a censor -- often
  falling under the jurisdictional or operational control of a censor
  in an indisputable way -- with the additional feature that an ISP
  can identify the regional and international traffic
  of all their users. The censor's filtration mechanisms can be placed
  on an ISP via governmental mandates, ownership, or voluntary/coercive influence.

* Institutions: Private institutions such as corporations,
  schools, and Internet cafes can use filtration mechanisms.
  These mechanisms are occasionally at the request of a
  government censor, but can also be implemented to help achieve
  institutional goals, such as fostering a particular moral outlook on
  life by school-children, independent of broader society or
  government goals.

* Content Distribution Networks (CDNs): CDNs seek to collapse network
  topology in order to better locate content closer to the service's
  users. This reduces content transmission latency and improves quality
  of service. The CDN service's content
  servers, located "close" to the user in a network-sense, can be
  powerful points of control for censors, especially if the location
  of CDN content repositories allow for easier interference.

* Certificate Authorities (CAs) for Public-Key Infrastructures (PKIs):
  Authorities that issue cryptographically secured resources can be a
  significant point of control. CAs that issue certificates to domain
  holders for TLS/HTTPS (the Web PKI) or Regional/Local Internet
  Registries (RIRs) that issue Route Origination Authorizations (ROAs)
  to BGP operators can be forced to issue rogue certificates that may
  allow compromise, i.e., by allowing censorship software to engage in
  identification and interference where not possible before. CAs may
  also be forced to revoke certificates. This may lead to adversarial
  traffic routing or TLS interception being allowed, or an otherwise
  rightful origin or destination point of traffic flows being unable
  to communicate in a secure way.

* Services: Application service providers can be pressured,
  coerced, or legally required to censor specific content or data flows.
  Service providers naturally face incentives to maximize their
  potential customer base and potential service shutdowns or legal
  liability due to censorship efforts may seem much less attractive
  than potentially excluding content, users, or uses of their
  service. Services have increasingly become focal points of
  censorship discussions, as well as the focus of discussions of moral
  imperatives to use censorship tools.
  
* Content sites: On the service side of communications lie many platforms that
  publish user-generated content require terms of service compliance with all content
  and user accounts in order to avoid intermediary liability for the web hosts.
  In aggregate these policies, actions and remedies are known as content moderation.
  Content moderation happens above the services or application layer, but
  these mechanisms are built to filter, sort and block content and users
  thus making them available to censors through direct pressure on the private entity.

* Personal Devices: Censors can mandate censorship software be
  installed on the device level. This has many disadvantages in terms
  of scalability, ease-of-circumvention, and operating system
  requirements. (Of course, if a personal device is treated with
  censorship software before sale and this software is difficult to
  reconfigure, this may work in favor of those seeking to control
  information, say for children, students, customers, or employees.)
  The emergence of mobile devices exacerbate these feasibility
  problems. This software can also be mandated by institutional actors
  acting on non-governmentally mandated moral imperatives.

At all levels of the network hierarchy, the filtration mechanisms used
to censor undesirable traffic are essentially the same: a censor
either directly identifies undesirable content using the identifiers
described below and then uses a blocking or shaping mechanism such as
the ones exemplified below to prevent or impair access, or requests
that an actor ancillary to the censor, such as a private entity,
perform these functions.  Identification of undesirable traffic can
occur at the application, transport, or network layer of the IP
stack. Censors often focus on web traffic, so the relevant protocols
tend to be filtered in predictable ways (see {{http-req}} and
{{http-resp}}). For example, a subversive image might make it past a
keyword filter. However, if later the image is deemed undesirable, a
censor may then blacklist the provider site's IP address.


Application Layer {#app-layer}
-----------------

The following subsections describe properties and tradeoffs of common
ways in which censors filter using application-layer information. Each
subsection includes empirical examples describing these common
behaviors for further reference.

### HTTP Request Header Identification {#http-req}

An HTTP header contains a lot of useful information for traffic
identification. Although "host" is the only required field in an HTTP
request header (for HTTP/1.1 and later), an HTTP method field is necessary
to do anything
useful. As such, "method" and "host" are the two fields used
most often for ubiquitous censorship. A censor can sniff traffic and
identify a specific domain name (host) and usually a page name (GET
/page) as well. This identification technique is usually paired with
transport header identification (see {{sec_thid}}) for a more robust
method.

Tradeoffs: Request Identification is a technically straight-forward
identification method that can be easily implemented at the Backbone
or ISP level. The hardware needed for this sort of identification is
cheap and easy-to-acquire, making it desirable when budget and scope
are a concern. HTTPS will encrypt the relevant request and response
fields, so pairing with transport identification (see {{sec_thid}}) is
necessary for HTTPS filtering. However, some countermeasures can
trivially defeat simple forms of HTTP Request Header Identification.
For example, two cooperating endpoints -- an instrumented web server
and client -- could encrypt or otherwise obfuscate the "host" header in
a request, potentially thwarting techniques that match against "host" header values.

Empirical Examples: Studies exploring censorship mechanisms have found
evidence of HTTP header/ URL filtering in many countries, including
Bangladesh, Bahrain, China, India, Iran, Malaysia, Pakistan, Russia,
Saudi Arabia, South Korea, Thailand, and Turkey
{{Verkamp-2012}} {{Nabi-2013}} {{Aryan-2012}}. Commercial technologies
such as the McAfee SmartFilter and NetSweeper are often purchased by
censors {{Dalek-2013}}.  These commercial technologies use a
combination of HTTP Request Identification and Transport Header
Identification to filter specific URLs. Dalek et al. and Jones et
al. identified the use of these products in the wild
{{Dalek-2013}} {{Jones-2014}}.


### HTTP Response Header Identification  {#http-resp}

While HTTP Request Header Identification relies on the information
contained in the HTTP request from client to server, response
identification uses information sent in response by the server to
client to identify undesirable content.

Tradeoffs: As with HTTP Request Header Identification, the techniques
used to identify HTTP traffic are well-known, cheap, and relatively
easy to implement. However, they are made useless by HTTPS because
HTTPS encrypts the response and its headers.

The response fields are also less helpful for identifying content than
request fields, as "Server" could easily be identified using HTTP
Request Header identification, and "Via" is rarely relevant.  HTTP
Response censorship mechanisms normally let the first n packets
through while the mirrored traffic is being processed; this may allow
some content through and the user may be able to detect that the
censor is actively interfering with undesirable content.

Empirical Examples: In 2009, Jong Park et al. at the University of New
Mexico demonstrated that the Great Firewall of China (GFW) has used this
technique {{Crandall-2010}}. However, Jong Park et al. found that the
GFW discontinued this practice during the course of the study. Due to
the overlap in HTTP response filtering and keyword filtering (see
[](#kw-filt)), it is likely that most censors rely on keyword
filtering over TCP streams instead of HTTP response filtering.


### Transport Layer Security (TLS) {#tls}

Similar to HTTP, censors have deployed a variety of techniques towards
censoring Transport Layer Security (TLS) (and by extension HTTPS). Most of
these techniques relate to the Server Name Indication (SNI) field,
including censoring SNI, Encrypted SNI, or omitted SNI. Censors can also
censor HTTPS content via server certificates. 
Note that TLS 1.3 acts as a security component of QUIC.


#### Server Name Indication (SNI) {#sni}

In encrypted connections using TLS, there
may be servers that host multiple "virtual servers" at a given network
address, and the client will need to specify in the
Client Hello message which domain name it seeks to connect to (so that
the server can respond with the appropriate TLS certificate) using the
Server Name Indication (SNI) TLS extension {{RFC6066}}. 
The Client Hello message is unencrypted for TCP-based TLS. 
When using QUIC, the Client Hello message is encrypted but its 
confidentiality is not effectively protected because the initial encryption 
keys are derived using a value that is visible on the wire. Since SNI is
often sent in the clear (as are the cert fields sent in response),
censors and filtering software can use it (and response cert fields)
as a basis for blocking, filtering, or impairment by dropping
connections to domains that match prohibited content (e.g.,
bad.foo.example may be censored while good.foo.example is not)
{{Shbair-2015}}. There are undergoing standardization efforts in the
TLS Working Group to encrypt SNI {{I-D.ietf-tls-sni-encryption}}
{{I-D.ietf-tls-esni}} and recent research shows promising results in
the use of encrypted SNI in the face of SNI-based filtering
{{Chai-2019}} in some countries.

Domain fronting has been one popular way to avoid identification by
censors {{Fifield-2015}}. To avoid identification by censors,
applications using domain fronting put a different domain name in the
SNI extension than in the Host: header, which is protected by
HTTPS. The visible SNI would indicate an unblocked domain, while the
blocked domain remains hidden in the encrypted application header.
Some encrypted messaging services relied on domain fronting to enable
their provision in countries employing SNI-based filtering. These
services used the cover provided by domains for which blocking at the
domain level would be undesirable to hide their true domain
names. However, the companies holding the most popular domains have
since reconfigured their software to prevent this practice.  It may be
possible to achieve similar results using potential future options to
encrypt SNI.

Tradeoffs: Some clients do not send the SNI extension (e.g., clients
that only support versions of SSL and not TLS), rendering this method
ineffective (see {{omitsni}}). In addition, this technique requires deep packet
inspection techniques that can be computationally and
infrastructurally expensive, especially when applied to QUIC where deep packet inspection requires key extraction and decryption of the Client Hello in order to read the SNI. Improper configuration of an SNI-based
block can result in significant overblocking, e.g., when a
second-level domain like populardomain.example is inadvertently
blocked. In the case of encrypted SNI, pressure to censor may
transfer to other points of intervention, such as content and application providers.

Empirical Examples: There are many examples of security firms that
offer SNI-based filtering products {{Trustwave-2015}} {{Sophos-2015}}
{{Shbair-2015}}, and the governments of China, Egypt, Iran, Qatar,
South Korea, Turkey, Turkmenistan, and the UAE all do widespread SNI
filtering or blocking {{OONI-2018}} {{OONI-2019}} {{NA-SK-2019}}
{{CitizenLab-2018}} {{Gatlan-2019}} {{Chai-2019}} {{Grover-2019}}
{{Singh-2019}}. SNI blocking against QUIC traffic has been first observed in Russia in March 2022 {{Elmenhorst-2022}}.


#### Encrypted SNI (ESNI) {#esni}

With the data leakage present with the SNI field, a natural response is to 
encrypt it, which is forthcoming in TLS 1.3 with Encrypted Client Hello
(ECH).  Prior to ECH, the Encrypted SNI (ESNI) extension is available to
prevent the data leakage caused by SNI, which encrypts only the SNI field.
Unfortunately, censors can target connections that use the ESNI extension
specifically for censorship. This guarantees overblocking for the censor,
but can be worth the cost if ESNI is not yet widely deployed within the
country.  Encrypted Client Hello (ECH) is the emerging standard for protecting
the entire TLS Client Hello, but it is not yet widely deployed. 

Tradeoffs: The cost to censoring Encrypted SNI (ESNI) is significantly
higher than SNI to a censor, as the censor can no longer target
censorship to specific domains and guarantees over-blocking. In these
cases, the censor uses the over-blocking to discourage the use of
ESNI entirely.

Empirical Examples: In 2020, China began censoring all uses of Encrypted
ESNI (ESNI) {{Bock-2020b}}, even for innocuous connections. The
censorship mechanism for China's ESNI censorship differs from how
China censors SNI-based connections, suggesting that new middleboxes
were deployed specifically to target ESNI connections. 


#### Omitted-SNI {#omitsni}

Researchers have observed that some clients omit the SNI extension
entirely. This omitted-SNI approach limits the information available
to a censor. Like with ESNI, censors can choose to block connections that
omit the SNI, though this too risks over-blocking. 

Tradeoffs: The approach of censoring all connections that omit the SNI field
is guaranteed to over-block, though connections that omit the SNI field
should be relatively rare in the wild. 

Empirical Examples: In the past, researchers have observed censors in Russia
blocking connections that omit the SNI field {{Bock-2020b}}.


#### Server Response Certificate

During the TLS handshake after the TLS Client Hello, the server will respond
with the TLS certificate. This certificate also contains the domain
the client is trying to access, creating another avenue that censors
can use to perform censorship. This technique will not work in TLS 1.3, as the 
certificate will be encrypted.

Tradeoffs: Censoring based on the server certificate requires deep
packet inspection techniques that can be more computationally
expensive compared to other methods. Additionally, the certificate is
sent later in the TLS Handshake compared to the SNI field, forcing
the censor to track the connection for longer.

Empirical Examples: Researchers have observed the Reliance Jio
ISP in India using certificate response fields to censor connections
{{Satija-2021}}.


### Instrumenting Content Distributors {#kw-filt}

Many governments pressure content providers to censor themselves, or
provide the legal framework within which content distributors are
incentivized to follow the content restriction preferences of agents
external to the content distributor {{Boyle-1997}}. Due to the
extensive reach of such censorship, we define content
distributor as any service that provides utility to users, including
everything from web sites to locally installed programs. A commonly
used method of instrumenting content distributors consists of keyword
identification to detect restricted terms on their platform. Governments
may provide the terms on such keyword lists. Alternatively, the content
provider may be expected to come up with their own list. A different
method of instrumenting content distributors consists of requiring a
distributor to disassociate with some categories of users. See also
{{notice}}.

Tradeoffs: By instrumenting content distributors to identify
restricted content or content providers, the censor can gain new
information at the cost of political capital with the companies it
forces or encourages to participate in censorship. For example, the
censor can gain insight about the content of encrypted traffic by
coercing web sites to identify restricted content. Coercing content
distributors to regulate users, categories of users, content and
content providers may encourage users and content providers to exhibit
self-censorship, an additional advantage for censors (see {{selfcensor}}). The tradeoffs
for instrumenting content distributors are highly dependent on the
content provider and the requested assistance. A typical concern is
that the targeted keywords or categories of users are too broad, risk
being too broadly applied, or are not subjected to a sufficiently
robust legal process prior to their mandatory application (see p. 8 of
{{EC-2012}}).

Empirical Examples: Researchers discovered keyword identification
by content providers on platforms ranging from instant messaging
applications {{Senft-2013}} to search engines {{Rushe-2015}}
{{Cheng-2010}} {{Whittaker-2013}} {{BBC-2013}} {{Condliffe-2013}}. To
demonstrate the prevalence of this type of keyword identification, we
look to search engine censorship.

Search engine censorship demonstrates keyword identification by
content providers and can be regional or worldwide.  Implementation is
occasionally voluntary, but normally it is based on laws and regulations
of the country a search engine is operating in. The keyword blocklists
are most likely maintained by the search engine provider. China is
known to require search engine providers to "voluntarily" maintain
search term blocklists to acquire and keep an Internet content provider
(ICP) license {{Cheng-2010}}.  It is clear these blocklists are
maintained by each search engine provider based on the slight
variations in the intercepted searches {{Zhu-2011}}
{{Whittaker-2013}}. The United Kingdom has been pushing search engines
to self-censor with the threat of litigation if they do not do it
themselves: Google and Microsoft have agreed to block more than
100,000 queries in U.K. to help combat abuse {{BBC-2013}}
{{Condliffe-2013}}.  European Union law, as well as US law, requires
modification of search engine results in response to either copyright,
trademark, data protection or defamation concerns {{EC-2012}}.

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

Disassociation by content distributors from certain categories of
users has happened for instance in Spain, as a result of the conflict
between the Catalunyan independence movement and the Spanish legal
presumption of a unitary state {{Lomas-2019}}. E-sport event
organizers have also disassociated themselves from top players who
expressed political opinions in relation to the 2019 Hong Kong
protests {{Victor-2019}}. See also {{discon}}.

### Deep Packet Inspection (DPI) Identification {#dpi}

DPI (deep packet inspection) technically is any kind of packet
analysis beyond IP address and port number and has become
computationally feasible as a component of censorship mechanisms
in recent years {{Wagner-2009}}. Unlike other
techniques, DPI reassembles network flows to examine the application
"data" section, as opposed to only headers, and is therefore often
used for keyword identification. DPI also differs from other
identification technologies because it can leverage additional packet
and flow characteristics, e.g., packet sizes and timings, when identifying
content. To prevent substantial quality of service (QoS) impacts, DPI
normally analyzes a copy of data while the original packets continue
to be routed. Typically, the traffic is split using either a mirror
switch or fiber splitter, and analyzed on a cluster of machines
running Intrusion Detection Systems (IDS) configured for censorship.

Tradeoffs: DPI is one of the most expensive identification mechanisms
and can have a large QoS impact {{Porter-2010}}.  When used as a
keyword filter for TCP flows, DPI systems can cause also major
overblocking problems. Like other techniques, DPI is less useful
against encrypted data, though DPI can leverage unencrypted elements
of an encrypted data flow, e.g., the Server Name Indication (SNI) sent
in the clear for TLS, or metadata about an encrypted flow, e.g., packet
sizes, which differ across video and textual flows, to identify traffic.
See {{sni}} for more information about SNI-based filtration mechanisms.

Other kinds of information can be inferred by comparing certain unencrypted elements
exchanged during TLS handshakes to similar data points from known sources.
This practice, called TLS fingerprinting, allows a probabilistic identification of
a party's operating system, browser, or application based on a comparison of the
specific combinations of TLS version, ciphersuites, compression options, etc.
sent in the ClientHello message to similar signatures found in unencrypted traffic {{Husak-2016}}.

Despite these problems, DPI is the most powerful identification method
and is widely used in practice. The Great Firewall of China (GFW), the
largest censorship system in the world, uses DPI to identify
restricted content over HTTP and DNS and inject TCP RSTs and bad DNS
responses, respectively, into connections {{Crandall-2010}} {{Clayton-2006}} {{Anonymous-2014}}.

Empirical Examples: Several studies have found evidence of censors
using DPI for censoring content and tools. Clayton et al., Crandal et al.,
Anonymous, and Khattak et al., all explored the GFW {{Crandall-2010}}
{{Clayton-2006}} {{Anonymous-2014}}. Khattak et al. even probed the
firewall to discover implementation details like how much state it stores {{Khattak-2013}}.
The Tor project claims that China, Iran, Ethiopia, and others must have used
DPI to block the obfs2 protocol {{Wilde-2012}}.  Malaysia has
been accused of using targeted DPI, paired with DDoS, to identify and
subsequently attack pro-opposition material {{Wagstaff-2013}}.  It
also seems likely that organizations not so worried about blocking
content in real-time could use DPI to sort and categorically search
gathered traffic using technologies such as NarusInsight
{{Hepting-2011}}.


Transport Layer {#transport}
---------------

### Shallow Packet Inspection and Transport Header Identification {#sec_thid}

Of the various shallow packet inspection methods, Transport Header
Identification is the most pervasive, reliable, and predictable type
of identification.  Transport headers contain a few invaluable pieces
of information that must be transparent for traffic to be successfully
routed: destination and source IP address and port.  Destination and
Source IP are doubly useful, as not only does it allow a censor to
block undesirable content via IP blocklisting, but also allows a
censor to identify the IP of the user making the request and the IP
address of the destination being visited, which in most cases can be
used to infer the domain being visited {{Patil-2019}}. Port is useful
for allowlisting certain applications.

Combining IP address, port and protocol information found in the transport header, shallow packet inspection can be used by a censor to identify specific TCP or UDP endpoints. UDP endpoint blocking has been observed in the context of QUIC blocking {{Elmenhorst-2021}}.

Trade-offs: header identification is popular due to its simplicity,
availability, and robustness.

Header identification is trivial to implement, but is difficult to
implement in backbone or ISP routers at scale, and is therefore
typically implemented with DPI. Blocklisting an IP is equivalent to
installing a specific route on a router (such as a /32 route for IPv4
addresses and a /128 route for IPv6 addresses). However, due to
limited flow table space, this cannot scale beyond a few thousand IPs
at most. IP blocking is also relatively crude. It often leads to
overblocking and cannot deal with some services like Content
Distribution Networks (CDN) that host content at hundreds or thousands
of IP addresses. Despite these limitations, IP blocking is extremely
effective because the user needs to proxy their traffic through
another destination to circumvent this type of identification. 
In addition, IP blocking is effective against all protocols above IP, e.g. 
TCP and QUIC.

Port-blocking is generally not useful because many types of content
share the same port and it is possible for censored applications to
change their port. For example, most HTTP traffic goes over port 80,
so the censor cannot differentiate between restricted and allowed web
content solely on the basis of port. HTTPS goes over port 443, with
similar consequences for the censor except only partial metadata may
now be available to the censor. Port allowlisting is occasionally
used, where a censor limits communication to approved ports, such as
80 for HTTP traffic and is most effective when used in conjunction
with other identification mechanisms. For example, a censor could
block the default HTTPS port, port 443, thereby forcing most users to
fall back to HTTP. A counter-example is that port 25 (SMTP) has long
been blocked on residential ISPs' networks to reduce the risk for
email spam, but in doing so also prohibits residential ISP customers
from running their own email servers.

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

Trade-offs: Protocol identification necessarily only provides insight
into the way information is traveling, and not the information itself.

Protocol identification is useful for detecting and blocking
circumvention tools, like Tor, or traffic that is difficult to
analyze, like VoIP or SSL, because the censor can assume that this
traffic should be blocked. However, this can lead to over-blocking
problems when used with popular protocols.  These methods are
expensive, both computationally and financially, due to the use of
statistical analysis, and can be ineffective due to their imprecise
nature. Moreover, censorship circumvention groups like the Tor Project
have developed "pluggable transports" which seek to make the traffic
of censorship circumvention tools appear indistinguishable from other
kinds of traffic {{Tor-2020}}.

Censors have also used protocol identification in the past in an
'allowlist' filtering capacity, such as by only allowing specific,
pre-vetted protocols to be used and blocking any unrecognized
protocols {{Bock-2020}}. These protocol filtering approaches can also lead to
over-blocking if the allowed lists of protocols is too small or
incomplete, but can be cheap to implement, as many standard 'allowed' 
protocols are simple to identify (such as HTTP).

Empirical Examples: Protocol identification can be easy to detect if
it is conducted in real time and only a particular protocol is
blocked, but some types of protocol identification, like active
scanning, are much more difficult to detect. Protocol identification
has been used by Iran to identify and throttle SSH traffic to make it
unusable {{Anonymous-2007}} and by China to identify and block Tor
relays {{Winter-2012}}. Protocol identification has also been used for
traffic management, such as the 2007 case where Comcast in the United
States used RST injection to interrupt BitTorrent Traffic
{{Winter-2012}}. In 2020, Iran deployed an allowlist protocol filter,
which only allowed three protocols to be used (DNS, TLS, and HTTP) on
specific ports and censored any connection it could not identify {{Bock-2020}}. 
In 2022, Russia seemed to have used protocol identification to block most
HTTP/3 connections {{Elmenhorst-2022}}.


## Residual Censorship {#residualcensorship}

Another feature of some modern censorship systems is residual censorship, a
punitive form of censorship whereby after a censor disrupts a forbidden
connection, the censor continues to target subsequent connections, even if they
are innocuous {{Bock-2021}}. Residual censorship can take many forms
and often relies on the methods of technical interference described in the next
section. 

An important facet of residual censorship is precisely what the censor
continues to block after censorship is initially triggered. There are three
common options available to an adversary: 2-tuple (client IP, server IP),
3-tuple (client IP, server IP+port), or 4-tuple (client IP+port, server
IP+port). Future connections that match the tuple of information the censor
records will be disrupted {{Bock-2021}}.

Residual censorship can sometimes be difficult to identify and can often complicate
censorship measurement.

Trade-offs: The impact of residual censorship is to provide users with further
discouragement from trying to access forbidden content, though it is not
clear how successful it is at accomplishing this.

Empirical Examples: China has used 3-tuple residual censorship in conjunction
with their HTTP censorship for years and researchers have reported seeing similar
residual censorship for HTTPS. China seems to use a mix of 3-tuple and 4-tuple
residual censorship for their censorship of HTTPS with ESNI. Some censors that
perform censorship via packet dropping often accidentally implement 4-tuple
residual censorship, including Iran and Kazakhstan {{Bock-2021}}.


Technical Interference {#tech-interference}
====================

Application Layer
-------------------

### DNS Interference {#dns-mangling}


There are a variety of mechanisms that censors can use to block or
filter access to content by altering responses from the DNS
{{AFNIC-2013}} {{ICANN-SSAC-2012}}, including blocking the response,
replying with an error message, or responding with an incorrect
address. Note that there are now encrypted transports for DNS queries
in DNS-over-HTTPS {{RFC8484}} and DNS-over-TLS {{RFC7858}} that can
mitigate interference with DNS queries between the stub and the
resolver.

Responding to a DNS query with an incorrect address can be achieved
with on-path interception, off-path cache poisoning, and lying by
the nameserver.

"DNS mangling" is a network-level technique of on-path interception where an incorrect IP
address is returned in response to a DNS query to a censored
destination. An example of this is what some Chinese networks do (we
are not aware of any other wide-scale uses of mangling). On those
Chinese networks, every DNS request in transit is examined (presumably
by network inspection technologies such as DPI) and, if it matches a
censored domain, a false response is injected. End users can see this
technique in action by simply sending DNS requests to any unused IP
address in China (see example below). If it is not a censored name,
there will be no response. If it is censored, a forged response
will be returned. For example, using the command-line dig utility to
query an unused IP address in China of 192.0.2.2 for the name
"www.uncensored.example"  compared with
"www.censored.example" (censored at the time of writing), we get a
forged IP address "198.51.100.0" as a response:

    % dig +short +nodnssec @192.0.2.2 A www.uncensored.example
    ;; connection timed out; no servers could be reached

    % dig +short +nodnssec @192.0.2.2 A www.censored.example
    198.51.100.0

DNS cache poisoning happens off-path and refers to a mechanism where a censor interferes
with the response sent by an authoritative DNS name server to a recursive
resolver by responding more quickly than the authoritative name server
can respond with an alternative IP address {{Halley-2008}}.
Cache poisoning occurs
after the requested site's name servers resolve the request and
attempt to forward the true IP back to the requesting device; on the
return route the resolved IP is recursively cached by each DNS server
that initially forwarded the request. During this caching process if
an undesirable keyword is recognized, the resolved IP is "poisoned"
and an alternative IP (or NXDOMAIN error) is returned more quickly
than the upstream resolver can respond, causing a forged IP
address to be cached (and potentially recursively so). The alternative
IPs usually direct to a nonsense domain or a warning page.
Alternatively, Iranian censorship appears to prevent the communication
en-route, preventing a response from ever being sent {{Aryan-2012}}.

There are also cases of what is colloquially called "DNS lying", where
a censor mandates that the DNS responses provided -- by an operator of
a recursive resolver such as an Internet access provider -- be
different than what authoritative name server would provide
{{Bortzmeyer-2015}}.

Trade-offs: These forms of DNS interference require the censor to
force a user to traverse a controlled DNS hierarchy (or intervening
network on which the censor serves as a Active Pervasive Attacker
{{RFC7624}} to rewrite DNS responses) for the mechanism to be
effective. It can be circumvented by using alternative DNS resolvers
(such as any of the public DNS resolvers) that may fall outside of the
jurisdictional control of the censor, or Virtual Private Network (VPN)
technology. DNS mangling and cache poisoning also imply returning an
incorrect IP to those attempting to resolve a domain name, but in some
cases the destination may be technically accessible; over HTTP, for
example, the user may have another method of obtaining the IP address
of the desired site and may be able to access it if the site is
configured to be the default server listening at this IP address.
Target blocking has also been a problem, as occasionally users outside
of the censors region will be directed through DNS servers or
DNS-rewriting network equipment controlled by a censor, causing the
request to fail. The ease of circumvention paired with the large risk
of content blocking and target blocking make DNS interference a
partial, difficult, and less than ideal censorship
mechanism.

Additionally, the above mechanisms rely on DNSSEC not being deployed
or DNSSEC validation not being active on the client or recursive
resolver (neither of which are hard to imagine given limited
deployment of DNSSEC and limited client support for DNSSEC
validation). Note that an adversary seeking to merely block resolution
can serve a DNSSEC record that doesn't validate correctly, assuming of
course that the client/recursive resolver validates.

Previously, techniques were used for e.g. censorship that relied on
DNS requests being passed in cleartext over port 53
{{SSAC-109-2020}}. With the deployment of encrypted DNS (e.g.,
DNS-over-HTTPS {{RFC8484}}) these requests are now increasingly passed
on port 443 with other HTTPS traffic, or in the case of DNS-over-TLS
{{RFC7858}} no longer passed in the clear (see also {{sec_thid}}).

Empirical Examples: DNS interference, when properly implemented, is
easy to identify based on the shortcomings identified above. Turkey
relied on DNS interference for its country-wide block of websites such
Twitter and YouTube for almost week in March of 2014 but the ease of
circumvention resulted in an increase in the popularity of Twitter
until Turkish ISPs implementing an IP blocklist to achieve the
governmental mandate {{Zmijewski-2014}}.  Ultimately, Turkish ISPs
started hijacking all requests to Google and Level 3's international
DNS resolvers {{Zmijewski-2014}}. DNS interference, when incorrectly
implemented, has resulted in some of the largest "censorship
disasters".  In January 2014, China started directing all requests
passing through the Great Fire Wall to a single domain,
dongtaiwang.com, due to an improperly configured DNS poisoning
attempt; this incident is thought to be the largest Internet-service
outage in history {{AFP-2014}} {{Anon-SIGCOMM12}}. Countries such as
China, Iran, Turkey, and the United States have discussed blocking
entire TLDs as well, but only Iran has acted by blocking all Israeli
(.il) domains {{Albert-2011}}. DNS-blocking is commonly deployed in
European countries to deal with undesirable content, such as child
abuse content (Norway, United Kingdom, Belgium, Denmark, Finland,
France, Germany, Ireland, Italy, Malta, the Netherlands, Poland, Spain
and Sweden {{Wright-2013}} {{Eneman-2010}}), online gambling (Belgium,
Bulgaria, Czech Republic, Cyprus, Denmark, Estonia, France, Greece,
Hungary, Italy, Latvia, Lithuania, Poland, Portugal, Romania,
Slovakia, Slovenia, Spain (see Section 6.3.2 of: {{EC-gambling-2012}},
{{EC-gambling-2019}})), copyright infringement (all European Economic Area countries),
hate-speech and extremism (France {{Hertel-2015}}) and terrorism
content (France {{Hertel-2015}}).


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

Trade offs: While implementing a performance degradation will not
always eliminate the ability of people to access a desire resource, it
may force them to use other means of communication where censorship
(or surveillance) is more easily accomplished.

Empirical Examples: Iran has been known to shape the bandwidth available to
HTTPS traffic to encourage unencrypted HTTP traffic {{Aryan-2012}}.

### Packet Dropping


Packet dropping is a simple mechanism to prevent undesirable
traffic. The censor identifies undesirable traffic and chooses to not
properly forward any packets it sees associated with the traversing
undesirable traffic instead of following a normal routing
protocol. This can be paired with any of the previously described
mechanisms so long as the censor knows the user must route traffic
through a controlled router.

Trade offs: Packet Dropping is most successful when every traversing
packet has transparent information linked to undesirable content, such
as a Destination IP. One downside Packet Dropping suffers from is the
necessity of blocking all content from otherwise allowable IPs
based on a single subversive sub-domain; blogging services and github
repositories are good examples. China famously dropped all github
packets for three days based on a single repository hosting
undesirable content {{Anonymous-2013}}.  The need to inspect every
traversing packet in close to real time also makes Packet Dropping
somewhat challenging from a QoS perspective.

Empirical Examples: Packet Dropping is a very common form of technical
interference and lends itself to accurate detection given the unique
nature of the time-out requests it leaves in its wake. The Great
Firewall of China has been observed using packet dropping as one of its primary
mechanisms of technical censorship {{Ensafi-2013}}. Iran has also used
Packet Dropping as the mechanisms for throttling SSH
{{Aryan-2012}}. These are but two examples of a ubiquitous censorship
practice. Notably, packet dropping during the handshake or working connection is the only interference technique observed for QUIC traffic so far, e.g. in India, Iran, Russia and Uganda {{Elmenhorst-2021}}{{Elmenhorst-2022}}.


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

QUIC is not vulnerable to these types of injection attacks once the
connection has been setup. While QUIC implements a stateless reset mechanism, 
such a reset is only accepted by a peer if the packet ends in a previously 
issued stateless reset token which is hard to guess. 
During the handshake, QUIC only provides effective protection
against off-path attackers but is vulnerable to injection attacks by
attackers that have parsed prior packets.
(See {{I-D.ietf-quic-transport}} for more details.)

Trade-offs: Although ineffective against non-TCP protocols (QUIC, IPSec), RST Packet Injection has a few advantages that make it
extremely popular as a technique employed for censorship. RST Packet Injection is
an out-of-band interference mechanism, allowing the avoidance of the the
QoS bottleneck one can encounter with inline techniques such as Packet
Dropping. This out-of-band property allows a censor to inspect a copy
of the information, usually mirrored by an optical splitter, making it
an ideal pairing for DPI and protocol identification
{{Weaver-2009}} (this asynchronous version of a MITM is often called a
Man-on-the-Side (MOTS)).
RST Packet Injection also has the advantage of only
requiring one of the two endpoints to accept the spoofed packet for
the connection to be interrupted.

The difficult part of RST Packet Injection is spoofing "enough"
correct information to ensure one end-point accepts a RST packet as
legitimate; this generally implies a correct IP, port, and TCP
sequence number. Sequence number is the hardest to get correct, as
{{RFC0793}} specifies an RST Packet should be in-sequence to be
accepted, although the RFC also recommends allowing in-window packets
as "good enough". This in-window recommendation is important, as if it
is implemented it allows for successful Blind RST Injection attacks
{{Netsec-2011}}.  When in-window sequencing is allowed, it is trivial
to conduct a Blind RST Injection: while the term "blind" injection
implies the censor
doesn't know any sensitive sequencing information about
the TCP stream they are injecting into, they can simply enumerate all
~70000 possible windows; this is particularly useful for interrupting
encrypted/obfuscated protocols such as SSH or Tor {{Gilad}}.
Some censorship evasion systems work by trying to confuse the censor
into tracking incorrect information, rendering their RST Packet Injection
useless {{Khattak-2013}}, {{Wang-2017}}, {{Li-2017}}, {{Bock-2019}},
{{Wang-2020}}.

RST Packet Injection relies on a stateful network, making it useless against UDP
connections. RST Packet Injection is among the most popular censorship
techniques used today given its versatile nature and effectiveness
against all types of TCP traffic. Recent research shows that a TCP RST
packet injection attack can even work in the case of an off-path
attacker {{Cao-2016}}.

Empirical Examples: RST Packet Injection, as mentioned above, is most
often paired with identification techniques that require splitting,
such as DPI or protocol identification. In 2007, Comcast was accused of
using RST Packet Injection to interrupt traffic it identified as
BitTorrent {{Schoen-2007}}, this later led to a US Federal
Communications Commission ruling against Comcast
{{VonLohmann-2008}}. China has also been known to use RST Packet
Injection for censorship purposes. This interference is especially
evident in the interruption of encrypted/obfuscated protocols, such as
those used by Tor {{Winter-2012}}.


Routing Layer
----------------------


### Network Disconnection {#discon}


While it is perhaps the crudest of all techniques employed for censorship, there is
no more effective way of making sure undesirable information isn't
allowed to propagate on the web than by shutting off the network. The
network can be logically cut off in a region when a censoring body
withdraws all of the Boarder Gateway Protocol (BGP) prefixes routing
through the censor's country.

Trade-offs: The impact to a network disconnection in a region is huge
and absolute; the censor pays for absolute control over digital
information by losing all the benefits the Internet brings; this
rarely a long-term solution for any censor and is normally only used
as a last resort in times of substantial unrest.

Empirical Examples: Network Disconnections tend to only happen in
times of substantial unrest, largely due to the huge social,
political, and economic impact such a move has. One of the first,
highly covered occurrences was with the Junta in Myanmar employing
Network Disconnection to help Junta forces quash a rebellion in 2007
{{Dobie-2007}}. China disconnected the network in the Xinjiang region
during unrest in 2009 in an effort to prevent the protests from
spreading to other regions {{Heacock-2009}}. The Arab Spring saw the
the most frequent usage of Network Disconnection, with events in Egypt
and Libya in 2011 {{Cowie-2011}}, and Syria in 2012
{{Thomson-2012}}. Russia indicated that it would attempt to
disconnect all Russian networks from the global internet in April 2019
as part of a test of the nation's network independence. Reports also
indicate that, as part of the test disconnect, Russian telecommunications firms
must now route all traffic to state-operated monitoring points
{{Cimpanu-2019}}. India was the country that saw the largest number of
internet shutdowns per year in 2016 and 2017 {{Dada-2017}}.


### Adversarial Route Announcement {#advroute}


More fine-grained and potentially wide-spread censorship can be achieved with BGP hijacking, which adversarially re-routes BGP IP prefixes incorrectly within a region and beyond. This restricts and effectively censors the correctly known location of information that flows into or out of a jurisdiction and will similarly prevent people from outside your jurisdiction from viewing content generated outside your jurisdiction as the adversarial route announcement propagates. The first can be achieved by an adversarial BGP announcement of incorrect routes that are not intended to leak beyond a jurisdiction, where the latter attacks traffic by deliberately introducing bogus BGP announcements that reach the global internet.

Trade-offs: A global leak of a misrouted website can overwhelm an ISP if the website gets a lot of traffic. It is not a permanent solution because incorrect BGP routes that leak globally can be fixed, though within a jurisdiction only the ISP/IXP is in a position to correct them for local users. 

Empirical examples: In 2008 Pakistan Telecom censored Youtube at the request of the Pakistan government by changing its BGP routes for the website. The new routes were announced to the ISP's upstream providers and beyond. The entire Internet began directing Youtube routes to Pakistan Telecom and continued doing so for many hours. In 2018 nearly all Google services and Google cloud customers like Spotify all lost more than one hour of service after it lost control of several million of its IP addresses. Those IP prefixes were being misdirected to China Telecom, a Chinese government-owned ISP {{Google-2018}}}, in a manner similar to the BGP hijacking of US government and military websites by China Telecom in 2010. ISPs in both Russia (2022) and Myanmar (2021) have tried to hijack the same Twitter prefix more than once {{MANRS}}.


Multi-layer and Non-layer
-------------------------


### Distributed Denial of Service (DDoS) {#ddos}


Distributed Denial of Service attacks are a common attack mechanism
used by "hacktivists" and malicious hackers, but censors have used
DDoS in the past for a variety of reasons. There is a huge variety of
DDoS attacks {{Wikip-DoS}}, but at a high level two possible impacts
tend to occur; a flood attack results in the service being unusable
while resources are being spent to flood the service, a crash attack
aims to crash the service so resources can be reallocated elsewhere
without "releasing" the service.

Trade-offs: DDoS is an appealing mechanism when a censor would like to
prevent all access to undesirable content, instead of only access in
their region for a limited period of time, but this is really the only
uniquely beneficial feature for DDoS as a technique employed for censorship. The
resources required to carry out a successful DDoS against major
targets are computationally expensive, usually requiring renting or
owning a malicious distributed platform such as a botnet, and
imprecise. DDoS is an incredibly crude censorship technique, and
appears to largely be used as a timely, easy-to-access mechanism for
blocking undesirable content for a limited period of time.

Empirical Examples: In 2012 the U.K.'s GCHQ used DDoS to temporarily
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


### Censorship in Depth

Often, censors implement multiple techniques in tandem, creating
"censorship in depth". Censorship in depth can take many forms; some
censors block the same content through multiple techniques (such as
blocking a domain by DNS, IP blocking, and HTTP simultaneously), some deploy
parallel systems to improve censorship reliability (such as deploying
multiple different censorship systems to block the same domain), and others 
can use complimentary systems to limit evasion (such as by blocking
unwanted protocols entirely, forcing users to use other filtered protocols).

Trade-offs: Censorship in depth can be attractive for censors to deploy,
as it offers additional guarantees about censorship: even if someone evades 
one type of censorship, they may still be blocked by another. The main
drawback to this approach is the cost to initial deployment, as it requires
the system to deploy multiple censorship systems in tandem.

Empirical Examples: Censorship in depth is present in many large censoring
nation states today. Researchers have observed China has deployed
significant censorship in depth, often censoring the same resource across
multiple protocols {{Chai-2019}}, {{Bock-2020b}} or deploying additional
censorship systems to censor the same content and protocol {{Bock-2021b}}. 
Iran also has deployed a complimentary protocol filter to limit which
protocols can be used on certain ports, forcing users to rely on protocols
their censorship system can filter {{Bock-2020}}.


Non-Technical Interference {#nontechint}
========================


Manual Filtering {#manualfiltering}
----------------

As the name implies, sometimes manpower is the easiest way to figure
out which content to block.  Manual Filtering differs from the common
tactic of building up blocklists in that it doesn't necessarily target
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

Self-Censorship {#selfcensor}
---------------

Self-censorship is difficult to document, as it manifests primarily
through a lack of undesirable content. Tools which encourage
self-censorship are those which may lead a prospective speaker to
believe that speaking increases the risk of unfavourable outcomes for
the speaker (technical monitoring, identification requirements,
etc.). Reporters Without Borders exemplify methods of imposing
self-censorship in their annual World Press Freedom Index reports
{{RWB2020}}.

Server Takedown {#serverko}
---------------

As mentioned in passing by {{Murdoch-2011}}, servers must have a
physical location somewhere in the world. If undesirable content is
hosted in the censoring country the servers can be physically seized
or -- in cases where a server is virtualized in a cloud infrastructure
where it may not necessarily have a fixed physical location -- the
hosting provider can be required to prevent access.


Notice and Takedown {#notice}
-------------------

In many countries, legal mechanisms exist where an individual or other
content provider can issue a legal request to a content host that
requires the host to take down content. Examples include the systems
employed by companies like Google to comply with "Right to be
Forgotten" policies in the European Union {{Google-RTBF}},
intermediary liability rules for electronic platform providers
{{EC-2012}}, or the copyright-oriented notice and takedown regime of
the United States Digital Millennium Copyright Act (DMCA) Section 512
{{DMLP-512}}.

Domain-Name Seizures {#dns-seizures}
--------------------

Domain names are catalogued in so-called name-servers operated by
legal entities called registries. These registries can be made to cede
control over a domain name to someone other than the entity which
registered the domain name through a legal procedure grounded in either
private contracts or public law. Domain name seizures is increasingly
used by both public authorities and private entities to deal with
undesired content dissemination {{ICANN2012}} {{EFF2017}}.

Contributors {#Contributors}
============

This document benefited from discussions with and input from
David Belson, Stephane Bortzmeyer, Vinicius Fortuna,
Gurshabad Grover, Andrew McConachie, Martin Nilsson, Michael
Richardson, Patrick Vacek and Chris Wood.

--- back

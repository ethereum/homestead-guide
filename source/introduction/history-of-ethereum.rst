********************************************************************************
History of Ethereum
********************************************************************************

For a recent historical account, see `Taylor Gerring's blogpost <https://blog.ethereum.org/2016/02/09/cut-and-try-building-a-dream/>`_

Inception
================================================================================
Ethereum was initially described by Vitalik Buterin in late 2013 as a result of his research and work in the Bitcoin community. Shortly thereafter, Vitalik published the `Ethereum white paper <http://vbuterin.com/ethereum.html>`_, where he describes in detail the technical design and rationale for the Ethereum protocol and smart contracts architecture. In January 2014, Ethereum was formally announced by Vitalik at the The North American Bitcoin Conference in Miami, Florida, USA.

Around that time, Vitalik also started working with Dr. Gavin Wood and together co-founded Ethereum. By April 2014, Gavin published the `Ethereum Yellow Paper <https://github.com/ethereum/yellowpaper>`_ that would serve as the technical specification for the Ethereum Virtual Machine (EVM). By following the detailed specification in the Yellow Paper, the Ethereum client has been implemented in seven programming languages (C++, Go, Python, Java, JavaScript, Haskell, Rust), and has resulted in better software overall.

* `Ethereum launches Cryptocurrency 2.0 network <http://www.coindesk.com/ethererum-launches-cryptocurrency-2-0-network/>`_ - Coindesk article of 2014 Jan on the beginnings
* `Ethereum announcement on bitcointalk <https://bitcointalk.org/index.php?topic=428589.0>`_ Vitalik's original announcement to the bitcoin community. Forum thread with 5000 replies.

The Ethereum Foundation and the ether presale
================================================================================
In addition to developing the software for Ethereum, the ability to launch a new cryptocurrency and blockchain requires a massive bootstrapping effort in order to assemble the resources needed to get it up and running. To kickstart a large network of developers, miners, investors, and other stakeholders, Ethereum announced its plan to conduct a presale of ether tokens, the currency unit of Ethereum. The legal and financial complexities of raising funds through a presale led to the creation of several legal entities, including the :ref:`Ethereum Foundation (Stiftung Ethereum) <foundation>` established June 2014 in Zug, Switzerland.

Beginning in July 2014, Ethereum distributed the initial allocation of ether via a 42-day public ether presale, netting 31,591 bitcoins, worth $18,439,086 at that time, in exchange for about 60,102,216 ether. The results of the sale were initially used to pay back mounting legal debts and also for the months of developer effort that had yet to be compensated, and to finance the ongoing development of the Ethereum.

* `Launching the ether sale <https://blog.ethereum.org/2014/07/22/launching-the-ether-sale/>`_ - original official announcement on the Ethereum blog
* `Concise information-rich stats page about the presale <http://ether.fund/market>`_ by (since then inactive) `Ether.Fund <http://ether.fund/>`_
* `Overview: Ethereum’s initial public sale <https://medium.com/@slacknation/overview-ethereum-s-initial-public-sale-563c05e95501>`_ - Blogpost by slacknation - all stats about the ether presale
* `Terms and Conditions of the Presale <https://www.ethereum.org/pdfs/TermsAndConditionsOfTheEthereumGenesisSale.pdf>`_


ETH/DEV and Ethereum development
================================================================================
Following the successful ether presale, Ethereum development was formalized under a non-for-profit organization called ETH DEV, which manages the development of Ethereum under contract from Ethereum Suisse – with Vitalik Buterin, Gavin Wood, and Jeffrey Wilcke as the 3 directors of the organization. Developer interest in Ethereum grew steadily throughout 2014 and the ETH DEV team delivered a series of proof-of-concept (PoC) releases for the development community to evaluate. Frequent posts by ETH DEV team on the  `the Ethereum blog <https://blog.ethereum.org>`_ also kept the excitement and momentum around Ethereum going. Increasing traffic and growing user-base on both the Ethereum forum and the ethereum subreddit testified that the platform is attracting a fast-growing and devoted developer community. This trend has been continuing to this very day.

DEVCON-0
--------------------------------------------------------------------------------
In November 2014, ETH DEV organized the `DEVCON-0 event <https://blog.ethereum.org/2014/12/05/d%CE%BEvcon-0-recap/>`_, which brought together Ethereum developers from around the world to Berlin to meet and discuss a diverse range of Ethereum technology topics. Several of the presentations and sessions at DEVcon-0 would later drive important initiatives to make Ethereum more reliable, more secure, and more scalable. Overall, the event galvanized developers as they continued to work towards the launch of Ethereum.

* `DEVCON-0 talks youtube playlist <https://www.youtube.com/watch?v=_BvvUlKDqp0&list=PLJqWcTqh_zKEjpSej3ddtDOKPRGl_7MhS>`_
* `DEVCON-0 reddit post <https://www.reddit.com/r/ethereum/comments/2nle7m/community_update_whats_going_on_devcon0/>`_
* `Gav's DEV update mentioning DEVCON-0 <https://blog.ethereum.org/2014/11/18/gavs-d%CE%BEv-update-iii/>`_
* `DEVcon-0 recap blog post <https://blog.ethereum.org/2014/12/05/d%CE%BEvcon-0-recap/>`_


DEVgrants program
--------------------------------------------------------------------------------

In April 2015, `the DEVgrants program <https://blog.ethereum.org/2015/04/07/devgrants-help/>`_ was announced, which is a program that offers funding for contributions both to the Ethereum platform, and to projects based on Ethereum. Hundreds of developers were already contributing their time and thinking to Ethereum projects and in open source projects. This program served to reward and support those developers for their contributions. The DEVgrants program continues to operate today and funding of the program was recently renewed in January 2016.

* `DEVgrants initial announcement <https://blog.ethereum.org/2015/04/07/devgrants-help/>`_
* `Announcement of new funding at DEVCON-1 <https://blog.ethereum.org/2016/01/08/d%CE%BEvgrants-update-new-funding/>`_
* `DEVgrants public gitter room <https://gitter.im/devgrants/public>`_
* `DEVgrants talk at DEVCON-1 by Wendell Davis on YouTube <https://www.youtube.com/watch?v=4jGqmlA4KEY>`_

.. _olympic-testnet:

Olympic testnet, bug bounty and security audit
--------------------------------------------------------------------------------

Throughout 2014 and 2015 development went through a series of proof of concept releases leading to the 9th POC open testnet, called Olympic. The developer community was `invited to test the limits of the network <https://blog.ethereum.org/2015/05/09/olympic-frontier-pre-release/>`_ and a substantial prize fund was allocated to award those holding various records or having success in breaking the system in some way or other. The `rewards were announced <https://blog.ethereum.org/2015/08/26/olympic-rewards-announced/>`_ officially a month after the live release.

In early 2015, an `Ethereum Bounty Program <http://bounty.ethereum.org/>`_ was launched, offering BTC rewards for finding vulnerabilities in any part of the Ethereum software stack. This has undoubtedly contributed to the reliability and security of Ethereum and the confidence of the Ethereum community in the technology. The bounty program is currently still active and there is no end date planned.

The Ethereum security audit began at the end of 2014 and continued through the first half of 2015. Ethereum engaged multiple third party software security firms to conduct an end-to-end audit of all protocol-critical components (Ethereum VM, networking, Proof of Work). The audits uncovered security issues that were addressed and tested again and as a result ultimately led to a more secure platform.

* `Olympic testnet prerelease <https://blog.ethereum.org/2015/05/09/olympic-frontier-pre-release/>`_ - Vitalik's blogpost detailing olympic rewards
* `Olympic rewards announced <https://blog.ethereum.org/2015/08/26/olympic-rewards-announced/>`_ - Vitalik's blogpost detailing the winners and prizes
* `Bug bounty program launch <https://blog.ethereum.org/2015/03/20/juttas-update-bug-bounty-program-security-audit/>`_
* `Ethereum Bounty Program website <http://bounty.ethereum.org/>`_
* `Least Authority audit blogpost <https://blog.ethereum.org/2015/07/07/know-ethereum-secure/>`_ - with links to the audit report
* `Deja Vu audit blogpost <http://www.dejavusecurity.com/blog/2015/7/23/deja-vu-security-assists-in-ethereum-release>`_

.. _frontier-launch:

The Ethereum Frontier launch
=======================================================================

The Ethereum Frontier network launched on July 30th, 2015, and developers began writing smart contracts and decentralized apps to deploy on the live Ethereum network. In addition, miners began to join the Ethereum network to help secure the Ethereum blockchain and earn ether from mining blocks. Even though the Frontier release is the first milestone in the Ethereum project and was intended for use by developers as a beta version, it turned out to be more capable and reliable than anyone expected, and developers have rushed in to build solutions and improve the Ethereum ecosystem.

See also:

* `Original announcement of the release scheme <https://blog.ethereum.org/2015/03/03/ethereum-launch-process>`__ by Vinay Gupta
* `Frontier is coming <https://blog.ethereum.org/2015/07/22/frontier-is-coming-what-to-expect-and-how-to-prepare>`_ - Frontier launch announcement by Stephan Tual
* `Frontier launch final steps <https://blog.ethereum.org/2015/07/27/final-steps/>`_ - Follow-up post to announcement
* `Ethereum goes live with Frontier launch <https://blog.ethereum.org/2015/07/30/ethereum-launches>`_
* `The frontier website <https://web.archive.org/web/20160207033817/https://ethereum.org/>`_

DEVCON-1
--------------------------------------------------------------------------------
The second developers' conference `DEVCON-1 <https://devcon.ethereum.org/>`_  took place in the city of London at the beginning of November 2015. The 5-day event featured more than 100 presentations, panel discussions and lightning talks, attracted more than 400 participants, a mix of developers, entrepreneurs, thinkers, and business executives.
The talks were all recorded and are `freely available <https://www.youtube.com/playlist?list=PLJqWcTqh_zKHQUFX4IaVjWjfT2tbS4NVk>`_

The presence of large companies like UBS, IBM and Microsoft clearly indicated enterprise interest in the technology. Microsoft announced that it would offer `Ethereum on its new Blockchain as a Service <https://azure.microsoft.com/en-us/blog/ethereum-blockchain-as-a-service-now-on-azure/>`_  offering on the Microsoft Azure cloud platform. In conjunction with DEVCON-1, this announcement will be remembered as the moment when blockchain technology became mainstream, with Ethereum at the center of it.

* `DEVCON-1 talks Youtube playlist <https://www.youtube.com/playlist?list=PLJqWcTqh_zKHQUFX4IaVjWjfT2tbS4NVk>`_
* `DEVCON-1 website <https://devcon.ethereum.org/>`_ full listing of presentations with links to the slides if available.

History resources
----------------------------------------

* `a simple graphical timeline <http://ethereumtimeline.org/>`_

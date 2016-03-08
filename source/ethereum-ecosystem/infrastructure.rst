.. _infrastructure:

********************************************************************************
Infrastructure
********************************************************************************


The Ethereum network
================================================================================

The basis for decentralised consensus is the peer-to-peer network of participating nodes which maintain and secure the blockchain.

Ethereum network stats
--------------------------------------------------

`EthStats\.net <https://ethstats.net/>`_ is a dashboard of live statistics of the Ethereum network. This dashboard displays important information such as the current block, hash difficulty, gas price, and gas spending. The nodes shown on the page are only a selection of actual nodes on the network. 
Anyone is allowed to add their node to the EthStats dashboard. The `Eth\-Netstats README on Github <https://github.com/cubedro/eth-netstats>`_ describes how to connect.

`EtherNodes\.com <https://www.ethernodes.org/>`_ displays current and historical data on node count and other information on both the Ethereum mainnet and Morden testnet.

Public, private, and consortium blockchains
------------------------------------------------

Most Ethereum projects today rely on Ethereum as a public blockchain, which grants access to a larger audience of users, network nodes, currency, and markets.  However, there are often reasons to prefer a private blockchain or consortium blockchain (among a group of trusted participants). For example, a number of companies in verticals, like banking, are looking to Ethereum as a platform for their own private blockchains.

Below is an excerpt from the blog post `On Public and Private Blockchains <https://blog.ethereum.org/2015/08/07/on-public-and-private-blockchains/>`_ that explains the difference between the three types of blockchains based on permissioning:

**Public blockchains**: a public blockchain is a blockchain that anyone in the world can read, anyone in the world can send transactions to and expect to see them included if they are valid, and anyone in the world can participate in the consensus process – the process for determining what blocks get added to the chain and what the current state is. As a substitute for centralized or quasi-centralized trust, public blockchains are secured by cryptoeconomics – the combination of economic incentives and cryptographic verification using mechanisms such as proof of work or proof of stake, following a general principle that the degree to which someone can have an influence in the consensus process is proportional to the quantity of economic resources that they can bring to bear. These blockchains are generally considered to be “fully decentralized”.

**Consortium blockchains**: a consortium blockchain is a blockchain where the consensus process is controlled by a pre-selected set of nodes; for example, one might imagine a consortium of 15 financial institutions, each of which operates a node and of which 10 must sign every block in order for the block to be valid. The right to read the blockchain may be public, or restricted to the participants, and there are also hybrid routes such as the root hashes of the blocks being public together with an API that allows members of the public to make a limited number of queries and get back cryptographic proofs of some parts of the blockchain state. These blockchains may be considered “partially decentralized”.

**Private blockchains**: a fully private blockchain is a blockchain where write permissions are kept centralized to one organization. Read permissions may be public or restricted to an arbitrary extent. Likely applications include database management, auditing, etc internal to a single company, and so public readability may not be necessary in many cases at all, though in other cases public auditability is desired.

While these private/consortium blockchains may not have any connection to the public blockchain, they still contribute to the overall Ethereum ecosystem by investing in Ethereum software development. Over time, this translates into software improvements, shared knowledge, and job opportunities.


Client implementations
================================================================================

Ethereum clients are written in multiple programming languages. Each implementation is based on the formal definition of the Ethereum protocol defined in the `Ethereum Yellow Paper <http://gavwood.com/paper.pdf>`_.

Client List
------------------------

===============         ===============
Language                 Name
===============         ===============
Golang                   `Geth <http://ethereum.github.io/go-ethereum/>`_
C++                      `Eth <https://github.com/ethereum/webthree-umbrella/wiki>`_
Javascript/Node          `EthereumJS <http://ethereumjs.github.io/>`_
Python                   `Pyethereum <https://github.com/ethereum/pyethereum>`_
Java                     `ethereumJ <https://github.com/ethereum/ethereumj>`_
Haskell                  `ethereumH <https://github.com/blockapps/strato-p2p-client>`_
Rust                     `Parity <https://ethcore.io/parity.html>`__
===============         ===============

Other Resources
--------------------------------------------------------------------------------
* `Distribution of client implementations on the current live network <https://etherchain.org/nodes>`_ - Realtime stats on EtherChain.
* `What is the need for that many implementations\? <https://www.reddit.com/r/ethereum/comments/2bxo9c/whats_the_need_for_that_many_implementations/>`_ - Reddit discussion.

.. _blockchain_explorers:

Blockchain explorers
================================================================================

Hosted blockchain explorers
--------------------------------------------------------------------------------

-  `EtherChain <https://www.etherchain.org/>`_
-  `EtherCamp <https://live.ether.camp/>`_
-  `EtherScan <http://etherscan.io/>`_
-  `Etherscan Morden Testnet  <http://testnet.etherscan.io>`_
-  `EtherBlockchain <http://www.etherblockchain.io/>`_ (to come)

Alternative ways to explore the blockchain
--------------------------------------------------------------------------------

* `Etherlisten <www.etherlisten.com>`_ - Realtime Ethereum transaction visualizer and audializer
* `chaingraph <https://www.reddit.com/r/ethereum/comments/3ibjxu/chain_graph_a_blockchain_visualiser/>`_ - Visualised blockchain explorer - *no longer available*

Getting and storing Ether
================================================================================

In order to obtain Ether, you need to either

* become an Ethereum miner (see _`Mining`)  or
* trade other currencies for Ether using centralised or trustless services
* use the user friendly `Mist Ethereum Wallet <https://github.com/ethereum/mist/releases>`_ that as of Beta 6 introduced the ability to purchase ether using the `Shapeshift`_ API.

Trustless services
--------------------------------------------------------------------------------

Note that the ethereum platform is special in that the smart contracts enable trustless services that obviate the need for trusted third parties in a currency exchange transaction, ie. disintermediate currency exchange businesses.

Such projects (alpha/prelaunch status at the time of writing) are:

* `BTCrelay <http://btcrelay.org/>`_ - `More information <https://medium.com/@ConsenSys/taking-stock-bitcoin-and-ethereum-4382f0a2f17>`_ (about ETH/BTC 2-way peg without modifying bitcoin code).
* `EtherEx decentralised exchange <https://etherex.org>`_.

List of centralised exchange marketplaces
--------------------------------------------------------------------------------

========================== ============================
Exchange                   Currencies
========================== ============================
Poloniex                   BTC
Kraken                     BTC, USD, EUR, CAD, GBP
Gatecoin                   BTC, EUR
Bittrex                    BTC
Bluetrade                  BTC, LTC, DOGE
HitBTC                     BTC
Livecoin                   BTC
Coinsquare                 BTC
Bittylicious               GBP
BTER                       CNY
Yunbi                      CNY
Metaexchange               BTC
========================== ============================

Centralised fixed rate exchanges
-----------------------------------

========================== ============================
Exchange                   Currencies
========================== ============================
`Shapeshift`_              BTC, LTC, DOGE, Other
`Bity`_                    BTC, USD, EUR, CHF
========================== ============================

.. _Bity: https://bity.com
.. _Shapeshift: shapeshift.io>

Trading and price analytics
--------------------------------------------------------------------------------

* `ETH markets exhaustive listing by volume on coinmarketcap <https://coinmarketcap.com/currencies/ethereum/#markets>`_
* Aggregating realtime stats of major ETH markets:

  * `Tradeblock <https://tradeblock.com/ethereum>`_
  * `EthereumWisdom <http://ethereumwisdom.com>`_
  * `Cryptocompare <https://www.cryptocompare.com/coins/eth/overview>`_
  * `Coinmarketcap <https://coinmarketcap.com/currencies/ethereum/>`_

.. _Ethereum-wallets-and-storage-solutions:

Ethereum wallets and storage solutions
----------------------------------------------------

* `Mist Ethereum Wallet <https://github.com/ethereum/mist/releases>`_ - Wallet created by the Ethereum Foundation. Standalone GUI wallet.
* `MyEtherWallet <https://www.myetherwallet.com/>`_ - Open Source JavaScript Client-Side/Online Ether Wallet.
* `MyEtherWallet Chrome Extension <http://sebfor.com/myetherwallet-chrome-extension-release/>`_ - 100% client side wallet allows you to save your wallets in your browser and transfer Ether from any page.
* Presale wallet import in Geth client.
* `Jaxx wallets <https://jaxx.io>`_ by `Kyptokit <http://krypyokit.org>`_ - Android App and Chrome extension.
* `Icebox <https://github.com/ConsenSys/icebox>`_ by `ConsenSys <https://consensys.net/>`_ - Cold storage based on lightwallet with HD wallet library integrated.
* `Kraken Wallet Sweeper Tool <https://www.kraken.com/ether>`_ - Pre-sale wallet import

Mining pools
================================================================================

* `coinotron`_
* `nanopool`_
* `ethpool`_ - Predictable solo mining, unconventional payout scheme, affiliated with `etherchain\.org`_.
* `supernova`_
* `coinmine.pl`_
* `eth.pp.ua`_
* `talkether`_ - Unconventional payout scheme
* `weipool`_
* `ethereumpool`_
* `pooleum`_
* `alphapool`_
* `dwarfpool`_
* `laintimes <http://pool.laintimes.com/>`_ - Discontinued

.. _Ethpool: https://github.com/etherchain-org/ethpool-core
.. _Ethpool source: https://github.com/etherchain-org/ethpool-core
.. _ethereumpool: https://ethereumpool.co/
.. _nanopool: http://eth.nanopool.org/
.. _pooleum:
.. _alphapool:
.. _dwarfpool: http://dwarfpool.com/eth
.. _talkether: http://talkether.org/
.. _weipool: http://weipool.org/
.. _supernova: https://eth.suprnova.cc/
.. _coinmine.pl: https://www2.coinmine.pl/eth/
.. _eth.pp.ua:  https://eth.pp.ua/
.. _coinotron: https://www.coinotron.com/
.. _etherchain.org: https://etherchain.org/


Resources
--------------------------------------------------------------------------------
* `Top miners of last 24h on etherchain <https://etherchain.org/statistics/miners>`_
* `pool hashrate distribution for august 2015 <ehttp://cryptomining-blog.com/5607-the-current-state-of-ethereum-mining-pools/>`_
* `Unmaintained list of pools on Forum <https://forum.ethereum.org/discussion/3659/list-of-pools>`_
* `Mining profitability calculator by cryptowizzard <http://cryptowizzard.github.io/eth-mining-calculator/>`_
* `Mining profitability calculator on etherscan <http://etherscan.io/ether-mining-calculator>`_
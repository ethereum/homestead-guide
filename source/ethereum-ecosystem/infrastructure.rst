********************************************************************************
Client Implementations
********************************************************************************
Ethereum clients are written in multiple programming languages. Each implementation is based on the formal definition of the Ethereum protocol defined in the `Ethereum Yellow Paper <http://gavwood.com/paper.pdf>`_.

Client List
===============

===============         ===============
Language                 Name
===============         ===============
Golang                   `Geth <http://ethereum.github.io/go-ethereum/>`_
C++                      `TurboEthereum (formerly eth) <https://github.com/ethereum/webthree-umbrella/wiki>`_
Javas/Node          `EthereumJS <http://ethereumjs.github.io/>`_
Python                   `Pyethereum <https://github.com/ethereum/pyethereum>`_
Java                     `ethereumJ <https://github.com/ethereum/ethereumj>`_
Haskell                  `ethereumH <https://github.com/blockapps/strato-p2p-client>`_
Rust                     `Parity <https://ethcore.io/parity.html>`__
===============         ===============

Resources
=============
* `Distribution of client implementations on the current live network <https://etherchain.org/nodes>`_ - realtime stats on etherchain
* `What is the need for that many implementations <https://www.reddit.com/r/ethereum/comments/2bxo9c/whats_the_need_for_that_many_implementations/>`_ - reddit discussion

********************************************************************************
Ethereum Network Stats
********************************************************************************

Live statistics on the Ethereum network can be viewed on the `stats dashboard <https://ethstats.net/>`_. This dashboard displays important numbers such as the current block, hash difficulty, gas price and gas spending and is updated realitime.
The nodes shown on the page are only a selection of actual nodes on the network.
Anyone can connect, the `Netstats README on github <>` describes how.



Private blockchains and applications
---------------------------------------------------------------
Most Ethereum projects today rely on Ethereum as a public blockchain, which grants access to a larger audience of users, network nodes, currency, and markets.  However, there are often reasons to prefer a private blockchain or consortium blockchain (among a group of trusted participants), and the Ethereum community fully supports this. For example, a number of companies in verticals like banking and insurance are looking to Ethereum as a platform for their own private blockchains.

While these private blockchains may not have any connection to the public blockchain, they still contribute to the overall Ethereum ecosystem by investing in Ethereum software development. Over time, this translates into software improvements, shared knowledge, and job opportunities.



TODO
   extend network stats to network types explanation private/consortium? (or at least put to glossary)


ine testnet Ethereum
- Use the `Ethereum wei faucet <https://zerogox.com/ethereum/wei_faucet>`__.
Getting Morden Testnet Ether
--------------------------------------------------------------------------------

Three ways to get Morden testnet ether:

- You can m
.. todo::
   Finish Morden Testnet Section

********************************************************************************
Blockchain explorers
********************************************************************************

Hosted blockchain xplorers
-----------------------------------

-  `EtherChain <https://www.etherchain.org/>`_
-  `Ether.Camp <https://live.ether.camp/>`_
-  `Etherscan`_ <http://etherscan.io/>- `Etherscan Morden Testnet  <http://testnet.etherscan.io>`_
- `EtherBlockchain <http://www.etherblockchain.io/>`_

Alternative ways to explore the blockchain
-------------------------------------------------------------

* `Etherlisten <www.etherlisten.com>`_ realtime Ethereum transaction visualizer and audializer
* `chaingraph <https://www.reddit.com/r/ethereum/comments/3ibjxu/chain_graph_a_blockchain_visualiser/>`_ - visualised blockchain explorer - *no longer available*


********************************************************************************
Mining pools
********************************************************************************

* `coinotron`_
* `nanopool`_
* `ethpool`_ - Predictable solo mining, unconventional payout scheme, affiliated with etherchain.org - open source: `Ethpool on github`_
* `supernova`_
* `coinmine.pl
* `eth.pp.ua`_
* `talkether`_   - unconventional payout scheme
* `weipool`_
* `ethereumpool`_
* `pooleum`_
* `alphapool`_
* `dwarfpool <http://dwarfpool.com/>`_
* `laintimes <http://pool.laintimes.com/>` - discontinued

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


Resources
----------------------
* `Top miners of last 24h on etherchain <https://etherchain.org/statistics/miners>`_
* `pool hashrate distribution for august 2015 <ehttp://cryptomining-blog.com/5607-the-current-state-of-ethereum-mining-pools/>`_
* `Unmaintained list of pools on Forum <https://forum.ethereum.org/discussion/3659/list-of-pools>`_
* `Mining profitability calculator by cryptowizzard <http://cryptowizzard.github.io/eth-mining-calculator/>`_
* `Mining profitability calculator on etherscan <http://etherscan.io/ether-mining-calculator>`_

********************************************************************************
Getting and storing Ether
********************************************************************************

In order to obtain Ether, you need to either
* become an Ethereum miner (see _`Mining`)  or
* trade other currencies for Ether

Trustless services
----------------------------

Note that the ethereum platform is special in that the smart contracts enable trustless services that obviate the need for trusted third parties in a currency exchange transaction, ie. disintermediate currency exchange businesses.

Such projects (alpha/prelaunch status at the time of writing) are
* `BTCrelay <>`_ - /
  * `Towards ETH/BTC 2-way peg <https://medium.com/@ConsenSys/taking-stock-bitcoin-and-ethereum-4382f0a2f17>`_
* `EtherEx decentralised exchange <https://etherex.org>`_

List of centralised exchanges
-------------------------------

========================== ============================
Exchange                   Currencies
Poloniex                   BTC
Kraken                     BTC, USD, EUR, CAD, GBP
Gatecoin                   BTC, EUR
Shapeshift                 BTC,
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

Trading and price analytic
-------------------------------

* `ETH markets exhaustive listing by volume on coinmarketcap <https://coinmarketcap.com/currencies/ethereum/#markets>`_
* Aggregating realtime stats of major ETH markets:
  * `Tradeblock <https://tradeblock.com/ethereum>`_
  * `Ethereumwisdom <http://ethereumwisdom.com>`_
  * `Cryptocompare <https://www.cryptocompare.com/coins/eth/overview>`_
  * `Coinmarketcap <https://coinmarketcap.com/currencies/ethereum/>`_
* `Shapeshift <shapeshift.io>`_ - easy fix-rate exchange between BTC and ETH

===================================================================
Wallet and Ether storage services
===================================================================

* `Mist Ethereum Wallet <>`_ by the Foundation, standalone GUI wallet
* `MyEtherWallet <>`_ with
  * `Chrome Extension <http://sebfor.com/myetherwallet-chrome-extension-release/>`_
  * `presale wallet import`
* `Jaxx wallets <https://jaxx.io>`_ by `Kyptokit <http://krypyokit.org>`_ - android app and chrome extension
* `Icebox <>`_ by `ConsenSys <>`_ cold storage based on lightwallet HD wallet lib
* `Kraken sweeper tool <http://kraken.com/>`_ - Presale wallet import



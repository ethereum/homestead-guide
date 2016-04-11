********************************************************************************
Ether
********************************************************************************

What is ether?
================================================================================

Ether is the name of the currency used within Ethereum. It is used to pay for
computation within the EVM. This is done indirectly by purchasing gas for ether as explained in _`gas`.

Denominations
--------------------------------------------------------

Ethereum has a metric system of denominations used as units of Ether. Each denomination has its own unique name (some bear the family name of seminal figures playing a role in evolution of computer science and cryptoeconomics). The smallest denomination aka *base unit* of Ether is called Wei. Below is a list of the named denominations and
their value in Wei. Following a common (although somewhat ambiguous) pattern, Ether also designates a unit (of 1e18 or one quintillion Wei) of the currency. Note that the currency is not called Ethereum as many mistakenly think, nor is Ethereum a unit.


+-------------------------+-----------+-------------------------------------------+
| Unit                    | Wei Value | Wei                                       |
+=========================+===========+===========================================+
| **wei**                 | 1 wei     | 1                                         |
+-------------------------+-----------+-------------------------------------------+
| **Kwei (babbage)**      | 1e3 wei   | 1,000                                     |
+-------------------------+-----------+-------------------------------------------+
| **Mwei (lovelace)**     | 1e6 wei   | 1,000,000                                 |
+-------------------------+-----------+-------------------------------------------+
| **Gwei (shannon)**      | 1e9 wei   | 1,000,000,000                             |
+-------------------------+-----------+-------------------------------------------+
| **microether (szabo)**  | 1e12 wei  | 1,000,000,000,000                         |
+-------------------------+-----------+-------------------------------------------+
| **milliether (finney)** | 1e15 wei  | 1,000,000,000,000,000                     |
+-------------------------+-----------+-------------------------------------------+
| **ether**               | 1e18 wei  | 1,000,000,000,000,000,000                 |
+-------------------------+-----------+-------------------------------------------+


Ether supply
=========================

* https://blog.ethereum.org/2014/04/10/the-issuance-model-in-ethereum/
* https://www.reddit.com/r/ethereum/comments/44zy88/clarification_on_ether_supply_and_cost_of_gas/
* https://www.reddit.com/r/ethereum/comments/45vj4g/question_about_scarcity_of_ethereum_and_its/
* https://www.reddit.com/r/ethtrader/comments/48yqg6/is_there_a_cap_like_with_btc_with_how_many_ether/


Getting ether
================================================================================

In order to obtain Ether, you need to either

* become an Ethereum miner (see _`Mining`)  or
* trade other currencies for Ether using centralised or trustless services
* use the user friendly `Mist Ethereum GUI Wallet <https://github.com/ethereum/mist/releases>`_ that as of Beta 6 introduced the ability to purchase ether using the http://shapeshift.io/ API.

Trustless services
--------------------------------------------------------------------------------

Note that the Ethereum platform is special in that the smart contracts enable trustless services that obviate the need for trusted third parties in a currency exchange transaction, ie. disintermediate currency exchange businesses.

Such projects (alpha/prelaunch status at the time of writing) are:

* `BTCrelay <http://btcrelay.org/>`_
   * `More information <https://medium.com/@ConsenSys/taking-stock-bitcoin-and-ethereum-4382f0a2f17>`_ (about ETH/BTC 2-way peg without modifying bitcoin code).
   * `BTCrelay audit <http://martin.swende.se/blog/BTCRelay-Auditing.html>`_
* `EtherEx decentralised exchange <https://etherex.org>`_.

List of centralised exchange marketplaces
--------------------------------------------------------------------------------

========================== ============================
Exchange                   Currencies
========================== ============================
Poloniex                   BTC
Kraken                     BTC, USD, EUR, CAD, GBP
Gatecoin                   BTC, EUR
Bitfinex                   BTC, USD
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
.. _Shapeshift: shapeshift.io


Trading and price analytics
--------------------------------------------------------------------------------

* `ETH markets exhaustive listing by volume on coinmarketcap <https://coinmarketcap.com/currencies/ethereum/#markets>`_
* Aggregating realtime stats of major ETH markets:

  * `Tradeblock <https://tradeblock.com/ethereum>`_
  * `EthereumWisdom <http://ethereumwisdom.com>`_
  * `Cryptocompare <https://www.cryptocompare.com/coins/eth/overview>`_
  * `Coinmarketcap <https://coinmarketcap.com/currencies/ethereum/>`_


.. _online-wallets-and-storage-solutions:

Online wallets, paper wallets, and cold storage
================================================================================

.. todo::
  This is here just a dumping ground of links and notes
  Please move this over in a listing form to ecosystem

  Keep examples here, maybe explain paranoid practices, list dangers

* Mist Ethereum Wallet
    * `Releases to download <https://github.com/ethereum/mist/releases>`_
    * `Mist Ethereum Wallet developer preview <https://blog.ethereum.org/2015/09/16/ethereum-wallet-developer-preview/>`_ - foundation blog post
    * `How to easily set up the Ethereum Mist wallet! <https://www.youtube.com/watch?v=Z6lE0Ctaeqs>`_ - Tutorial by Tommy Economics
* Kryptokit Jaxx
    * `Jaxx main site <http://jaxx.io/>`_
    * `Mobile release <http://favs.pw/first-ethereum-mobile-app-released/#.VsHn_PGPL5c>`_
* Etherwall
    * `Etherwall website <http://www.etherwall.com/>`_
    * `Etherwall source <https://github.com/almindor/etherwall>`_
* MyEtherWallet
    * `MyEtherWallet website <https://www.myetherwallet.com/>`_
    * `MyEtherWallet source <https://github.com/kvhnuke/etherwallet/>`_
    * `Chrome extension <http://sebfor.com/myetherwallet-chrome-extension-release/>`_
* Cold storage
    * `Icebox <https://github.com/ConsenSys/icebox>`_ by `ConsenSys <https://consensys.net/>`_ - Cold storage based on lightwallet with HD wallet library integrated.
    * `Reddit discussion 1 <https://www.reddit.com/r/ethereum/comments/45uvmy/offline_cold_storage_question/offline_cold_storage_question>`_
    * `How to setup a cold storage wallet <https://www.reddit.com/r/ethereum/comments/48wfbv/eli5_how_to_setup_a_cold_storage_wallet_as/>`_
* Hardware wallet
    * `reddit discussion 2 <https://www.reddit.com/r/ethereum/comments/45siaq/hardware_wallet/>`_
    * `reddit discussion 3 <https://www.reddit.com/r/ethereum/comments/4521o4/crowdfunding_ethereum_hardware_cold_storage_wallet/>`_
* Brain wallet
    * brain wallets are not safe, do not use them. https://www.reddit.com/r/ethereum/comments/45y8m7/brain_wallets_are_now_generally_shunned_by/
    * Extreme caution with brain wallets. Read the recent controversy: https://reddit.com/r/ethereum/comments/43fhb5/brainwallets vs http://blog.ether.camp/post/138376049438/why-brain-wallet-is-the-best
* Misc
    * `Kraken Wallet Sweeper Tool <https://www.kraken.com/ether>`_ - Pre-sale wallet import
    * `Recommended ways to safely store ether <http://ethereum.stackexchange.com/questions/1239/what-is-the-recommended-way-to-safely-store-ether>`_
    * `How to buy and store ether <http://sebfor.com/how-to-buy-and-store-ether/>`_
    * `A laymen's intro into brute forcing and why not to use brain wallets <http://www.fastcompany.com/3056651/researchers-find-a-crack-that-drains-supposedly-secure-bitcoin-wallets>`_
    * `Pyethsaletool <https://github.com/ethereum/pyethsaletool/blob/master/README.md>`_
    * `Account vs wallet <https://www.reddit.com/r/ethereum/comments/47j3r5/eli5_accounts_vs_wallet_contracts_on_mist/>`_

Sending ether
================================================================================

The `Ethereum Wallet  <https://github.com/ethereum/mist/releases>`_  supports sending ether via a graphical interface.

Ether can also be transferred using the **geth console**.

.. code-block:: console

    > var sender = eth.accounts[0];
    > var receiver = eth.accounts[1];
    > var amount = web3.toWei(0.01, "ether")
    > eth.sendTransaction({from:sender, to:receiver, value: amount})

For more information of Ether transfer transactions, see :ref:`account-types-gas-and-transactions`.

Ethereum is unique in the realm of cryptocurrencies in that ether has utility value as a cryptofuel, commonly referred to as "gas". Beyond transaction fees, gas is a central part of every network request and requires the sender to pay for the computing resources consumed. The gas cost is dynamically calculated, based on the volume and complexity of the request and multiplied by the current gas price. Its value as a cryptofuel has the effect of increasing the stability and long-term  demand for ether and Ethereum as a whole. For more information, see :ref:`account-types-gas-and-transactions`.

Gas and ether
=============================

* https://www.reddit.com/r/ethereum/comments/271qdz/can_someone_explain_the_concept_of_gas_in_ethereum/
* https://www.reddit.com/r/ethereum/comments/3fnpr1/can_someone_possibly_explain_the_concept_of/
* https://www.reddit.com/r/ethereum/comments/49gol3/can_ether_be_used_as_a_currency_eli5_ether_gas/


Gas is supposed to be the constant cost of network resources/utilisation. You want the real cost of sending a transaction to always be the same, so you can't really expect Gas to be issued, currencies in general are volatile.

So instead, we issue Ether whose value is supposed to vary, but also implement a Gas Price in terms of Ether. If the price of Ether goes up, the Gas Price in terms of Ether should go down to keep the real cost of Gas the same.

Gas has multiple associated terms with it: Gas Prices, Gas Cost, Gas Limit, and Gas Fees. The principle behind Gas is to have a stable value for how much a transaction or computation costs on the Ethereum network.

* Gas Cost is a static value for how much a computation costs in terms of Gas, and the intent is that the real value of the Gas never changes, so this cost should always stay stable over time.
* Gas Price is how much Gas costs in terms of another currency or token like Ether. To stabilise the value of gas, the Gas Price is a floating value such that if the cost of tokens or currency fluctuates, the Gas Price changes to keep the same real value. The Gas Price is set by the equilibrium price of how much users are willing to spend, and how much processing nodes are willing to accept.
* Gas Limit is the maximum amount of Gas that can be used per block, it is considered the maximum computational load, transaction volume, or block size of a block, and miners can slowly change this value over time.
* Gas Fee is effectively the amount of Gas needed to be paid to run a particular transaction or program (called a contract). The Gas Fees of a block can be used to imply the computational load, transaction volume, or size of a block. The gas fees are paid to the miners (or bonded contractors in PoS).

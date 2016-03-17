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


Getting and storing ether
================================================================================

In order to obtain Ether, you need to either

* become an Ethereum miner (see _`Mining`)  or
* trade other currencies for Ether using centralised or trustless services
* use the user friendly `Mist Ethereum GUI Wallet <https://github.com/ethereum/mist/releases>`_ that as of Beta 6 introduced the ability to purchase ether using the `Shapeshift`_ API.

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
    * How to easily set up the Ethereum Mist wallet! *Tutorial* – Tommy Economics – https://www.youtube.com/watch?v=Z6lE0Ctaeqs
* Kryptokit Jaxx
    * `Jaxx main site <http://jaxx.io/>`_
    * `Mobile release <http://favs.pw/first-ethereum-mobile-app-released/#.VsHn_PGPL5c>`_
* Etherwall
    * `Etherwall website <http://www.etherwall.com/>`_
    * `Etherwall source <https://github.com/almindor/etherwall>`_
* MyEtherWallet
    * `MyEtherWallet website <https://www.myetherwallet.com/>`_
    * `MyEtherWallet source <https://github.com/kvhnuke/etherwallet/>`_
    * `chrome extention <http://sebfor.com/myetherwallet-chrome-extension-release/>`_
* Cold storage
    * `Icebox <https://github.com/ConsenSys/icebox>`_ by `ConsenSys <https://consensys.net/>`_ - Cold storage based on lightwallet with HD wallet library integrated.
    * `reddit discussion 1 <https://www.reddit.com/r/ethereum/comments/45uvmy/offline_cold_storage_question/offline_cold_storage_question>`_
* Hardware wallet
    * `reddit discussion 2 <https://www.reddit.com/r/ethereum/comments/45siaq/hardware_wallet/>`_
    * `reddit discussion 3 <https://www.reddit.com/r/ethereum/comments/4521o4/crowdfunding_ethereum_hardware_cold_storage_wallet/>`_
* Brain wallet
    * brain wallets are not safe, do not use them. https://www.reddit.com/r/ethereum/comments/45y8m7/brain_wallets_are_now_generally_shunned_by/
    * Extreme caution with brain wallets. Read the recent controversy: https://reddit.com/r/ethereum/comments/43fhb5/brainwallets vs http://blog.ether.camp/post/138376049438/why-brain-wallet-is-the-best
* Misc
    * `Kraken Wallet Sweeper Tool <https://www.kraken.com/ether>`_ - Pre-sale wallet import
    * `Recommended ways to safely store ether <http://ethereum.stackexchange.com/questions/1239/what-is-the-recommended-way-to-safely-store-ether>`_
    * `How to buy and stole ether <http://sebfor.com/how-to-buy-and-store-ether/>`_
    * `A laymen's intro into brute forcing and why not to use brain wallets <http://www.fastcompany.com/3056651/researchers-find-a-crack-that-drains-supposedly-secure-bitcoin-wallets>`_
    * `Pyethsaletool <https://github.com/ethereum/pyethsaletool/blob/master/README.md>`_


Sending ether
================================================================================

The `Ethereum Wallet  <https://github.com/ethereum/mist/releases>`_  supports sending ether via a graphical interface.

Ether can also be transfered using the **geth console**.

.. code-block:: console

    > var sender = eth.accounts[0];
    > var receiver = eth.accounts[1];
    > var amount = web3.toWei(0.01, "ether")
    > eth.sendTransaction({from:sender, to:receiver, value: amount})

For more information of Ether transfer transactions, see :ref:`account-types-gas-and-transactions`.

Ethereum is unique in the realm of cryptocurrencies in that ether has utility value as a cryptofuel, commonly referred to as "gas". Beyond transaction fees, gas is a central part of every network request and requires the sender to pay for the computing resources consumed. The gas cost is dynamically calculated, based on the volume and complexity of the request and multiplied by the current gas price. Its value as a cryptofuel has the effect of increasing the stability and long-term  demand for ether and Ethereum as a whole. For more information, see :ref:`account-types-gas-and-transactions`.



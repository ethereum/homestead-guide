********************************************************************************
Ether
********************************************************************************

What is Ether?
================================================================================

Ether is the base unit of currency used within Ethereum.  It is used to pay for
computation within the EVM

Denominations
================================================================================

There are different denominations used in Ether and each denomination has its
own unique name and value. Below is a list of different denomination names and
how they are related to Ether.

+=====================+===========+===========================================+
| unit                | wei value |                                           |
+=====================+===========+===========================================+
| **wei**             | 1 wei     | 1                                         |
| **Kwei (babbage)**  | 1e3 wei   | 1,000                                     |
| **Mwei (lovelace)** | 1e6 wei   | 1,000,000                                 |
| **Gwei (shannon)**  | 1e9 wei   | 1,000,000,000                             |
| **szabo**           | 1e12 wei  | 1,000,000,000,000                         |
| **finney**          | 1e15 wei  | 1,000,000,000,000,000                     |
| **ether**           | 1e18 wei  | 1,000,000,000,000,000,000                 |
| **kether**          | 1e21 wei  | 1,000,000,000,000,000,000,000             |
| **Mether**          | 1e24 wei  | 1,000,000,000,000,000,000,000,000         |
| **Gether**          | 1e27 wei  | 1,000,000,000,000,000,000,000,000,000     |
| **Tether**          | 1e30 wei  | 1,000,000,000,000,000,000,000,000,000,000 |
+---------------------+-----------+-------------------------------------------+

Getting Ether
================================================================================

Version 0.3.9 (Beta 6) of the `Ethereum Wallet`_ introduced the ability to
purchase ether via Shape Shift.

You can also purchase Ether on any exchange which supports the currency.  As of
2015-02-12 Poloniex was the exchange with the highest volume in Ethereum
transactions.

[Will point to mining and exchanges pages with explanation of both]

Sending Ether
================================================================================

The `Ethereum Wallet`_ supports sending ether via a graphical interface.

Ether can also be transfered using the **geth console**.

.. code-block:: bash

    > var sender = eth.accounts[0];
    > var receiver = eth.accounts[1];
    > var amount = web3.toWei(0.01, "ether")
    > eth.sendTransaction({from:sender, to:receiver, value: amount})



.. _Ethereum Wallet: https://github.com/ethereum/mist/releases/tag/0.3.9

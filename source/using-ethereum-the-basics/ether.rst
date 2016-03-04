********************************************************************************
Ether
********************************************************************************

What is Ether?
================================================================================

Ether is the name of the currency used within Ethereum. It is used to pay for
computation within the EVM. This is done indirectly by purchasing gas for ether as explained in _`Gas and cryptofuel`.

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



Sending Ether
================================================================================

On how to acquire or purchase Ether, see _`Getting and storing Ether`.

The `Ethereum Wallet  <https://github.com/ethereum/mist/releases>`_  supports sending ether via a graphical interface.

Ether can also be transfered using the **geth console**.

.. code-block:: console

    > var sender = eth.accounts[0];
    > var receiver = eth.accounts[1];
    > var amount = web3.toWei(0.01, "ether")
    > eth.sendTransaction({from:sender, to:receiver, value: amount})


For more information of Ether transfer transactions, see :ref:`account-types-gas-and-transactions`.

Ethereum is unique in the realm of cryptocurrencies in that ether has utility value as a cryptofuel, commonly referred to as "gas". Beyond transaction fees, gas is a central part of every network request and requires the sender to pay for the computing resources consumed. The gas cost is dynamically calculated, based on the volume and complexity of the request and multiplied by the current gas price. Its value as a cryptofuel has the effect of increasing the stability and long-term  demand for ether and Ethereum as a whole. For more information, see :ref:`account-types-gas-and-transactions`.



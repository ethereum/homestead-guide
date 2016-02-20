********************************************************************************
Ether
********************************************************************************

What is Ether?
================================================================================

Ether is the name of the currency used within Ethereum. It is used to pay for
computation within the EVM. This is done indirectly by purchasing gas for ether as explained in _`gas and cryptofuel`.

Denominations
--------------------------------------------------------

Ethereum has a metric system of denominations used as units of Ether. Each denomination has its own unique name (some bear the family name of seminal figures playing a role in evolution of computer science and cryptoeconomics). The smallest denomination aka *base unit* of Ether is called Wei. Below is a list of the named denominations and
their value in Wei. Following a common (although somewhat ambiguous) pattern, Ether also designates a unit (of 1e18 or one trillion Wei) of the currency. Note that the currency is not called Ethereum as many mistakenly think, nor is Ethereum a unit.

+---------------------+-----------+-------------------------------------------+
| Unit                | Wei Value | Wei                                       |
+=====================+===========+===========================================+
| **wei**             | 1 wei     | 1                                         |
+---------------------+-----------+-------------------------------------------+
| **Kwei (babbage)**  | 1e3 wei   | 1,000                                     |
+---------------------+-----------+-------------------------------------------+
| **Mwei (lovelace)** | 1e6 wei   | 1,000,000                                 |
+---------------------+-----------+-------------------------------------------+
| **Gwei (shannon)**  | 1e9 wei   | 1,000,000,000                             |
+---------------------+-----------+-------------------------------------------+
| **szabo**           | 1e12 wei  | 1,000,000,000,000                         |
+---------------------+-----------+-------------------------------------------+
| **finney**          | 1e15 wei  | 1,000,000,000,000,000                     |
+---------------------+-----------+-------------------------------------------+
| **ether**           | 1e18 wei  | 1,000,000,000,000,000,000                 |
+---------------------+-----------+-------------------------------------------+
| **kether**          | 1e21 wei  | 1,000,000,000,000,000,000,000             |
+---------------------+-----------+-------------------------------------------+
| **Mether**          | 1e24 wei  | 1,000,000,000,000,000,000,000,000         |
+---------------------+-----------+-------------------------------------------+
| **Gether**          | 1e27 wei  | 1,000,000,000,000,000,000,000,000,000     |
+---------------------+-----------+-------------------------------------------+
| **Tether**          | 1e30 wei  | 1,000,000,000,000,000,000,000,000,000,000 |
+---------------------+-----------+-------------------------------------------+

Getting Ether
-----------------------------------------------------------

Users, traders and miners

Version 0.3.9 (Beta 6) of the `Ethereum Wallet`_ introduced the ability to
purchase ether via Shape Shift.

You can also purchase Ether on any exchange which supports the currency.  As
of 2015-02-12 Poloniex was the exchange with the highest volume in Ethereum
transactions.

Ether may also be mined using your computer's graphics card (GPU). To be
efficient the GPU should have a sufficient amount of memory, as it must hold
and access the "DAG" efficiently. The DAG is a resource that is required by
Ethash, the ASIC-resistant (i.e. memory-hard) proof of work algorithm used by
Ethereum. The DAG is more than 1 GB in size.

[Will point to mining and exchanges pages with explanation of both]

Sending Ether
================================================================================

The `Ethereum Wallet <`_ supports sending ether via a graphical interface.

Ether can also be transfered using the **geth console**.

.. code-block:: shell

    > var sender = eth.accounts[0];
    > var receiver = eth.accounts[1];
    > var amount = web3.toWei(0.01, "ether")
    > eth.sendTransaction({from:sender, to:receiver, value: amount})


Notably, Ethereum is unique in the realm of cryptocurrencies in that ether has utility value as a cryptofuel, commonly referred to as "gas". Beyond transaction fees, gas is a central part of every network request and requires the sender to pay for the computing resources consumed. The gas cost is dynamically calculated, based on the volume and complexity of the request and multiplied by the current gas price. Its value as a cryptofuel has the effect of increasing the stability and long-term  demand for ether and Ethereum as a whole.



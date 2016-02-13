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

You can also purchase Ether on any exchange which supports the currency.  As 
of 2015-02-12 Poloniex was the exchange with the highest volume in Ethereum
transactions.

Ether may also be mined using your computer's graphics card (GPU). To be 
efficient the GPU should have a sufficient amount of memory, as it must hold 
and access the "DAG" efficiently. The DAG is a resource that is required by 
Ethash, the ASIC-resistant (i.e. memory-hard) proof of work algorithm used by 
Ethereum. The DAG is more than 1 GB in size.

1. To start mining on Windows, first download `Geth`_. Geth communicates with 
the Ethereum network to coordinate the mining process over all computers 
connected to the network. 
2. Unzip Geth (right-click and select unpack) and launch Command Prompt.
3. Use 'cd' to navigate to the location of the Geth folder.
e.g. 'cd /' to go to the C: drive. 
4. Now create a new geth account by typing 'geth account new'. Hit Enter.
5. You will be asked to enter a password.
Careful! You won't see the password when you type. Also, do not lose your 
password! Without it you will lose all Ether associated with the wallet held 
by that private key.
7. Now let's start Geth. Type 'geth --rpc'.
As soon as you enter this the Ethereum blockchain will start downloading. 
Sometimes your firewall may block the synchronisation process (it will prompt 
you when doing so). If this is the case, click "Allow access". 
8. Now it's time to download the actual mining software, `Ethminer`_. 
9. Install Ethminer (your firewall or Windows itself may act up, allow access)
10. Open up another Command Prompt (leave the first one running!) 
11. Type 'cd /' and hit Enter.
12. Type 'cd prog' and hit Tab. It will auto-complete to 'cd Program Files'.
Hit Enter.
13. Type 'cd eth' and hit Tab again. It will auto-complete to 'cd Ethereum(++)'.
A version number will follow after 'Ethereum(++)'. Hit Enter. 
14. Type 'cd release' and hit Enter. 
15. Now type 'ethminer -G' and hit Enter. This will start the mining process!
At this point some problems may appear. If you get an error press 'Ctrl' and 
'c' at the same time to shut down the process. If the error says 
"Insufficient Memory", your GPU does not have enough memory to mine Ether. 
You may want to get another graphics card or opt for CPU mining.
16. For CPU mining, type 'ethminer' and hit Enter. 

You can also use your computer's central processing unit (CPU) to mine ether 
on the testnet. This ether has no value outside of testing purposes. 

[Will point to mining and exchanges pages with explanation of both]

Sending Ether
================================================================================

The `Ethereum Wallet`_ supports sending ether via a graphical interface.

Ether can also be transfered using the **geth console**.

.. code-block:: shell

    > var sender = eth.accounts[0];
    > var receiver = eth.accounts[1];
    > var amount = web3.toWei(0.01, "ether")
    > eth.sendTransaction({from:sender, to:receiver, value: amount})



.. _Ethereum Wallet: https://github.com/ethereum/mist/releases/tag/0.3.9
.. _Geth: https://build.ethdev.com/builds/Windows%20Go%20master%20branch/
.. _Ethminer: http://cryptomining-blog.com/tag/ethminer-cuda-download/

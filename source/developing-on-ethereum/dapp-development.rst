********************************************************************************
DApp Development
********************************************************************************

Web3
================================================================================
TODO

Connecting to Morden Testnet
================================================================================

TODO

Setting Up a Local Private Testnet
================================================================================
You either pre-generate or mine your own Ether on a private
testnet. It is a much more cost effective way of trying out
Ethereum.

The things that are required to specify in a private chain are:
 - Custom Genesis File
 - Custom Data Directory
 - Custom NetworkID
 - (Recommended) Disable Node Discovery

The Genesis File
--------------------------------------------------------------------------------

The Genesis block is the start of the Blockchain - the first
block, block 0, and the only block that does not point to a predecessor
block. Ethereum’s client protocol ensures that no other node will agree with your version of the
blockchain unless they have the same genesis block, so you can make as many private testnet blockchains as you'd like!

CustomGensis.json

.. code-block:: JSON

  {     "nonce": "0x0000000000000042",     "timestamp": "0x0",     
  "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",     
  "extraData": "0x0",     "gasLimit": "0x8000000",     "difficulty": "0x400",     
  "mixhash": "0x0000000000000000000000000000000000000000000000000000000000000000",     
  "coinbase": "0x3333333333333333333333333333333333333333",     "alloc": {     } }

Save a file called CustomGenesis.json.
You will reference this when starting your geth node using the following flag:

``--genesis /path/to/CustomGenesis.json``

Geth Flags For Your Private Network
--------------------------------------------------------------------------------

There are some command line options (also called “flags”) that are
necessary in order to make sure that your network is private. We already covered the genesis flag, but we need a few more. 

``--nodiscover``

Use this to make sure that your node is not discoverable by people who do not manually add you. Otherwise, there is a chance that your node may be inadvertently added to a stranger's blockchain if they have the same genesis file and network id.

``--maxpeers 0``

Use maxpeers 0 if you do not want anyone else connecting to your test chain. Alternatively, you can adjust this number if you know exactly how many peers you want connecting to your node.

``--rpc``

This will enable RPC interface on your node. This is generally enabled by default in Geth.


``--rpcapi "db,eth,net,web3"``

This dictates what APIs that are allowed to be accessed over RPC. By default, Geth enables the web3 interface over RPC. 

**IMPORTANT: Please note that offering an API over the RPC/IPC interface will give everyone access to the API who can access this interface (e.g. DApp's). Be careful which API's you enable. By default geth enables all API's over the ipc interface and only the db,eth,net and web3 API's over the RPC interface.********************************************************************************


``--rpcport "8080"``

Change 8000 to any port that is open on your network. The default for geth is 8080.

``--rpccorsdomain "http://chriseth.github.io/browser-solidity/"``

This dictates what URLs can connect to your node in order to perform RPC client tasks. Be very careful with this put a specific URL rather than the wildcard (*) which would allow any URL to connect to your RPC instance. Since this is a private chain that will not hold real Ether, I usually put a wildcard so I can use sites such as [Browser Solidity](http://chriseth.github.io/browser-solidity/) for my testing.


``--datadir "/home/TestChain1"``

This is the data directory that your private chain data will be stored in. Choose a location that is separate from your public Ethereum chain folder.


``--port "30303"``

This is the "network listening port", which you will use to connect with other peers manually.


``--identity "TestnetMainNode"``

This will set up an identity for your node so it can be identified more easily in a list of peers.
Here is an example of how these identities show up on the network.


Creating the geth Command
--------------------------------------------------------------------------------

After you have created your custom genesis block JSON file and created a directory for your chain to go into, type the following command into your console that has access to geth:

.. code-block:: Bash

  geth --identity "MyNodeName" --genesis /path/to/CustomGenesis.json --rpc --rpcport "8080" --rpccorsdomain "*" --datadir "C:\chains\TestChain1" --port "30303" --nodiscover --rpcapi "db,eth,net,web3" --networkid 1999 console

You will need to start your geth instance with your custom chain command every time you want to access your custom chain. If you just type "geth" in your console, it will not remember all of the flags you have set. Different operating systems have ways to make this easier. Check out this page NEED LINK HERE for other geth console commands that may be applicable to your network set-up and situation.

Pre-Allocating Ether to Your Account
--------------------------------------------------------------------------------

A difficulty of "0x400" allows you to mine Ether very quickly on your private testnet chain. If you create your chain and start mining, you should have hundreds of Ether in a matter of minutes which is way more than enough to test transactions on your network. If you would still like to pre-allocate Ether to your account, you will need to:
1. Create a new Ethereum account after you create your private chain
2. Copy your new account address
3. Add the following command to your Custom_Genesis.json file:

.. code-block:: JSON

  "alloc":
  { 
	  "<your account address e.g. 0x1fb891f92eb557f4d688463d0d7c560552263b5a>":
	  { "balance": "20000000000000000000" } 
  }

Save your genesis file and re-run the command at the bottom of this guide to start your private chain in Geth. You are now in the Geth console. We want to assign an address as "primary" and check it's balance.

.. code-block:: Console

  > primary = eth.accounts[0];

This should return you your primary Ethereum address you created. If it does not, try settinfg primary to 1, 2, etc. until you find your address you created. Addrsses are assigned those array indexes in order of creation.

.. code-block:: Console

  > balance = web3.fromWei(eth.getBalance(primary), "ether");

This should return you ``20`` Ether in your account. The reason we had to put such a large number in the alloc section of your genesis file is because the "balance" field takes a number in wei which is the smallest sub-unit of Ether.

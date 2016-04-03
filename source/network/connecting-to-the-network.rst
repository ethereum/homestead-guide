.. _sec:connecting-to-the-network:

********************************************************************************
Connecting to the Network
********************************************************************************

This section

The Ethereum network
================================================================================

The basis for decentralised consensus is the peer-to-peer network of participating nodes which maintain and secure the blockchain. See :ref:`mining`.

Ethereum network stats
--------------------------------------------------

`EthStats\.net <https://ethstats.net/>`_ is a dashboard of live statistics of the Ethereum network. This dashboard displays important information such as the current block, hash difficulty, gas price, and gas spending. The nodes shown on the page are only a selection of actual nodes on the network.
Anyone is allowed to add their node to the EthStats dashboard. The `Eth\-Netstats README on Github <https://github.com/cubedro/eth-netstats>`_ describes how to connect.

`EtherNodes\.com <https://www.ethernodes.org/>`_ displays current and historical data on node count and other information on both the Ethereum mainnet and Morden testnet.

`Distribution of client implementations on the current live network <https://etherchain.org/nodes>`_ - Realtime stats on EtherChain.

Public, private, and consortium blockchains
------------------------------------------------

Most Ethereum projects today rely on Ethereum as a public blockchain, which grants access to a larger audience of users, network nodes, currency, and markets.  However, there are often reasons to prefer a private blockchain or consortium blockchain (among a group of trusted participants). For example, a number of companies in verticals, like banking, are looking to Ethereum as a platform for their own private blockchains.

Below is an excerpt from the blog post `On Public and Private Blockchains <https://blog.ethereum.org/2015/08/07/on-public-and-private-blockchains/>`_ that explains the difference between the three types of blockchains based on permissioning:

- **Public blockchains**: a public blockchain is a blockchain that anyone in the world can read, anyone in the world can send transactions to and expect to see them included if they are valid, and anyone in the world can participate in the consensus process – the process for determining what blocks get added to the chain and what the current state is. As a substitute for centralized or quasi-centralized trust, public blockchains are secured by cryptoeconomics – the combination of economic incentives and cryptographic verification using mechanisms such as proof of work or proof of stake, following a general principle that the degree to which someone can have an influence in the consensus process is proportional to the quantity of economic resources that they can bring to bear. These blockchains are generally considered to be “fully decentralized”.

- **Consortium blockchains**: a consortium blockchain is a blockchain where the consensus process is controlled by a pre-selected set of nodes; for example, one might imagine a consortium of 15 financial institutions, each of which operates a node and of which 10 must sign every block in order for the block to be valid. The right to read the blockchain may be public, or restricted to the participants, and there are also hybrid routes such as the root hashes of the blocks being public together with an API that allows members of the public to make a limited number of queries and get back cryptographic proofs of some parts of the blockchain state. These blockchains may be considered “partially decentralized”.

- **Private blockchains**: a fully private blockchain is a blockchain where write permissions are kept centralized to one organization. Read permissions may be public or restricted to an arbitrary extent. Likely applications include database management, auditing, etc internal to a single company, and so public readability may not be necessary in many cases at all, though in other cases public auditability is desired.

While these private/consortium blockchains may not have any connection to the public blockchain, they still contribute to the overall Ethereum ecosystem by investing in Ethereum software development. Over time, this translates into software improvements, shared knowledge, and job opportunities.


How to connect
================================================================================

Geth continuously attempts to connect to other nodes on the network until it has peers. If you have UPnP enabled on your router or run Ethereum on an Internet-facing server, it will also accept connections from other nodes.

Geth finds peers through something called the *discovery protocol*. In the discovery protocol, nodes are gossipping with each other to find out about other nodes on the network. In order to get going initially, geth uses a set of bootstrap nodes whose endpoints are recorded in the source code.

Checking connectivity and ENODE IDs
--------------------------------------------------------------------------------

To check how many peers the client is connected to in the interactive console, the ``net`` module has two attributes that give you info about the number of peers and whether you are a listening node.

.. code-block:: Javascript

  > net.listening
  true

  > net.peerCount
  4

To get more information about the connected peers, such as IP address and port number, supported protocols, use the ``peers()`` function of the ``admin`` object. ``admin.peers()`` returns the list of currently connected peers.

.. code-block:: Javascript

  > admin.peers
  [{
  	ID: 'a4de274d3a159e10c2c9a68c326511236381b84c9ec52e72ad732eb0b2b1a2277938f78593cdbe734e6002bf23114d434a085d260514ab336d4acdc312db671b',
  	Name: 'Geth/v0.9.14/linux/go1.4.2',
  	Caps: 'eth/60',
  	RemoteAddress: '5.9.150.40:30301',
  	LocalAddress: '192.168.0.28:39219'
   }, {
  	ID: 'a979fb575495b8d6db44f750317d0f4622bf4c2aa3365d6af7c284339968eef29b69ad0dce72a4d8db5ebb4968de0e3bec910127f134779fbcb0cb6d3331163c',
  	Name: 'Geth/v0.9.15/linux/go1.4.2',
  	Caps: 'eth/60',
  	RemoteAddress: '52.16.188.185:30303',
  	LocalAddress: '192.168.0.28:50995'
   }, {
  	ID: 'f6ba1f1d9241d48138136ccf5baa6c2c8b008435a1c2bd009ca52fb8edbbc991eba36376beaee9d45f16d5dcbf2ed0bc23006c505d57ffcf70921bd94aa7a172',
  	Name: 'pyethapp_dd52/v0.9.13/linux2/py2.7.9',
  	Caps: 'eth/60, p2p/3',
  	RemoteAddress: '144.76.62.101:30303',
  	LocalAddress: '192.168.0.28:40454'
   }, {
    ID: 'f4642fa65af50cfdea8fa7414a5def7bb7991478b768e296f5e4a54e8b995de102e0ceae2e826f293c481b5325f89be6d207b003382e18a8ecba66fbaf6416c0',
    Name: '++eth/Zeppelin/Rascal/v0.9.14/Release/Darwin/clang/int',
    Caps: 'eth/60, shh/2',
    RemoteAddress: '129.16.191.64:30303',
    LocalAddress: '192.168.0.28:39705'
   } ]


To check the ports used by geth and also find your enode URI run:

.. code-block:: Javascript

  > admin.nodeInfo
  {
    Name: 'Geth/v0.9.14/darwin/go1.4.2',
    NodeUrl: 'enode://3414c01c19aa75a34f2dbd2f8d0898dc79d6b219ad77f8155abf1a287ce2ba60f14998a3a98c0cf14915eabfdacf914a92b27a01769de18fa2d049dbf4c17694@[::]:30303',
    NodeID: '3414c01c19aa75a34f2dbd2f8d0898dc79d6b219ad77f8155abf1a287ce2ba60f14998a3a98c0cf14915eabfdacf914a92b27a01769de18fa2d049dbf4c17694',
    IP: '::',
    DiscPort: 30303,
    TCPPort: 30303,
    Td: '2044952618444',
    ListenAddr: '[::]:30303'
  }

Download the blockchain faster
================================================================================

When you start an Ethereum client, the Ethereum blockchain is automatically downloaded. The time it takes to download the Ethereum blockchain can vary based on client, client settings, connection speed, and number of peers available. Below are some options for more quickly obtaining the Ethereum blockchain.

Using geth
--------------------------------------------------------------------------------

If you are using the geth client, there are some things you can do to speed up the time it takes to download the Ethereum blockchain. If you choose to use the ``--fast`` flag to perform an Ethereum fast sync, you will not retain past transaction data.

.. note:: You cannot use this flag after performing all or part of a normal sync operation, meaning you should not have any portion of the Ethereum blockchain downloaded before using this command. `See this Ethereum Stack\.Exchange answer for more information <http://ethereum.stackexchange.com/questions/1845/why-isnt-fast-sync-the-default>`_.

Below are some flags to use when you want to sync your client more quickly.

``--fast``

This flag enables fast syncing through state downloads rather than downloading the full block data. This will also reduce the size of your blockchain dramatically.
NOTE: ``--fast`` can only be run if you are syncing your blockchain from scratch and only the first time you download the blockchain for security reasons. `See this Reddit post for more information <https://www.reddit.com/r/ethereum/comments/3y9316/geth_fast_option_question/>`_.

``--cache=1024``

Megabytes of memory allocated to internal caching (min 16MB / database forced). Default is 16MB, so increasing this to 256, 512, 1024 (1GB), or 2048 (2GB) depending on how much RAM your computer has should make a difference.

``--jitvm``

This flag enables the JIT VM.

Full example command with console:

.. code-block:: Bash

  geth --fast --cache=1024 --jitvm console

For more discussion on fast syncing and blockchain download times, `see this Reddit post <https://www.reddit.com/r/ethereum/comments/46c4ga/lets_benchmark_the_clients/>`_.

Exporting/Importing the blockchain
--------------------------------------------------------------------------------

If you already have a full Ethereum node synced, you can export the blockchain data from the fully synced node and import it into your new node. You can accomplish this in geth by exporting your full node with the command ``geth export filename`` and importing the blockchain into your node using ``geth import filename``.
see `this link <staticnodes>`_

..  _cr-static-nodes:

Static Nodes, Trusted Nodes, and Boot Nodes
================================================================================

Geth supports a feature called static nodes if you have certain peers you always want to connect to. Static nodes are re-connected on disconnects. You can configure permanent static nodes by putting something like the following into ``<datadir>/static-nodes.json`` (this should be the same folder that your ``chaindata`` and ``keystore`` folders are in)

.. code-block:: Javascript

  [
  	"enode://f4642fa65af50cfdea8fa7414a5def7bb7991478b768e296f5e4a54e8b995de102e0ceae2e826f293c481b5325f89be6d207b003382e18a8ecba66fbaf6416c0@33.4.2.1:30303",
  	"enode://pubkey@ip:port"
  ]

You can also add static nodes at runtime via the Javascript console using ``admin.addPeer()``

.. code-block:: Console

  > admin.addPeer("enode://f4642fa65af50cfdea8fa7414a5def7bb7991478b768e296f5e4a54e8b995de102e0ceae2e826f293c481b5325f89be6d207b003382e18a8ecba66fbaf6416c0@33.4.2.1:30303")

Common problems with connectivity
--------------------------------------------------------------------------------

Sometimes you just can't get connected. The most common reasons are:

* Your local time might be incorrect. An accurate clock is required to participate in the Ethereum network. Check your OS for how to resync your clock (example ``sudo ntpdate -s time.nist.gov``) because even 12 seconds too fast can lead to 0 peers.
* Some firewall configurations can prevent UDP traffic from flowing. You can use the static nodes feature or ``admin.addPeer()`` on the console to configure connections by hand.

To start geth without the discovery protocol, you can use the ``--nodiscover`` parameter. You only want this if you are running a test node or an experimental test network with fixed nodes.

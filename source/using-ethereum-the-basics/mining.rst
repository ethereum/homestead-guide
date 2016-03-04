.. _mining:

********************************************************************************
Mining
********************************************************************************


Introduction
================================================================================

The word mining originates in the context of the gold analogy for crypto currencies. Gold or precious metals are scarce, so are digital tokens, and the only way to increase the total volume is through mining it. This is appropriate to the extent that in Ethereum too, the only mode of issuance post launch is via the mining. Unlike these examples however, mining is also the way to secure the network by creating, verifying, publishing and propagating blocks in the blockchain.

- Mining Ether = Securing the network = verify computation

So What is Mining Anyway?
--------------------------------------------------------------------------------

Ethereum, like all blockchain technologies, uses an incentive-driven model of security. Consensus is based on choosing the block with the highest total difficulty. Miners produce blocks which the others check for validity. Among other well-formedness criteria, a block is only valid if it contains **proof of work** (PoW) of a given **difficulty**. Note that in the Ethereum Serenity milestone, this is likely going to be replaced by a **proof of stake** model.

The Ethereum blockchain is in many ways similar to the Bitcoin blockchain, although it does have some differences. The main difference between Ethereum and Bitcoin with regard to the blockchain architecture is that, unlike Bitcoin, Ethereum blocks contain a copy of both the transaction list and the most recent state. Aside from that, two other values, the block number and the difficulty, are also stored in the block.

The proof of work algorithm used is called
`Ethash <https://github.com/ethereum/wiki/wiki/Ethash>`__ (a modified version of `Dagger-Hashimoto <https://github.com/ethereum/wiki/wiki/Dagger-Hashimoto>`)__ and involves finding a nonce input to the algorithm so that the result is below a certain threshold depending on the difficulty. The point in PoW algorithms is that there is no better strategy to find such a nonce than enumerating the possibilities while verification of a solution is trivial and cheap. If outputs have a uniform distribution, then we can guarantee that on average the time needed to find a nonce depends on the difficulty threshold, making it possible to control the time of finding a new block just by manipulating difficulty.

The difficulty dynamically adjusts so that on average one block is
produced by the entire network every 12 seconds (ie., 12 s block time).
This heartbeat basically punctuates the synchronisation of system state
and guarantees that maintaining a fork (to allow double spend) or
rewriting history is impossible unless the attacker possesses more than
half of the network mining power (so called 51% attack).

Any node participating in the network can be a miner and their expected
revenue from mining will be directly proportional to their (relative)
mining power or **hashrate**, ie., number of nonces tried per second
normalised by the total hashrate of the network.

Ethash PoW is memory hard, making it basically ASIC resistant. This
basically means that calculating the PoW requires choosing subsets of a
fixed resource dependent on the nonce and block header. This resource (a
few gigabyte size data) is called a **DAG**. The
`DAG <https://github.com/ethereum/wiki/wiki/Ethash-DAG>`__ is totally
different every 30000 blocks (a 100 hour window, called an **epoch**)
and takes a while to generate. Since the DAG only depends on block
height, it can be pregenerated but if its not, the client need to wait
the end of this process to produce a block. Until clients actually
precache dags ahead of time the network may experience a massive block
delay on each epoch transition. Note that the DAG does not need to be
generated for verifying the PoW essentially allowing for verification
with both low CPU and small memory.

As a special case, when you start up your node from scratch, mining will
only start once the DAG is built for the current epoch.

Mining Rewards
--------------------------------------------------------------------------------

Note that mining 'real' Ether will start with the Frontier release. On
the Olympics testnet, the `Frontier
pre-release <http://ethereum.gitbooks.io/frontier-guide/>`__, the ether
mined have no value (but see `Olympic
rewards <https://blog.ethereum.org/2015/05/09/olympic-frontier-pre-release/>`__).

The successful PoW miner of the winning block receives:

* a **static block reward** for the 'winning' block, consisting of exactly 5.0 Ether
* cost of the gas expended within the block, its ether amount depends on the gas price
* an extra reward for including uncles as part of the block, in the form of an extra 1/32 per uncle included

All the gas consumed by the execution of all the transactions in the block submitted
by the winning miner is compensated for by the senders. The gas cost
incurred is credited to the miner's account as part of the consensus
protocol. Over time, it's expected these will dwarf the static block
reward.

Uncles are stale blocks i.e. with parents that are ancestors (max 6 blocks
back) of the including block. Valid uncles are rewarded in order to
neutralise the effect of network lag on the dispersion of mining
rewards, thereby increasing security. Uncles included in a block formed
by the successful PoW miner receive 7/8 of the static block reward (=4.375 ether)
A maximum of 2 uncles are allowed per block.

Ethash DAG
--------------------------------------------------------------------------------

Ethash uses a **DAG** (directed acyclic graph) for the proof of work
algorithm, this is generated for each **epoch**, i.e every 30000 blocks
(100 hours). The DAG takes a long time to generate. If clients only
generate it on demand, you may see a long wait at each epoch transition
before the first block of the new epoch is found. However, the DAG only
depends on block number, so it CAN and SHOULD be calculated in advance
to avoid long wait at each epoch transition. ``geth`` implements
automatic DAG generation and maintains two DAGS at a time for smooth
epoch transitions. Automatic DAG generation is turned on and off when
mining is controlled from the console. It is also turned on by default
if ``geth`` is launched with the ``--mine`` option. Note that clients
share a DAG resource, so if you are running multiple instances of any
client, make sure automatic dag generation is switched on in at most one
client.

To generate the DAG for an arbitrary epoch:

::

    geth makedag <block number> <outputdir>

For instance ``geth makedag 360000 ~/.ethash``. Note that ethash uses
``~/.ethash`` (Mac/Linux) or ``~/AppData/Ethash`` (Windows) for the DAG
so that it can shared between clients.

The Algorithm
================================================================================

Our algorithm, `Ethash <https://github.com/ethereum/wiki/wiki/Ethash>`__
(previously known as Dagger-Hashimoto), is based around the provision of
a large, transient, randomly generated dataset which forms a DAG (the
Dagger-part), and attempting to solve a particular constraint on it,
partly determined through a block's header-hash.

It is designed to hash a fast verifiability time within a slow CPU-only
environment, yet provide vast speed-ups for mining when provided with a
large amount of memory with high-bandwidth. The large memory
requirements mean that large-scale miners get comparatively little
super-linear benefit. The high bandwidth requirement means that a
speed-up from piling on many super-fast processing units sharing the
same memory gives little benefit over a single unit.

JSON-RPC
--------------------------------------------------------------------------------

Communication between the external mining application and the Ethereum
daemon for work provision and submission happens through the JSON-RPC
API. Two RPC functions are provided; ``eth_getWork`` and
``eth_submitWork``.

These are formally documented on the `JSON-RPC
API <https://github.com/ethereum/wiki/wiki/JSON-RPC>`_ wiki article.

Mining Preliminaries
======================

In order to do mining, you need an ether account. This account is used to send the mining rewards to and is often referred to as 'coinbase' or 'etherbase'.
So on any platform, any implementation, you first need to `create a new geth account`. Using ``geth`` you simply type ``geth account new`` and hit Enter.
You will be asked to enter a password. Careful! You won't see the password when you type. Also, do not lose your password! Without it you will lose all Ether associated with the account.


Mining rewards
========================

https://forum.ethereum.org/discussion/2262/eli5-whats-an-uncle-in-ethereum-mining
`Mining difficulty chart on etherscan <http://etherscan.io/charts/difficulty>`_

CPU Mining
================================================================================

You can use your computer's central processing unit (CPU) to mine ether.
This is no longer profitable, since GPU miners are roughly two orders of magnitude more efficient.
However, you can use CPU mining to mine of the testnet or a private chain for the purposes of creating ether to test contracts and transactions without spending your real ether on the live network.
Note that ether (sourced from faucet or earned via mining) has no value other than using it for testing purposes. It is most unlikely there will ever be a proper market for testnet ether.



GPU Mining
================================================================================

GPU Mining on Windows
-------------------------------

To start mining on Windows, first download `Geth`_. Geth communicates with
the Ethereum network to coordinate the mining process over all computers
connected to the network.

Unzip Geth (right-click and select unpack) and launch Command Prompt.
Use 'cd' to navigate to the location of the Geth folder.
e.g. 'cd /' to go to the C: drive.

Start geth by typing ``geth --rpc``.

As soon as you enter this the Ethereum blockchain will start downloading.
Sometimes your firewall may block the synchronisation process (it will prompt
you when doing so). If this is the case, click "Allow access".

Download and install the C++ mining software, `Ethminer`_.
(your firewall or Windows itself may act up, allow access)

Open up another Command Prompt (leave the first one running!), change directory by typing ``cd /Program\ Files/Ethereum(++)/release``

Now make sure `geth` has finished syncing the blockchain by.
If it is not syncing any longer, you can  start the mining process by typing
``ethminer -G`` at the command prompt
At this point some problems may appear. If you get an error, you can abort the miner by pressing 'Ctrl+C'. If the error says
"Insufficient Memory", your GPU does not have enough memory to mine Ether.


* http://cryptomining-blog.com/5323-quick-guide-on-how-to-mine-ethereum-on-windows/
*

GPU Mining on Ubuntu linux
-----------------------------

* `Spacience blogpost <http://spacience.blogspot.sg/2015/11/gpu-mining-in-ethereum-1404-from-scratch.html>`_


Pool Mining
================================================================================

Mining pools are cooperatives that aims to smooth out expected revenue by pooling resources, submit blocks with proof of work found by the pool participants from a central account and redistribute the reward to participants in proportion to their contributed mining power. Unlike in Bitcoin, the benefit of pooling is minimal due to the very short blocktime.

_`Mining Pools` lists the pools we know of.

Note that most mining pools involve third party central components which means they are not trustless. In other worlds, pool operators can run away with your earnings. Act with caution.

There are a number of trustless, decentralised pools with open source codebase.
We recommend using those.

Mining pools only outsource proof of work calculation, they do not validate blocks or run the VM to check state transitions brought about by executing the transactions.
This effectively make pools behave like single nodes in terms of security, so their growing big poses a centralisation risk of a 51% attack. Make sure you follow the network capacity distribution and do not allow pools to grow big.

Mining profitability calculators:
  * `in the ether <http://ethereum-mining-calculator.com/>`_


.. _Geth: https://build.ethdev.com/builds/Windows%20Go%20master%20branch/
.. _Ethminer: http://cryptomining-blog.com/tag/ethminer-cuda-download/

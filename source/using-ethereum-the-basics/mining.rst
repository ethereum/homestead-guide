.. _mining:

********************************************************************************
Mining
********************************************************************************


Introduction
================================================================================

The word mining originates in the context of the gold analogy for crypto currencies. Gold or precious metals are scarce, so are digital tokens, and the only way to increase the total volume is through mining. This is appropriate to the extent that in Ethereum too, the only mode of issuance post launch is via mining. Unlike these examples however, mining is also the way to secure the network by creating, verifying, publishing and propagating blocks in the blockchain.

- mining Ether = securing the network = verify computation

So what is mining anyway?
--------------------------------------------------------------------------------

Ethereum, like all blockchain technologies, uses an incentive-driven model of security. Consensus is based on choosing the block with the highest total difficulty. Miners produce blocks which the others check for validity. Among other well-formedness criteria, a block is only valid if it contains *proof of work* (PoW) of a given *difficulty*. Note that in the Ethereum Serenity milestone, this is likely going to be replaced by a *proof of stake* (PoS) model (see _`Proof of stake`).

The Ethereum blockchain is in many ways similar to the Bitcoin blockchain, although it does have some differences. The main difference between Ethereum and Bitcoin with regard to the blockchain architecture is that, unlike Bitcoin, Ethereum blocks contain a copy of both the transaction list and the most recent state (the root hash of the merkle patricia trie encoding the state to be more precise). Aside from that, two other values, the block number and the difficulty, are also stored in the block.

The proof of work algorithm used is called `Ethash <https://github.com/ethereum/wiki/wiki/Ethash>`_ (a modified version of `the Dagger-Hashimoto algorithm <https://github.com/ethereum/wiki/wiki/Dagger-Hashimoto>`_) and involves finding a *nonce* input to the algorithm so that the result is below a certain difficulty threshold. The point in PoW algorithms is that there is no better strategy to find such a nonce than enumerating the possibilities, while verification of a solution is trivial and cheap. Since outputs have a uniform distribution (as they are the result of the application of a hash function), we can guarantee that, on average, the time needed to find such a nonce depends on the difficulty threshold. This makes it possible to control the time of finding a new block just by manipulating the difficulty.

As dictated by the protocol, the difficulty dynamically adjusts in such a way that on average one block is produced by the entire network every 15 seconds. We say that the network produces a blockchain with a *15 second block time*.
This "heartbeat" basically punctuates the synchronisation of system state
and guarantees that maintaining a fork (to allow double spend) or
rewriting history by malicious actors are impossible unless the attacker possesses more than half of the network mining power (this is the so called *51% attack*).

Any node participating in the network can be a miner and their expected
revenue from mining will be directly proportional to their (relative)
mining power or *hashrate*, i.e., the number of nonces tried per second
normalised by the total hashrate of the network.

Ethash PoW is *memory hard*, making it *ASIC resistant*. Memory hardness is achieved with a proof of work algorithm that requires choosing subsets of a
fixed resource dependent on the nonce and block header. This resource (a
few gigabyte size data) is called a **DAG**. The
`DAG <https://github.com/ethereum/wiki/wiki/Ethash-DAG>`_ is totally
different every 30000 blocks, a 125-hour window called *epoch* (roughly 5.2 days)
and takes a while to generate. Since the DAG only depends on block
height, it can be pregenerated but if its not, the client needs to wait
the end of this process to produce a block. If clients do not
pregenerate and cache dags ahead of time the network may experience massive block
delay on each epoch transition. Note that the DAG does not need to be
generated for verifying the PoW essentially allowing for verification
with both low CPU and small memory.

As a special case, when you start up your node from scratch, mining will
only start once the DAG is built for the current epoch.


Mining rewards
--------------------------------------------------------------------------------

The successful PoW miner of the winning block receives:

* a *static block reward* for the 'winning' block, consisting of exactly 5.0 Ether
* cost of the gas expended within the block – an amount of ether that depends on the current gas price
* an extra reward for including uncles as part of the block, in the form of an extra 1/32 per uncle included

All the gas consumed by the execution of all the transactions in the block submitted
by the winning miner is paid by the senders of each transaction. The gas cost
incurred is credited to the miner's account as part of the consensus
protocol. Over time, it is expected these will dwarf the static block
reward.

*Uncles* are stale blocks i.e. with parents that are ancestors (max 6 blocks
back) of the including block. Valid uncles are rewarded in order to
neutralise the effect of network lag on the dispersion of mining
rewards, thereby increasing security (this is called the GHOST protocol).
Uncles included in a block formed by the successful PoW miner receive 7/8 of the static block reward (=4.375 ether). A maximum of 2 uncles are allowed per block.

Ethash DAG
--------------------------------------------------------------------------------

Ethash uses a *DAG* (directed acyclic graph) for the proof of work
algorithm, this is generated for each *epoch*, i.e., every 30000 blocks
(125 hours, ca. 5.2 days). The DAG takes a long time to generate. If clients only
generate it on demand, you may see a long wait at each epoch transition
before the first block of the new epoch is found. However, the DAG only
depends on block number, so it can and should be calculated in advance
to avoid long wait times at each epoch transition. Both ``geth`` and ``ethminer``implement automatic DAG generation and maintains two DAGS at a time for smooth
epoch transitions. Automatic DAG generation is turned on and off when
mining is controlled from the console. It is also turned on by default
if ``geth`` is launched with the ``--mine`` option. Note that clients
share a DAG resource, so if you are running multiple instances of any
client, make sure automatic dag generation is switched off in all but one instance.

To generate the DAG for an arbitrary epoch:

::

    geth makedag <block number> <outputdir>

For instance ``geth makedag 360000 ~/.ethash``. Note that ethash uses
``~/.ethash`` (Mac/Linux) or ``~/AppData/Ethash`` (Windows) for the DAG
so that it can shared between different client implementations as well as multiple running instances.

The algorithm
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
same memory gives little benefit over a single unit. This is important in that
pool mining have no benefit for nodes doing verification, thus discourageing centralisation.

JSON-RPC
--------------------------------------------------------------------------------

Communication between the external mining application and the Ethereum
daemon for work provision and submission happens through the JSON-RPC
API. Two RPC functions are provided; ``eth_getWork`` and
``eth_submitWork``.

These are formally documented on the `JSON-RPC API <https://github.com/ethereum/wiki/wiki/JSON-RPC>`_ wiki article.

Mining preliminaries
======================

In order to do mining, you need an ether account. This account is used to send the mining rewards to and is often referred to as *coinbase* or *etherbase*.
So on any platform, any implementation, you first need to create a new account. Using ``geth`` you simply type ``geth account new`` and hit Enter.
You will be asked to enter a password. Careful! You won't see the password when you type. Also, do not lose your password! Without it you will lose all ether associated with the account.

Resources:

* `Forum thread explaining uncles <https://forum.ethereum.org/discussion/2262/eli5-whats-an-uncle-in-ethereum-mining>`_
* `Mining difficulty chart on etherscan <http://etherscan.io/charts/difficulty>`_

CPU mining
================================================================================

You can use your computer's central processing unit (CPU) to mine ether.
This is no longer profitable, since GPU miners are roughly two orders of magnitude more efficient.
However, you can use CPU mining to mine on the testnet or a private chain for the purposes of creating the ether you need to test contracts and transactions without spending your real ether on the live network.
Note that ether (sourced from a *faucet* or earned via mining) has no value other than using it for testing purposes. It is most unlikely there will ever be a proper market for testnet ether.

GPU mining
================================================================================

GPU mining on windows
-------------------------------

To start mining on Windows, first `download the geth windows binary <https://build.ethdev.com/builds/Windows%20Go%20master%20branch/>`_. Geth communicates with
the Ethereum network to coordinate the mining process over all computers
connected to the network.

* Unzip Geth (right-click and select unpack) and launch Command Prompt. Use `cd` to navigate to the location of the Geth data folder. (e.g. ``cd /`` to go to the ``C:`` drive)
* Start geth by typing ``geth --rpc``.

As soon as you enter this, the Ethereum blockchain will start downloading.
Sometimes your firewall may block the synchronisation process (it will prompt
you when doing so). If this is the case, click "Allow access".

* First `download and install ethminer <http://cryptomining-blog.com/tag/ethminer-cuda-download/>`_, the C++ mining software (your firewall or Windows itself may act up, allow access)
* Open up another Command Prompt (leave the first one running!), change directory by typing ``cd /Program\ Files/Ethereum(++)/release``
* Now make sure `geth` has finished syncing the blockchain. If it is not syncing any longer, you can  start the mining process by typing ``ethminer -G`` at the command prompt

At this point some problems may appear. If you get an error, you can abort the miner by pressing ``Ctrl+C``. If the error says
"Insufficient Memory", your GPU does not have enough memory to mine ether.

Resources:

* `Quick guide on ethereum GPU mining on windows <http://cryptomining-blog.com/5323-quick-guide-on-how-to-mine-ethereum-on-windows/>`_ -  cryptomining blogpost


GPU mining on Ubuntu linux
-----------------------------

Resources:

* `GPU mining on Ubuntu <http://spacience.blogspot.sg/2015/11/gpu-mining-in-ethereum-1404-from-scratch.html>`_ - Spacience blogpost


Pool mining
================================================================================

Mining pools are cooperatives that aim to smooth out expected revenue by pooling the mining power of participating miners. The mining pool submits blocks with proof of work from a central account and redistributes the reward to participants in proportion to their contributed mining power. _`Mining Pools` lists the pools we know of.

.. note:: Unlike in Bitcoin, *the benefit of pooling is minimal* due to the very short blocktime and the GHOST protocol.

.. warning::  Most mining pools involve third party, central components which means they are not trustless. In other words, pool operators can run away with your earnings. Act with caution. There are a number of trustless, decentralised pools with open source codebase. We recommend using those.

.. warning:: Mining pools only outsource proof of work calculation, they do not validate blocks or run the VM to check state transitions brought about by executing the transactions. This effectively make pools behave like single nodes in terms of security, so their growth poses a centralisation risk of a 51% attack. Make sure you follow the network capacity distribution and do not allow pools to grow too large.

Mining pools
--------------------------------------------------------------------

* `coinotron`_
* `nanopool`_
* `ethpool`_ - Predictable solo mining, unconventional payout scheme, affiliated with `etherchain\.org`_.
* `supernova`_
* `coinmine.pl`_
* `eth.pp.ua`_
* `talkether`_ - Unconventional payout scheme
* `weipool`_
* `ethereumpool`_
* `pooleum`_
* `alphapool`_
* `dwarfpool`_
* `laintimes <http://pool.laintimes.com/>`_ - Discontinued

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
.. _etherchain.org: https://etherchain.org/


Mining resources
--------------------------------------------------------------------------------

* `Top miners of last 24h on etherchain <https://etherchain.org/statistics/miners>`_
* `pool hashrate distribution for august 2015 <ehttp://cryptomining-blog.com/5607-the-current-state-of-ethereum-mining-pools/>`_
* `Unmaintained list of pools on Forum <https://forum.ethereum.org/discussion/3659/list-of-pools>`_
* `Mining profitability calculator by cryptowizzard <http://cryptowizzard.github.io/eth-mining-calculator/>`_
* `Mining profitability calculator on etherscan <http://etherscan.io/ether-mining-calculator/>`_
* `Mining profitability calculator in the ether <http://ethereum-mining-calculator.com/>`_

technical notes to the go-ethereum blockchain synchronisation module

Intro
-----

An Ethereum node needs to acquire the set of blocks from which the
current consensus can be proved. This includes scenarios where the node
starts up from scratch (i.e., with an empty database) in which case the
block pool acts as a *download manager* as well as normal operation
where the node needs to synchronize recent blocks by finding the best
candidate new blocks. Since network latency and disruption can cause any
amount of blocks to be missed the two scenarios can be considered the
same task: finding the best chain to give to the blockchain manager.

**Goal**: The Blockpool needs to find the best chain to be inserted in
the blockchain.

In order the achieve this, the blockpool can only rely on p2p
communication using the `Ethereum wire
protocol <https://github.com/ethereum/wiki/wiki/Ethereum-Wire-Protocol>`__.

Terminology
-----------

The blockchain database is a tree structure with exactly one root, the
*genesis block* and contains at least one leaf node. The consensus
protocol specifies that the block with the highest *total difficulty* is
the consensus state. The total difficulty of a block is always strictly
higher than that of its parent, so a consensus state is always a leaf
node. The current known best block is also called the *head block* of
the node. When the node is starting up the first time with an empty
database, the head block is the genesis block itself.

A *chain* is any sequence of blocks connecting a root with a leaf node.
The leaf node with the highest total difficulty is the head of the block
chain which specifies the consensus state of the network. The chain
connecting the genesis block with the head is the *canonical chain*.

A sequence of blocks or block hashes that form a contiguous subsequence
of a chain is called a *section*. The youngest section of blocks headed
by the peer's current head is called the peer's *head section*.

If there are two different blocks with the same parent, the chain has a
*fork*. Those blocks which do not end up on the canonical chain are
called *stale* blocks, a sequence of such blocks is a *stale section*.

The Blockpool stores a pool of blocks which have not been processed yet,
thus it acts as a queue or processing buffer for the blockchain manager.
Therefore the notions of chain, fork, section, etc. carry over to
sequences of blocks and blockhashes in the blockpool.

Interface with network protocol and peers
-----------------------------------------

As a proper decentralised consensus system, Ethereum relies only on
other peers to synchronise. The `eth wire
protocol <https://github.com/ethereum/wiki/wiki/Ethereum-Wire-Protocol>`__
defines the messages that the blockpool can use to communicate. For a
naive new node, the only entry point to the blockchain is the head block
advertised by a peer as part of their status message (``StatusMsg``,
i.e., protocol handshake) or when a ``NewBlockMsg`` is received from a
miner. A sequence of block hashes can be requested and received with
``getBlockHashesMsg``/``BlockHashesMsg`` message pair. A set of blocks
can be requested and received with ``getBlocksMsg``/``BlocksMsg``
message pair.

Although the exact way synchronisation is done is not specified by
either the wire protocol or the block chain consensus protocol, the
messages provided restrict the synchronisation process:

**Synchronisation**: proceeds from head to known block by requesting and
fetching block hashes iteratively from young to old (head to root).
Based on block hashes, blocks can be requested. Based on the parenthash
of a block, independent sections can be linked and a chain established.
By checking if a block is found in the block chain the root of the
blockpool can be established and the chain can be inserted in the
blockchain.

We will elaborate on how exactly this is done below.

Our implementation currently provide 4 entry points to the blockpool for
the ``eth`` protocol instances running on each peer. These get called
when a message relevant to blockchain synchronisation is received from
the peer.

Adding and removing a peer
~~~~~~~~~~~~~~~~~~~~~~~~~~

```AddPeer`` <https://github.com/ethereum/go-ethereum/blob/develop/blockpool/blockpool.go#L262>`__
is `called by the ``eth``
protocol <https://github.com/ethereum/go-ethereum/blob/develop/eth/protocol.go#L342>`__
right after receiving the `*status message* <>`__ (or protocol
handshake) from a peer. The blockpool registers the peer with
information about its total difficulty and current head block. It also
registers *peer callbacks* so that the blockpool can send requests
directly to a peer (``requestBlockHashes`` and ``requestBlocks``) and
report a peer error (``peerError``).

Once a peer is removed (disconnect or eviction), the `protocol calls
back <https://github.com/ethereum/go-ethereum/blob/develop/eth/protocol.go#L138>`__
to the BlockPool to unregister the peer with
```RemovePeer`` <https://github.com/ethereum/go-ethereum/blob/develop/blockpool/blockpool.go#L276>`__.

The blockpool synchronisation relies on choosing the *best peer* out of
the connected peers. The best peer is defined as the peer with the
highest advertised total difficulty that is ahead of us. The blockpool
works by following and replicating the best peer's canonical chain.

**Strategy**: follow the best peer and replicate its canonical chain.

In our architecture the Blockpool controls peer selection only
indirectly. If a peer violates a blockpool policy, the blockpool reports
it as a peer error. If the error is fatal, the peer is disconnected and
suspended for ``PeerSuspensionInterval``. Synchronisation therefore
crucially relies on a healthy network (i.e., connectivity as well as
efficient message relaying).

Choosing the best peer
^^^^^^^^^^^^^^^^^^^^^^

Every time a peer is registered, its total difficulty is checked against
the best peer. If it is higher, the peer is *promoted as best peer*.
Every time the best peer disconnects, a new "second best" peer is
promoted. Surely this is limited to peers that are ahead of us, i.e.,
ones with advertised total difficulty strictly greater than ours.

Since our own total difficulty can change when mining, the blockpool
needs to receive updates of the last total difficulty. This is achieved
by subscribing to ``ChainHeadEvent`` posted in the blockchain manager. A
blockpool update routine is listening to these total difficulty updates
and if it finds that our own total difficulty goes above that of the
best peer, the peer is demoted (our own node becomes the best peer as it
were). Note that because of forks it is not sufficient to check if we
already have the head block of a peer.

Adding and updating peer info
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The total difficulty determining best peer status is communicated in one
of the following 4 ways:

-  when a peer is connected, the ``eth`` protocol receives its status
   message that contains the total difficulty of the peer as well as its
   current block hash. If this total difficulty is higher than that of
   self and other peers, a peer switch happens: the new peer is promoted
   best peer, the current best peer (if there was one) is demoted.
-  when `a new block message
   arrives <https://github.com/ethereum/go-ethereum/blob/develop/eth/protocol.go#L253>`__,
   it contains the new total difficulty, as well as the head block
   (including its header hash). To allow for the update of peers head
   info and a potential peer switch, the `protocol calls
   ``AddPeer`` <https://github.com/ethereum/go-ethereum/blob/develop/blockpool/blockpool.go#L549>`__.
   In the special case when a new block message arrives from the best
   peer, its head information is updated and a new process is launched
   to obtain the peer's new head section.
-  when a peer sends a block, it can optionally include the total
   difficulty *td*. The head information on the peer `gets updated <>`__
   in this case as well. Since we requested this block, it cannot be the
   head of the pool. However if the current best peer as well as all
   others with difficulty above *td* get disconnected, this peer can be
   choosen as best peer.

Add block hashes
~~~~~~~~~~~~~~~~

The third entry poing,
```AddBlockHashes`` <https://github.com/ethereum/go-ethereum/blob/develop/blockpool/blockpool.go#L292>`__
is `called by the ``eth``
protocol <https://github.com/ethereum/go-ethereum/blob/develop/eth/protocol.go#L188>`__
when a ``blockHashesMsg`` (blockhashes message) arrives. Since the
blockpool needs to follow the canonical chain of the best peer at all
times, only the best peer can add block hashes. If this is not the case,
``AddBlockHashes`` returns without effect.

Add blocks
~~~~~~~~~~

```AddBlocks`` <https://github.com/ethereum/go-ethereum/blob/develop/blockpool/blockpool.go#L549>`__
is `called by the ``eth``
protocol <https://github.com/ethereum/go-ethereum/blob/develop/eth/protocol.go#L250>`__
when a ``blocksMsg`` (blocks message) arrives. The various blocks are
requested from multiple peers therefore they are accepted from any peer.
The peer is recorded on the pool node as the source of the block, this
makes it possible to assign an error to the peer in case the block is
invalid.

Synchronisation
---------------

Once a peer is promoted as best peer (total difficulty, and current
chain head block registered) a *head section process* is started, which
first requests from the peer the head block itself. Once the head block
is received, blockhashes starting from the peer's head block are
requested from the best peer.

Once a response is received (and the protocol calls ``AddBlockHashes``),
the sequence of block hashes in the response from the best peer are used
to build up a sequence nodes replicating the head section of the peer's
canonical chain. If the peer fails to respond to requests, after a
period of
```blockTimeout`` <https://github.com/ethereum/go-ethereum/blob/develop/blockpool/blockpool.go#L34>`__,
an ``ErrInsufficientChainInfo`` error is raised. As a consequence, the
peer is disconnected and suspended for ``PeerSuspensionInterval`` during
which it is not allowed to reconnect.

Once the head section nodes are set up, the blockpool starts requesting
blocks for that section. The requests are distributed among multiple
peers so that fetching is optimised.

If the root block of a section is received, then we can connect a
section to its parent section (the root block's parent is the parent
section's head block). We can repeat requesting blockhashes for the
parent section since now we have a way to tell if they arrived.

Once a batch of hashes is received, the node skeleton for the new
section is built, and a process similar to the head section process is
repeated in a somewhat simplified form. To recap, each section runs its
own parallel process with 2 main objective: - get hashes for its parent
section, and - obtain the blocks in the section. This is achieved by -
requesting hashes starting from the root (bottom) node of the section -
requesting blocks based on the hashes in the section

Block requests are distributed among connected peers to optimise
bandwidth utilisation.

With this recursive strategy, a chain is getting built from young to old
blocks section by section. This process is repeated until a known block
is reached. If the known block is found in the blockchain, the
descendent blocks in the chain can be inserted to the blockchain. If the
block is known to the blockpool, i.e., it is found in a known section,
then the peer is registered with the section's process. This means that
the section is requesting and receiving blocks because the section is
part of the best peer's canonical chain. If block insertion reveals an
invalid block, its source (may not be online any more) is given a
``ErrInvalidBlock`` error resulting in disconnect and suspension.

If a block process does not complete within a set period of time
```blockTimeout`` <https://github.com/ethereum/go-ethereum/blob/develop/blockpool/blockpool.go#L34>`__,
the chain is killed and the synchronisation is reattempted with
(potentially) new peers. Note that these timeouts are needed to protect
against attacks where a rogue peer is sending random blockhashes
indefinitely.

Interface to Ethereum core
--------------------------

The interface of the Blockpool with the core is defined with the help of
4 entry points. These are specified as parameters to the `blockpool
constructor <>`__.

Block verification
~~~~~~~~~~~~~~~~~~

Initial block validation that does not require the block to have a known
(already processed and valid) parent block. `Soft proof of work
validation <https://github.com/ethereum/ethash/blob/master/ethash.go#L360>`__
is such a step.

This is used as a first line of defence: when received, blocks are
verified, which by putting a cost to make a peer accept your block,
protects against simple spamming. If PoW verification fails the sender
peer receives an ``ErrInvalidPoW`` error. As a consequence, it is
disconnected and not allowed to reconnect for
```PeerSuspensionInterval`` <link>`__

Inserting a block into blockchain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add one or more blocks on top of a known block. See
```ChainManager.InsertChain`` <https://github.com/ethereum/go-ethereum/blob/develop/core/chain_manager.go#L404>`__
The chain manager runs the vm and does proper block validation as well
as establishes which block has the highest total difficulty defining the
head of the node. If the chain manager finds a block invalid, the peer
that supplied the block receives an ``ErrInvalidBlock`` error and as a
consequence, gets disconnected and suspended for
``PeerSuspensionInterval``. After successfully inserting blocks, if the
block is or was the head block of a peer, the blockpool also checks if
the block's actual total difficulty is identical to one advertised by
the peer. If it is not, the peer received an ``ErrIncorrectTD`` and as a
consequence gets disconnected and suspended for
``PeerSuspensionInterval``. This protects against rogue peers
advertising a high total difficulty and forcing us to follow their
(potentially non-canonical) chain.

Query if block is known
~~~~~~~~~~~~~~~~~~~~~~~

When receiving block hashes and blocks, we need to check whether the
block is already in the blockchain. See
```ChainManager.HasBlock`` <https://github.com/ethereum/go-ethereum/blob/develop/core/chain_manager.go#L292>`__.

Current Total Difficulty
~~~~~~~~~~~~~~~~~~~~~~~~

`Subscription to new block event <>`__, to help set and reset current
total difficulty of our head block. This is needed to filter out
candidate best peers that are behind and therefore useless.

Further features and optimisations
----------------------------------

-  maximise bandwidth utilisation by running parallel section processes
   fetching blocks
-  peer switch: section processes that are part of a stale fork (not on
   the canonical chain of the new best peer) are put to *idle mode*,
   i.e., parent section hash requests and block requests are not sent,
   missing blocks are not checked. Only the absolute deadline timer is
   active on this process.
-  resilience to quick peers switches when several competing miners are
   connected
-  section process caching: if a registered active peer is promoted best
   peer not for the first time during its connection, all non-contiguous
   series of sections are activated (they may or may not have been part
   of the canonical chain of the previous best peer)
-  In order to help optimise mining, blocks are inserted into the
   blockchain the earliest possible time (not waiting for the entire
   section to be processed for instance).

Known limitations
-----------------

The parameters are not currently optimised or even tried against other
settings. This includes batch size, section length, timeouts, and block
request distribution strategy.

When distributing block requests, we could in principle be smarter and
do not request blocks from peers with a known lower difficulty. It is
unclear how certain we can be of peers state, since they could have
caught up synchronising since we received any information about their
head.

In case of a network outage, the timeouts are still ticking, if the
connection is intermittent, this could cause a lot of repeated work
rebuilding the same sections over and over.

Errors
------

The Blockpool uses these
`errors <https://github.com/ethereum/go-ethereum/blob/develop/blockpool/blockpool.go#L62>`__
that are meant to be 'assigned' to peers.

-  ``ErrInvalidBlock`` : Invalid block. Block insertion fails. (Fatal)
-  ``ErrInvalidPoW``: Invalid PoW. Light block verification fails.
   (Fatal)
-  ``ErrUnrequestedBlock``: Unrequested block. Error when there is an
   attempt to add a block to the pool, but there is no skeleton node for
   the blockhash.
-  ``ErrInsufficientChainInfo``: Insufficient chain info. This error is
   raised if the best peer fails to provide the block for their
   advertised current block hash or fail to provide a sequence of
   ancestor hashes of which the *head section* is build up. (Fatal)
-  ``ErrIdleTooLong``: Idle too long. This error is raised if the best
   peer does not send a new block message after an idle period. (Fatal)
-  ``ErrIncorrectTD``: Incorrect ID. Raised when the peer is found to
   advertise incorrect TD for their head block. (Fatal)

Fatal errors lead to the peer getting disconnected and suspended for a
period of ``PeerSuspensionInterval`` for the duration of which they are
not allowed to reconnect.

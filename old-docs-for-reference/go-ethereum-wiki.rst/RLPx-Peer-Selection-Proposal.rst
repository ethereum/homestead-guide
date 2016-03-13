**This is a proposal about how we to select peers using the discovery
protocol. It is not implemented yet.**

In this strategy the maximum number of active peers is ``N * 2``, where
``N`` is configurable and should typically be ``5 <= N <= 8``.

Finding peers to dial
---------------------

The 512 bit (256 bit) space is divided into ``N`` ranges. The dialer
maintains ``N`` slots, one for each range.

In order to find peers, it performs a node lookup with a random target
in reach range corresponding to an empty slot. The results of the lookup
are then dialed. If dialing does not succeed for any node, another
random lookup is performed in that range. Dialed addresses should be
cached for some amount of time to avoid re-dialing unreachable nodes
pointlessly.

Handling incoming connections
-----------------------------

Again, the 512 bit (256 bit) space is divided into ``N`` ranges. The
listener maintains ``N`` buckets, one for each range.

For an incoming connection, after the remote identity has been verified
in the handshake, the listener should keep the new peer if the
corresponding bucket is empty or if the total number of inbound peers is
less than ``N``.

When the number of inbound peers reaches ``N``, the new connection
replaces a random existing connection from any bucket with more than one
entry.

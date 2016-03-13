In order for the network emerging from the peer selection algorithm in
p2p package to support multiple protocols that might require routing,
such as Swarm, the known node set must satisfy the following properties:
\* Peers should make it known which protocols they support (as a list of
identifiers) \* In each row of the Kademlia table, there should be a
sufficient number (as defined by the redundancy requirement *k*, which
might be distinct for each protocol) of node supporting *each* of the
protocols which the host itself supports.

The second requirement is achieved by maintaining distinct redundancy
limits *k*\ \ *p*\  for each protocol *p*, with nodes supporting
multiple protocols counting towards the corresponding limits for each of
them.

Thus, even nodes that do not support a specific protocol can help other
nodes in search of peers that do support it.

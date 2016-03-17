********************************************************************************
Web3 Base Layer Services
********************************************************************************

In addition to the Ethereum blockchain, more components are being developed that decentralise other important aspects of web applications.

.. image:: ../img/ethereum-protocols.png

Swarm - Decentralised data storage and distribution
================================================================================

Swarm is a peer to peer data sharing network in which files are addressed by the hash of their content. Similar to Bittorrent, it is possible to fetch the data from many nodes at once and as long as a single node hosts a piece of data, it will remain accessible everywhere. This approach makes it possible to distribute data without having to host any kind of server - data accessibility is location independent.

Other nodes in the network can be incentivised to replicate and store the data themselves, obviating the need for hosting services when the original nodes are not connected to the network.


Whisper - Decentralised messaging
================================================================================

A protocol for private, secure communication directly between nodes.

--------

Furthermore, standard contracts are being created to make the development and usage of distributed applications easier:

Name registry
================================================================================

Because dapps can be stored anywhere, including the Swarm network, the name registry maps names to their content or location. This is a decentralised alternative to the Domain Name System (DNS).

See https://github.com/ethereum/EIPs/issues/26

Contract registry
================================================================================

To publish the source code of a specific contract, its address has to be mapped to it. The contract registry stores this mapping. Users can then look up this mapping and verify the contract byte code.

See
* global registrar code
* namereg API

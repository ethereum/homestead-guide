.. _Architecture:

################################################################################
Architecture
################################################################################

..  image:: ../../img/dependency_graph.svg

- bench: trie benchmarking
- cmake: cmake files for build system, contains specification of inter-dependencies
- eth: A command-line Ethereum full-node that can be controlled via RPC.
- ethkey: stand-alone key management
- ethminer: stand-alone ethash miner
- ethvm: stand-alone EVM execution utility
- evmjit: library for the EVM just-in-time compiler
- libdevcore: data structures, utilities, rlp, trie, memory db
- libdevcrypto: crypto primitives. Depends on libsecp256k1 and libcrypto++.
- libp2p: core peer to peer networking implementation (excluding specific sub-protocols)
- libethash: ethash mining POW algorithm implementation
- libethash-cl: ethash mining code for GPU mining (OpenCL)
- libethashseal: generic wrapper around the POW block seal engine. Also contains the genesis states for all ethash-based chains.
- libethcore: collection of core data structures and concepts
- libethereum: main consensus engine (minus EVM). Includes the State and BlockChain classes.
- libevm: Ethereum Virtual Machine implementation (interpreter).
- libevmasm: EVM assembly tools, also contains the optimizer.
- libevmcore: elementary data structures of the EVM, opcodes, gas costs, ...
- libweb3jsonrpc: json-rpc server-side endpoint, provides http and IPC (unix socket, windows pipe) connectors
- libwebthree: service connectors for ethereum, swarm/ipfs and whisper.
- libwhisper: whisper implementation
- rlp: stand-alone rlp en-/decoder
- testeth: tests for the modules formerly within the **libethereum** repo
- testweb3core: tests for the modules formerly within the **libweb3core** repo
- testweb3: tests for the modules formerly within the **webthree** repo
- utils/json_spirit: JSON parser written for Boost's Spirit library.
- utils/libscrypt: scrypt implementation
- utils/secp256k1: implementation of the SECP 256k1 ECDSA signing algorithm.

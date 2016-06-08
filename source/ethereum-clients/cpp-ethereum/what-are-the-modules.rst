
################################################################################
What are the modules?
################################################################################


What are the primary executables?
================================================================================

- **eth** A command-line Ethereum full-node that can be controlled via RPC.
- **mix** An IDE for contract and user interface development, testing and deployment to the blockchain.
- **solc**  The solidity command line compiler
- **lllc** The LLL command-line compiler.


Deprecated executables, to be retired soon
================================================================================

- **AlethZero** A Qt-based all-encompassing GUI for interacting with Ethereum (receives minimal support).
- **EthKey** Key management CLI.


What are the various modules?
================================================================================

- **AlethZero** - A Qt-based GUI for interacting with Ethereum. Receives minimal support.
- **libethereum** - Modules related to the Ethereum part of web3, i.e. consensus engine, blockchain download, virtual machine.
    - **ethkey**: stand-alone key management
    - **ethminer**: stand-alone ethash miner
    - ethvm: stand-alone EVM execution utility
    - evmjit: library for the EVM just-in-time compiler
    - libethash: ethash mining POW algorithm implementation
    - libethash-cl: ethash mining code for GPU mining (OpenCL)
    - libethashseal: generic wrapper around the POW block seal engine. Also contains the genesis states for all ethash-based chains.
    - libethcore: collection of core data structures and concepts
    - libethereum: main consensus engine (minus EVM). Includes the State and BlockChain classes.
    - libevm: Ethereum Virtual Machine implementation (interpreter).
    - libevmasm: EVM assembly tools, also contains the optimizer.
    - libevmcore: elementary data structures of the EVM, opcodes, gas costs, ...
    - liblll: Low-level LISP-like Language compiler & assembler.
    - libnatspec: natspec script evaluator (confirmation messages)
    - libtestutils: utilities for testing code
    - lllc: LLL compiler commandline interface
- **libweb3core** - Web3 core libraries, networking, encoding, decoding, basic data structures.
    - bench: trie benchmarking
    - libdevcore: data structures, utilities, rlp, trie, memory db
    - libdevcrypto: crypto primitives. Depends on libsecp256k1 and libcrypto++.
    - libp2p: core peer to peer networking implementation (excluding specific sub-protocols)
    - rlp: stand-alone rlp en-/decoder
- **mix** - Dapp IDE
- **solidity** - Solidity compiler
    - docs: documentation, appears at http://solidity.readthedocs.org/
    - libsolidity: actual implementation
    - analysis: reference resolution, type checking, ... (builds up the annotations for the AST)
    - ast: abstract syntax tree and type system
    - codegen: assembly code generation from annotated AST
    - formal: formal verification
    - interface: external interface for users of libsolidity
    - parsing: parser (creates the non-annotated AST)
    - solc: commandline compiler
- **web3.js** - JavaScript Dapp framework library (connects to backend via RPC / IPC)
- **webthree** - actual client / node implementation ("eth")
    - eth: commandline client / node
    - libjsconsole: JavaScript console for access to eth - deprecated, to be replaced by nodejs application
    - libjsengine: underlying engine for libjsconsole, to be removed
    - libweb3jsonrpc: json-rpc server-side endpoint, provides http and IPC (unix socket, windows pipe) connectors
    - libwebthree: service connectors for ethereum, swarm/ipfs and whisper.
    - libwhisper: whisper implementation
- **webthree-helpers** - build system and some external dependencies
    - cmake: cmake files for build system, contains specification of inter-dependencies
    - utils: external dependencies
        - json_spirit: JSON parser written for Boost's Spirit library.
        - libscrypt: scrypt implementation
        - secp256k1: implementation of the SECP 256k1 ECDSA signing algorithm.

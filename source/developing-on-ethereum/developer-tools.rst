********************************************************************************
Developer Tools
********************************************************************************
As a Ðapp developer you have five main resources which allow Ðapp
development.

Five Primary Resources
================================================================================
ÐApp development requires an understanding of the Web3 Javascript API, the JSON RPC API, and the Solidity programming language. Note: There are developer tools that help you develop, test, and deploy ÐApps in a way that automatically utilizes the resources listed below.

.. todo::

   Add cross reference to developer tools page in the first paragraph.

-  `Web3 JavaScript API <https://github.com/ethereum/wiki/wiki/JavaScript-API>`__ - This is the main JavaScript SDK to use when you want to interact with an Ethereum node.
-  `JSON RPC API <https://github.com/ethereum/wiki/wiki/JSON-RPC>`__ - This is the low level JSON RPC 2.0 interface to interface with a node. This API is used by the `Web3 JavaScript API <https://github.com/ethereum/wiki/wiki/JavaScript-API>`__.
-  `Solidity Documentation <https://solidity.readthedocs.org/en/latest/>`__ - Solidity is the Ethereum developed Smart Contract language, which compiles to EVM (Ethereum Virtual Machine) opcodes.
-  `Testnets`_ - Test networks help developers develop and test Ethereum code and network interactions without spending their own Ether on the main network. Test network options are listed below.
- `IDE or Development Framework`_. This assists you in developing, debugging, and deploying Ethereum applications. 


Ethereum High Level Languages
===========================================================================

Contracts live on the blockchain in an Ethereum-specific binary format (EVM bytecode) that is executed by the Ethereum Virtual Machine (EVM). However, contracts are typically written in a higher level language and then compiled using an EVM compiler into byte code which is then deployed to the blockchain.

Below are the different high level languages developers can use to write smart contracts for Ethereum.

Solidity
--------------------------------------------------------------------------------

Solidity is a language similar to JavaScript which allows you to develop contracts and compile to EVM bytecode. It is currently the flagship language of Ethereum and the most popular.

* `Solidity Documentation <http://solidity.readthedocs.org/en/latest/>`_ - Solidity is the flagship Ethereum high level language that is used to write contracts.
* `Solidity online realtime compiler <http://chriseth.github.io/browser-solidity/>`_
* `Standardized Contract APIs <https://github.com/ethereum/wiki/wiki/Standardized_Contract_APIs>`__
* `Useful Ðapp Patterns <https://github.com/ethereum/wiki/wiki/Useful-Ðapp-Patterns>`__ - Code snippets which are useful for Ðapp development.

Serpent
--------------------------------------------------------------------------------

Serpent is a language similar to Python which can be used to develop contracts and compile to EVM bytecode. It is intended to be maximally clean and simple, combining many of the efficiency benefits of a low-level language with ease-of-use in programming style, and at the same time adding special domain-specific features for contract programming. Serpent is compiled using _`LLL`.

* `Serpent on the ethereum wiki <https://github.com/ethereum/wiki/wiki/Serpent>`_
* `Serpent EVM compiler <https://github.com/ethereum/serpent>`_

LLL
--------------------------------------------------------------------------------

`Lisp Like Language (LLL) <https://github.com/ethereum/libethereum/tree/develop/liblll>`_ is a low level language similar to Assembly. It is meant to be very simple and minimalistic; essentially just a tiny wrapper over coding in EVM directly.

* `LIBLLL in GitHub <https://github.com/ethereum/libethereum/tree/develop/liblll>`_
* `Examples of LLL <https://www.reddit.com/r/ethereum/comments/3secu1/anyone_have_a_copy_of_the_old_lll_tutorials/>`_

Mutan (Deprecated)
--------------------------------------------------------------------------------

`Mutan <https://github.com/obscuren/mutan>`_ is a statically typed, C-like language designed and developed by Jeffrey Wilcke. It is no longer maintained.


IDEs/Frameworks
================================================================================

Below are developer frameworks and IDEs used for writing Ethereum Đapps.

TODO
  expand at least some of these to subsections, add reference to community

* `Mix Ethereum IDE <https://github.com/ethereum/mix>`__ - Mix is an IDE that allows developers to build and deploy contracts and decentralized applications on top of the Ethereum blockchain. It includes a Solidity source code debugger.
* `Truffle <https://github.com/ConsenSys/truffle>`__ - Truffle is a development environment, testing framework and asset pipeline for Ethereum.
* `Dapple <https://github.com/nexusdev/dapple>`__ - Dapple is a tool for Solidity developers to help build and manage complex contract systems on Ethereum-like blockchains.
* `Populus <http://populus.readthedocs.org/en/latest/>`__ - Populus is a Smart Contract development framework written in python.
* `Embark <https://iurimatias.github.io/embark-framework/>`__ - Embark is a Ðapp development framework written in JavaScript.
* `EtherScripter \(obsolete, discontinued\) <http://etherscripter.com/0-5-1/>`_
* `Resilience Raw Transaction Broadcaster <https://github.com/resilience-me/broadcaster/>`_

Base Layer Services
=================================================

Ethereum Alarm Clock
--------------------------------------------------------------------------------

* **Author:** Piper Merriam
* **Website:** `alarm_main_website`_.
* **Documentation:** `alarm_documentation`_.

A marketplace that facilitates scheduling transactions to occur at a later
time.  Serves a similar role to things like *crontab* in unix, or *setTimeout*
in javascript.


Ethereum Computation Market
--------------------------------------------------------------------------------

* **Author:** Piper Merriam
* **Website:** `computation_market_main_website`_.
* **Documentation:** `computation_market_documentation`_.

A marketplace that facilitates verifiable execution of computations off-chain.
Allows for very expernsive computations to be used within the EVM without
having to actually pay the high gas costs of executing them on-chain.

.. _alarm_main_website: http://www.ethereum-alarm-clock.com/
.. _alarm_documentation: http://docs.ethereum-alarm-clock.com/
.. _computation_market_main_website: http://www.ethereum-computation-market.com/
.. _computation_market_documentation: http://docs.ethereum-computation-market.com/

The EVM
================================================================================
The Ethereum Virtual Machine (EVM) is the runtime environment for smart contracts in Ethereum. It is not only sandboxed, but actually completely isolated, which means that code running inside the EVM has no access to network, filesystem, or other processes. Smart contracts even have limited access to other smart contracts.

Contracts live on the blockchain in an Ethereum-specific binary format (EVM bytecode). However, contracts are typically written in an Ethereum high level language, compiled into byte code using an EVM compiler, and finally uploaded on the blockchain using an Ethereum client.

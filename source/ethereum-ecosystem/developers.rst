********************************************************************************
Developer Tools
********************************************************************************

========================================================================
Client Implementations
========================================================================

Ethereum clients are written in multiple programming languages. Each implementation is based on the formal definition of the Ethereum protocol defined in the `Ethereum Yellow Paper <http://gavwood.com/paper.pdf>`_.

Client List
-------------------------------

===============         ===============
Language                 Name
===============         ===============
Golang                   `Geth <http://ethereum.github.io/go-ethereum/>`_
C++                      `TurboEthereum (formerly eth) <https://github.com/ethereum/webthree-umbrella/wiki>`_
Javascript/Node          `EthereumJS <http://ethereumjs.github.io/>`_
Python                   `Pyethereum <https://github.com/ethereum/pyethereum>`_
Java                     `ethereumJ <https://github.com/ethereum/ethereumj>`_
Haskell                  `ethereumH <https://github.com/blockapps/strato-p2p-client>`_
Rust                     `Parity <https://ethcore.io/parity.html>`__
===============         ===============

Resources
-------------------------------------

* `Distribution of client implementations on the current live network <https://etherchain.org/nodes>`_ - realtime stats on etherchain
* `What is the need for that many implementations <https://www.reddit.com/r/ethereum/comments/2bxo9c/whats_the_need_for_that_many_implementations/>`_ - reddit discussion


===========================================================================
Ethereum High Level Languages
===========================================================================

Contracts live on the blockchain in an Ethereum-specific binary format (EVM bytecode) that is executed by the Ethereum Virtual Machine (EVM). However,
 contracts are typically written in a higher level language and then compiled using an EVM compiler into byte code which is then deployed to the blockchain .

Below are the different high level languages developers can use to write  smart contracts for Ethereum.

Solidity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Solidity is a language similar to JavaScript which allows you to develop contracts and compile to EVM bytecode. It is currently the flagship language of Ethereum and the most popular.

* `Solidity documentation site <http://solidity.readthedocs.org/en/latest/>`_
* `Solidity online compiler <http://chriseth.github.io/browser-solidity/>`_

Serpent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Serpent is a language similar to Python which can be used to develop contracts and compile to EVM bytecode. It is intended to be maximally clean and simple, combining many of the efficiency benefits of a low-level language with ease-of-use in programming style, and at the same time adding special domain-specific features for contract programming. Serpent can be compiled into LLL.

* `Serpent on the ethereum wiki <https://github.com/ethereum/wiki/wiki/Serpent>`_
* `Serpent EVM compiler <>`_


LLL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lisp Like Language is a low level language similar to Assembly. It is meant to be very simple and minimalistic; essentially just a tiny wrapper over coding in EVM directly.


Mutan (Deprecated)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mutan is a statically typed, C-Like language. Mutan is a  higher level language.


IDEs/Frameworks
================================================================================

TODO
  expand at least some of these to subsections, add reference to community

- `Mix Ethereum IDE <https://github.com/ethereum/mix>`__ - Mix is an IDE that allows developers to build and deploy contracts and decentralized applications on top of the Ethereum blockchain. It includes a Solidity source code debugger.
- `Truffle <https://github.com/ConsenSys/truffle>`__ - Truffle is a development environment, testing framework and asset pipeline for Ethereum.
- `Dapple <https://github.com/nexusdev/dapple>`__ - Dapple is a tool for Solidity developers to help build and manage complex contract systems on Ethereum-like blockchains.
- `Populus <http://populus.readthedocs.org/en/latest/>`__ - Populus is a Smart Contract development framework written in python.
- `Embark <https://iurimatias.github.io/embark-framework/>`__ - Embark is a Ðapp development framework written in JavaScript.


TODO
   reorg developers resources, ethereum-high-level-languages.rst under developing on ethereum?  alarm clock, computational market should come under this
   would like to include/endorse oraclize and btcrelay


* `Ether.Fund Calculator <>`_ (note, uses crowdsale pricing so USD is not accurate)
* `Ethereum Gas Prices <https://docs.google.com/spreadsheets/d/1m89CVujrQe5LAFJ8-YAUCcNK950dUzMQPMJBxRtGCqs>`_
* `EtherScripter (obsolete, discontinued) <http://etherscripter.com/0-5-1/>`_
* `Resilience Raw Transaction Broadcaster <https://github.com/resilience-me/broadcaster/>`_

********************************************************************************
Base Layer Services
********************************************************************************


Ethereum Alarm Clock
----------------------

* **Author:** Piper Merriam
* **Website:** `alarm_main_website`_.
* **Documentation:** `alarm_documentation`_.

A marketplace that facilitates scheduling transactions to occur at a later
time.  Serves a similar role to things like *crontab* in unix, or *setTimeout*
in javascript.


Ethereum Computation Market
-----------------------------

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

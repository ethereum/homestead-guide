********************************************************************************
Ethereum High Level Languages
********************************************************************************
Contracts live on the blockchain in an Ethereum-specific binary format (EVM bytecode) that is executed by the Ethereum Virtual Machine (EVM). However, contracts are typically written in a higher level language and then compiled using an EVM compiler into byte code which is then deployed to the blockchain .

Below are the different high level languages developers can use to write  smart contracts for Ethereum.


TODO
  listing and comparison of merits, existing infrastructure, educational resources
  crossref to developers resources in developer chapter

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


LLL - unmaintained ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lisp Like Language is a low level language similar to Assembly. It is meant to be very simple and minimalistic; essentially just a tiny wrapper over coding in EVM directly.


Mutan - unmaintained?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mutan is a statically typed, C-Like language. Mutan is a  higher level language.

Obsolete Terminology
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO
  put this into the glossary marked as obsolete `

HLL
  Acronym for Higher Level Language, which is what Serpent and Solidity are. HLL is what early Ðapp developers called Ethereum programming languages that did not touch the low level elements. This phrase has been phased out.

CLL
  Acronym for C Like Language, which Mutan was. This acronym has been phased out.

ES1, ES2, and ES3
  "Ethereum Script" versions 1,2 and 3. There were early versions of what would become the Ethereum Virtual Machine (EVM).


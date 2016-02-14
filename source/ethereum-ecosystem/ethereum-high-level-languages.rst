********************************************************************************
Ethereum High Level Languages
********************************************************************************
Contracts live on the blockchain in an Ethereum-specific binary format (EVM bytecode). However, contracts are typically written in an Ethereum high level language and then compiled into byte code to be uploaded on the blockchain using an EVM compiler.

Below are the different high level Ethereum languages in Ethereum which allow you to compile your Smart Contract into a EVM specific bytecode.

Supported
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Solidity** - Solidity is a language similar to JavaScript which allows you to develop contracts and compile to EVM bytecode. It is currently the flagship language of Ethereum and the most popular. More details can be found here: http://solidity.readthedocs.org/en/latest/

**Serpent** - Serpent is a language similar to Python which can be used to develop contracts and compile to EVM bytecode. It is intended to be maximally clean and simple, combining many of the efficiency benefits of a low-level language with ease-of-use in programming style, and at the same time adding special domain-specific features for contract programming. Serpent can be compiled into LLL. More details can be found here: https://github.com/ethereum/wiki/wiki/Serpent

**LLL** - Lisp Like Language is a low level language similar to Assembly. It is meant to be very simple and minimalistic; essentially just a tiny wrapper over coding in EVM directly.

Not-Supported
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Mutan** - Mutan is a statically typed, C-Like language. Mutan is a  higher level language.

Related Acronyms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**HLL** - Acronym for Higher Level Language, which is what Serpant and Solidity are. HLL is what early Ðapp developers called Ethereum programming languages that did not touch the low level elements. This phrase has been phased out.

**CLL** - Acronyom for C Like Language, which Mutan was. This acronym has been phased out.

**ES1, ES2, and ES3** - "Ethereum Script" versions 1,2 and 3. There were early versions of what would become the Ethereum Virtual Machine (EVM).
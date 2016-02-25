
A next generation blockchain
=======================================================================
A blockchain is a distributed computing architecture where every network node executes and records the same transactions, grouped in blocks. Each block contains a mathematical calculation which verifies that it contains all of the transactions and is based on the previous block. If all nodes in the blockchain network have consensus on each block in the chain, then this enables a sort of distributed ledger or replicated database of the transactions that occurred.

Blockchain technology is the technological basis of Bitcoin, first described as a coherent cryptoeconomic system by its mysterious author Satoshi Nakamoto in his white paper "Bitcoin: A Peer-to-Peer Electronic Cash System", published in 2009. While the use of blockchains for more general uses is already discussed in the original paper, it was not until a few years later that blockchain technology emerged as a generic term to designate the cryptoeconomic system composed of a transparent open ledger or database representing a state of a complex system, updated via sending transactions to the guardians of the blockchain. The guardians are nodes of a decentralised peer to peer network. In Bitcoin's case the open ledger is simply conceived of as a table of account balances, and transactions are value transfers. Due to the decentralised nature of this peer to peer system, secured by cryptography and driven by algorithmically enforced economic incentives coupled with scarcity and controlled issuance (predictable inflation) coded in the protocol, bitcoin is suitable to serve as sound digital money without central bank or other power behind it. This allows trustless finance between individuals.

A few years into the bitcoin experiment novel projects started to show interest in using the bitcoin network for purposes other than financial transfer. This provided the necessary inspiration Ethereum's inventor, Vitalik Buterin, needed to realise that the technical requirements for all these ventures could be subsumed under a high level system, only if the right abstraction is found.
In 2014, Ethereum founders Vitalik Buterin, Gavin Wood and Jeffrey Wilcke began work on a next generation blockchain that had the ambitions to implement a fully general trustless smart contract platform.


********************************************************************************
What is Ethereum?
********************************************************************************

Ethereum in the narrow sense refers to a suite of protocols that define a platform for decentralised applications. At the heart of it is the Virtual Machine, which can execute code of arbitrary algorithmic complexity (Turing Completeness). Ethereum
is also a peer to peer network protocol. Each and every node of the network runs the EVM and executes the same instructions hence the evokative name, World Computer.
Important to understand that this distributed network is not in place to distribute computation in order to make code execution more efficient via parallelisation.
In sharp contrast to such systems (hadoop, golem), ethereum nodes all compute the same rendering the system massively redundant. This is the price to pay for decentralised consensus. If you want to do without a central third party, an oracle to tell you what is right, you must check yourself. Efficiency here is on this level.

At least since bitcoin we understand why monopoly or centralisation always lead to inefficient markets due to the brittlenes of putting all trust into one entity.
Decentralising consensus results in extreme levels of fault tolerance, zero downtime and forever unchangeable storage and censorship-resistance.

The ethereum platform is featureless or value-agnostic in the same sense as a programming language is. Similar to programming language enviroments, it is up to users (more like entrepreneurs and developers) to decide what they are using it for.
That said it is clear that application that can automate direct interaction or facilitate coordinated group action which benefit most from using Ethereum as their backend. Due to near-zero switching cost as well as its open-architecture, Ethereum has the potetial to disintermediate now powerful rent-seeking middle man businesses and therefore drive the pricelevel of services down to marginal costs.

Since nodes need to (be able to) argree on the outcome of computations, the Ethereum Virtual Machine runs in a closed box so that strictly deterministic execution is guaranteed. If you understand this, you will understand why it is not possible to have native random number generation or external calls (like access to current date/time or api calls etc).

The Ethereum blockchain is an open database. In this database  sit the accounts which are smart contracts. Smart contracts are pieces of code which executes when a transaction is sent addressing the account in question. Users can create new contracts by deploying the EVM contract code to the blockchain or trigger the execution of existing contracts. Both are done by sending a transaction to the network.
The nodes of the network receieve, verify, execute all incoming transactions which they them package in blocks. The peer to peer network protocol describes how transactions are relayed and how blocks are announced.

We can think of these smart contracts as functions which are called with input parameters specified in the transaction. Peers are motivated to produce blocks (which presupposes the execution of all transactions in previous blocks) by economic incentives.
Just like in the case of bitcoin, the blocks need to be sealed by a proof of work.
Any computational problem that requires orders of magnitude more resources to solve algorithmically than it takes to verify the solution is a good candidate for proof of work. In order to discourage centralisation due to usin specialised hardware, Ethereum chose a memory-hard computational problem. If the problem requires memory as well as CPU, specialised hardware is in fact the general computer hence Ethereum is ASIC resistant, allowing a more democratised provision of security than say in Bitcoin.

The nodes are incentivised to validate blocks and perform the proof of work calculations by competing for a reward. Those node to first submit a valid block with the strongest proof is rewarded.

The system is protected against users sending frivolous computational tasks (DDOS peers with transactions or running infinite loops etc) because transaction senders are charged for each execution step. Even in the absence of transactions, nodes are producing blocks and get a standard one-off fee for their contribution called mining reward.

Transaction charges and mining reward necessitate having a token of value, a currency at the heart of the system. The mining reward is newly minted coins as if you found gold (which is why the whole process of validation is called mining). This currency is Ether.

Because of all these aspects of the system it makes sense to talk about Ethereum in the wide sense as an ecosystem of the core protocol with supporting infrastructure and community.

This chapter discusses the
* social and institutional basis relevant for governance and collaboration of an open source project (_`The Ethereum foundation`, _`Community Discussion Fora`)
* the currency behind Ether and its use to buy gas, the cryptofuel that drive the VM
* sofware implementing the Ethereum protocol narrow sense (_`Client implementations`), software and analytic/educational infrastructure supporting mining, obtaining and storing Ether and tracking activity.
* Finally we provide information for developers that write smart contracts and build decentralised applications for the web3 by listing developer tools, testing practices, and access to base payer services.



Web 3:
A platform for decentralized apps
=======================================================================

The realisation came early on that a trustless contract platform is perfectly suited as the shared backend to the internet we always wanted.
Ethereum's mission to provide Web 3.0, the crypto 2.0 vision of a truly decentralized and secure internet populated by decentralized apps (dapps) and interacting autonomous agents was born.

As intended by the Ethereum developers, Ethereum is a blank canvas and you have the freedom to build whatever you want with it. The Ethereum protocol is meant to be generalized so that the core features can be combined in arbitrary ways. Ideally, dapp projects on Ethereum will leverage the Ethereum blockchain to build solutions that rely on decentralized consensus to provide new products and services that were not previously possible.

Ethereum can also be understood by looking at the projects that use Ethereum. Already, there are a number of high-profile projects built on Ethereum such as Augur, Digix, Maker, and many more (see _`Dapps`). In addition, there are development teams that build open source components that anyone can use.  While each of these organizations are separate from the Ethereum Foundation and have their own goals, they undoutedly benefit the overall Ethereum ecosystem.







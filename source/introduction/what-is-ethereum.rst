
A next generation blockchain
=======================================================================
A blockchain is a distributed computing architecture where every network node executes and records the same transactions, grouped in blocks. Each block contains a mathematical calculation which verifies that it contains all of the transactions and is based on the previous block. If all nodes in the blockchain network have consensus on each block in the chain, then this enables a sort of distributed ledger or replicated database of the transactions that occurred.

Blockchain technology is the technological basis of Bitcoin, first described by its mysterious author Satoshi Nakamoto in his white paper "Bitcoin: A Peer-to-Peer Electronic Cash System", published in 2008. While the use of blockchains for more general uses was already discussed in the original paper, it was not until a few years later that blockchain technology emerged as a generic term to designate the cryptoeconomic system composed of a transparent open ledger or database representing a state of a complex system, manipulated via transactions propagated across a peer to peer network. In Bitcoin's case the open ledger is conceived of as a table of account balances, and transactions are transfers of the bitcoin token. Due to the decentralised nature of this peer to peer system, secured by cryptography and driven by algorithmically enforced economic incentives coupled with scarcity and controlled issuance (predictable inflation) coded in the protocol, bitcoin is suitable to serve as digital money without a central bank or other centralized authority behind it. This allows trustless finance between individuals.

As bitcoin began attracting greater attention from developers and technologists, novel projects began to use the bitcoin network for purposes other than transfers of value tokens. Many of these took the form of "alt coins" - separate blockchains with cryptocurrencies of their own which improved on the original bitcoin protocol to add new features or capabilities. In late 2013, Ethereum's inventor Vitalik Buterin proposed that a single blockchain with the capability to be reprogrammed to perform any arbitrarily complex computation could subsume these many other projects. 

In 2014, Ethereum founders Vitalik Buterin, Gavin Wood and Jeffrey Wilcke began work on a next-generation blockchain that had the ambitions to implement a general fully trustless smart contract platform.


********************************************************************************
What is Ethereum?
********************************************************************************

Ethereum is a programmable blockchain. Rather than give users a set of pre-defined operations (e.g. bitcoin transactions), Ethereum allows users to create their own operations. In this way, it serves as a platform for many different types of decentralized blockchain applications, including but not limited to cryptocurrencies.

Ethereum in the narrow sense refers to a suite of protocols that define a platform for decentralised applications. At the heart of it is the Ethereum Virtual Machine ("EVM"), which can execute code of arbitrary algorithmic complexity. In computer science terms, Ethereum is "turing complete". Developers can create applications that run on the EVM using friendly programming languages modelled on existing languages like javascript and python.

Like any blockchain, Ethereum also includes a peer-to-peer network protocol. The ethereum blockchain database is maintained and updated by many nodes connected to the network. Each and every node of the network runs the EVM and executes the same instructions. For this reason, Ethereum is sometimes described evocatively as a "world computer". 

This massive parallelisation of computing across the entire Ethereum network is not done to make computation more efficient. In fact, this process makes computation on Ethereum far slower and more expensive than on a traditional "computer". Rather, every Ethereum node runs the EVM in order to maintain consensus across the blockchain. Decentralized consensus gives Ethereum extreme levels of fault tolerance, ensures zero downtime, and makes data stored on the blockchain forever unchangeable and censorship-resistant.

Many applications are now being built on Ethereum. The Ethereum platform itself is featureless or value-agnostic. Similar to programming language enviroments, it is up to entrepreneurs and developers to decide what it should be used for. However, it is clear that certain application types benefit more than others from Ethereum's capabilities. Specifically, ethereum is **suited for applications that automated direct interaction between peers or facilitate coordinated group action across a network**. For instance, applications for coordinating peer-to-peer marketplaces, or the automation of complex financial contracts. Ethereum's open architecture - the fact that anyone, anywhere, can build on it - gives it the potential to compete with existing services. 

********************************************************************************
How does Ethereum work?
********************************************************************************

Ethereum incorporates many features and technologies that will be familiar to users of bitcoin, while also introducing many modifications and innovations of its own.

Whereas the bitcoin blockchain was purely a list of transactions, **Ethereum's basic unit is the account**. The Ethereum blockchain tracks the state of every account, and all state transitions on the Ethereum blockchain are transfers of value and information beween accounts. There are two types of account:

- Externally Owned Accounts (EOAs), which are controlled by private keys
- Contract Accounts, which are controlled by their contract code and can only be "activated" by an EOA

For most users, the basic difference between these is that human users control EOAs - because they can control the private keys which give control over an EOA. Contract accounts, on the other hand, are governed by their internal code. If they are "controlled" by a human user, it is because they are *programmed* to be controlled by an EOA with a certain address, which is in turn controlled by whoever holds the private keys that control that EOA. The popular term "smart contracts" refers to cod in a Contract Account - programs that execute when a transaction is sent to that account. Users can create new contracts by deploying code to the blockchain. 

Contract accounts only perform any operation when instructed to do so by an EOA. So it is not possible for a Contract Account to be performing native operations like random number generation or API calls - it can do these things only if prompted by an EOA. This is because Ethereum requires nodes to be able to agree on the outcome of computation, which requires a guarantee of strictly deterministic execution.

Like in bitcoin, users must pay small transaction fees to the network. This protects the Ethereum blockchain from frivolous or malicious computational tasks, like DDOS attacks or infinite loops. The sender of a transaction must pay for each step of the "program" they activated, including computation and memory storage.  These fees are paid in amounts of Ethereum's native value-token, Ether. 

These transaction fees are collected by the nodes that validate the network. These "miners" are nodes in the Ethereum network that receive, propogate, verify, and execute transactions. The miners then group the transactions - which include many updates to the "state" of accounts in the Ethereum blockchain - into what are called "blocks", and miners then compete with one another for *their* block to be the next one to be added to the blockchain. Miners are rewarded for each succesful block they mine with ether. This provides the economic incentive for people to dedicate hardware and electriciy to Ethereum network. 

Just as in the bitcoin network, miners are tasked with solving a complex mathematical problem in order to succesfully "mine" a block. This is known as a Proof of Work. Any computational problem that requires orders of magnitude more resources to solve algorithmically than it takes to verify the solution is a good candidate for proof of work. In order to discourage centralisation due to the use of specialised hardware (e.g. ASICs), as has occurred in the Bitcoin network, Ethereum chose a memory-hard computational problem. If the problem requires memory as well as CPU, the ideal hardware is in fact the general computer. This makes Ethereum's Proof of Work ASIC-resistant, allowing a more decentralized distribution of of security than blockchains whose mining is dominated by specialized hardware, like Bitcoin.


Ethereum is perhaps best described as an ecosystem: the core protocol is supported by various pieces of infrastructure, code, and community that together make up the Ethereum project.

This chapter discusses the
* social and institutional basis relevant for governance and collaboration of an open source project (_`The Ethereum foundation`, _`Community Discussion Fora`)
* the currency behind Ether and its use to buy gas, the cryptofuel that drive the VM
* sofware implementing the Ethereum protocol narrow sense (_`Client implementations`), software and analytic/educational infrastructure supporting mining, obtaining and storing Ether and tracking activity.
* Finally we provide information for developers that write smart contracts and build decentralised applications for the web3 by listing developer tools, testing practices, and access to base payer services.


********************************************************************************
Web 3: A platform for decentralized apps
********************************************************************************

The realisation came early on that a trustless contract platform is perfectly suited as the shared backend to the internet we always wanted.
Ethereum's mission to provide Web 3.0, the crypto 2.0 vision of a truly decentralized and secure internet populated by decentralized apps (dapps) and interacting autonomous agents was born.

As intended by the Ethereum developers, Ethereum is a blank canvas and you have the freedom to build whatever you want with it. The Ethereum protocol is meant to be generalized so that the core features can be combined in arbitrary ways. Ideally, dapp projects on Ethereum will leverage the Ethereum blockchain to build solutions that rely on decentralized consensus to provide new products and services that were not previously possible.

Ethereum can also be understood by looking at the projects that use Ethereum. Already, there are a number of high-profile projects built on Ethereum such as Augur, Digix, Maker, and many more (see _`Dapps`). In addition, there are development teams that build open source components that anyone can use.  While each of these organizations are separate from the Ethereum Foundation and have their own goals, they undoutedly benefit the overall Ethereum ecosystem.







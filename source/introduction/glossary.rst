********************************************************************************
Glossary
********************************************************************************

.. glossary::
   :sorted:
 
   Đ
      Đ, `D with stroke <https://en.wikipedia.org/wiki/D_with_stroke>`_, is used in Old English, Middle English, Icelandic, and Faroese to stand for an uppercase letter "Eth". The uppercase eth (Ð) is also used to symbolize the cryptocurrency Dogecoin.
   Đapp
      Unofficially stands for either "distributed app" or "eth app". Some say it is pronounced Ethapp due to the use of the uppercase eth letter Ð.

   ether
      Ether is the name of the currency used within Ethereum. It is used to pay for computations within the EVM.

   EOA
      An account controlled by a private key. If you own the private key associated with the EOA you have the ability to send ether and messages from it. This differs from a contract account that has it's own code and is controlled by code. EOAs and contract accounts may be combined into a single account type during Serenity.

   gas
      Name for the execution fee for every operation made on an Ethereum blockchain.

   Gas limit
      This is the maximum amount of gas that you indicate that you are willing to pay for a contract execution transaction. It is meant to protect users from getting their ether depleted when trying to execute buggy or malicious contracts.
   gas price
      Price (in ether) of one unit of gas specified in the transaction.

   Account
      A private and public key pair that allows you to receive and send ether.
   transaction
      The signed data package that stores a message to be sent from an externally owned account. Simply put, a transaction describes a transfer of information from an EOA to another EOA or a contract account.

   message
      A data transfer mechanism contracts use to communicate with other contracts. Messages can also be described as virtual objects that are never serialized and exist only in the Ethereum execution environment.

   web3
      The exact definition of the Web3 paradigm is still taking form, but it generally refers to the phenomenon of increased connectedness between all kinds of devices, decentralisation of services and applications, semantic storage of information online and application of artificial intelligence to the web.
      
   DAO
      Decentralized Autonomous Organisation.
   Epoch
      Epoch is the interval between each regeneration of the DAG used as seed by the PoW algorithm Ethash. The epoch in specified as 30000 blocks.

   Elliptic curve (cryptography)
      Refers to an approach to public-key cryptography based on the algebraic structure of elliptic curves over finite fields. See `here <https://en.wikipedia.org/wiki/Elliptic_curve_cryptography>`_.
   wallet
      A wallet is a smart contract that secures your ether and identity with features such as multisignature signing, new addresses for each transaction and password protection.
   Contract
      A persistent piece of code on the Ethereum blockchain that encompasses a set of data and executable functions. These functions execute when Ethereum transactions are made to them with certain input parameters. Based on the input parameters, the functions will execute and interact with data within and outside of the contract.
   Suicide
      This refers to the permanent killing(aka deletion) of the executable code belonging to a contract. It frees up space on the blockchain and prevents future execution of the contract. The contract's address will however still persist, but ether sent to it will be lost forever. The possibility to kill a contract has to be implemented by the contract creator him/herself using the Solidity 'suicide' function.
   Transaction fee
      Also known as gas cost, it is the amount of ether that the miners will charge for the execution of your transaction.
   mining
      The process of verifying transactions and contract execution on the Ethereum blockchain in exchange for a reward in ether with the mining of every block.
   mining pool
      The pooling of resources by miners, who share their processing power over a network, to split the reward equally, according to the amount of work they contributed to solving a block.
   mining reward
      The amount of cryptographic tokens (in this case ether) that is given to the miner who mined a new block.
   State
      Refers to a snapshot of all balances and data at a particular point in time on the blockchain, normally referring to the condition at a particular block.
   blockchain
      An ever-extending series of data blocks that grows as new transactions are confirmed as part of a new block. Each new block is chained to the existing blockchain by a cryptographic proof-of-work.
   peer
      Other computers on the network also running an Ethereum node (Geth) with an exact copy of the blockchain that you have.
   signing
      Producing a piece of data from the data to be signed using your private key, to proof that the data originates from you.  
   discovery (peer)
      The process of 'gossiping' with other nodes in the network to find out the state of other nodes on the network.
   gas price oracle
      A helper function of the Geth client that tries to find an appropriate default gas price when sending transactions. 
   light client
      A client program that allows users in low-capacity environments to still be able to execute and check the execution of transactions without needing to run a full Ethereum node (Geth).
   etherbase
      It is the default name of the account on your node that acts as your primary account. If you do mining, mining rewards will be credited to this account.
   coinbase
      Coinbase is analogous to etherbase, but is a more generic term for all cryptocurrency platforms.
   balance
      The amount of cryptocurrency (in this case) belonging to an account.
   solidity
      Solidity is a high-level language whose syntax is similar to that of JavaScript and it is designed to compile to code for the Ethereum Virtual Machine.
   serpent
      Serpent is a high-level language whose syntax is similar to that of Python and it is designed to compile to code for the Ethereum Virtual Machine.
   evm
      Ethereum Virtual Machine, the decentralized computing platform which forms the core of the Ethereum platform. 
   virtual machine
      In computing, it refers to an emulation of a particular computer system. 
   peer to peer network
      A network of computers that are collectively able to perform functionalities normally only possible with centralized, server-based services.
   decentralisation
      The concept of moving the control and execution of computational processes away from a central entity. 
   distributed hash table
      A distributed hash table (DHT) is a class of a decentralized distributed system that provides a lookup service similar to a hash table: (key, value) pairs are stored in a DHT, and any participating node can efficiently retrieve the value associated with a given key.
   NAT
      Network address translation (NAT) is a methodology of remapping one IP address space into another by modifying network address information in Internet Protocol (IP) datagram packet headers while they are in transit across a traffic routing device.
   nonce
      Number Used Once or Number Once. A nonce, in information technology, is a number generated for a specific use, such as session authentication. Typically, a nonce is some value that varies with time, although a very large random number is sometimes used. In general usage, nonce means “for the immediate occasion” or “for now.”
      In the case of Blockchain Proof of Work scenarios, the hash value, found by a Miner, matching the network's Difficulty thus proving the Block Validity is called Nonce as well.

   proof of work
      Often seen in its abbreviated form "PoW", it refers to a mathematical value that can act act as the proof of having solved a resource and time consuming computational problem.
   proof of stake
      An alternative method of mining blocks that require miners to demonstrate their possession of a certain amount of the currency of the network in question. This works on the principle that miners will be disincentivised to try to undermine a network in which they have a stake in. PoS is less wasteful than PoW, but is still often used together with it to provide added security to the network.
   casper
      Casper is a security-deposit based economic consensus protocol. This means that nodes, so called “bonded validators”, have to place a security deposit (an action we call “bonding”) in order to serve the consensus by producing blocks. If a validator produces anything that Casper considers “invalid”, their deposit are forfeited along with the privilege of participating in the consensus process.  
   consensus
      The agreement among all nodes in the network about the state of the Ethereum network.
   homestead
      
   metropolis
      
   serenity
      
   frontier
      
   olympic
      
   morden
      
   testnet
      A mirror network of the production Ethereum network that is meant for testing.
   private chain
      A fully private blockchain is a blockchain where write permissions are kept centralized to one organization.
   consortium chain
      A blockchain where the consensus process is controlled by a pre-selected set of nodes.
   micropayment
      A micropayment is a financial transaction involving a very small sum of money (<1 USD) and usually one that occurs online.
   sharding
      The splitting the space of possible accounts (contracts are accounts too) into subspaces, for example, based on first digits of their numerical addresses. This allows for contract executions to be executed within 'shards' instead of network wide, allowing for faster transactions and greater scalability.
   hash
      A cryptographic hash function is a hash function which takes an input (or 'message') and returns a fixed-size alphanumeric string, which is called the hash value (sometimes called a message digest, a digital fingerprint, a digest or a checksum).
   cryptofuel
      Similar to 'gas', referring to the amount of cryptocurrency required to power a transaction.
   cryptoeconomics
      The economics of cryptocurrencies.
   protocol
      A standard used to define a method of exchanging data over a computer network.
   block validation
      The checking of the coherence of the cryptographic signature of the block with the history stored in the entire blockchain.
   blocktime
      The average time interval between the mining of two blocks.
   difficulty
      The amount of effort required to mine a new block.
   network hashrate
      The number of hash calculations the network can make per second collectively.
   hashrate
      The number of hash calculations made per second.
   uncle
      Uncles are blockchain blocks found by a miner, when different miner has already found another block for the corresponding place in the blockchain. They are called “stale blocks”. The parent of an Uncle is an ancestor of the inserting block, located at the tip of the blockchain. In contrast to the Bitcoin network, Ethereum rewards stale blocks as well in order to avoid to penalise miners with a bad connection to the network. This is less critical In the Bitcoin network, because the Block Time there is much higher (~10 minutes) than on the Ethereum network (aimed to ~15 seconds, Frontier).

   ghost
      Greedy Heaviest-Observed Sub-Tree is an alternative chain-selection method that is designed to incentivise stale blocks (uncles) as well, thus reducing the incentive for pool mining. In GHOST, even the confirmation given by stale blocks to previous blocks are considered valid, and the miners of the stale blocks are also rewarded with a mining reward.
   patricia merkle tree
      Merkle Patricia trees provide a cryptographically authenticated data structure that can be used to store all (key, value) bindings. They are fully deterministic, meaning that a Patricia tree with the same (key,value) bindings is guaranteed to be exactly the same down to the last byte and therefore have the same root hash, provide the holy grail of O(log(n)) efficiency for inserts, lookups and deletes, and are much easier to understand and code than more complex comparison-based alternatives like red-black trees.
   DAG
      DAG stands for Directed Acyclic Graph. It is a graph, a set of nodes and links between nodes, that has very special properties.
      Ethereum uses a DAG in Ethash, the Ethereum Proof of Work (POW) algorithm.The Ethash DAG takes a long time to be generated, which is done by a Miner node into a cache file for each Epoch. The file data is then used when a value from this graph is required by the algorithm. Directed Acyclic Graph Daggerav.

   uncle rate
      The number of uncles produced per block.
   issueance
      The minting and granting of new cryptocurrency to a miner who has found a new block.
   presale
      Sale of cryptocurrency before the actual launch of the network.
   static node
      ?
   bootnode
      The nodes which can be used to initiate the discovery process when running a node. The endpoints of these nodes are recorded in the Ethereum source code.
   exchange
      An online marketplace which facilitate the exchange of crypto or fiat currencies based on the market exchange rate.
   compiler
      A program that translates pieces of code written in high level languages into low level executable code.
   genesis block
      The first block in a blockchain. 
   network id
      An number which identifies a particular version of the Ethereum network.
   block header
      The data in a block which is unique to its content and the circumstances in which it was created. It includes hash of the previous block's header, the version of the software the block is mined with, the timestamp and the merkle root hash of the contents of the block.
   pending transaction
      A transaction that is not yet confirmed by the Ethereum network.
   block propagation
      The process of transmitting a confirmed block to all other nodes in the network. 
   sidechain
      A blockchain that branches off a main blockchain and checks in periodically with the main blockchain. Besides that it runs independently from the main chain, and any security compromises in the sidechain will not affect the main chain.
   pegging
      Locking down the exchange rate of the coins/tokens in two chains (usually a main and a side chain) in a certain directiom.
   2-way pegging
      Locking down the exchange rate of the coins/tokens in two chains (usually a main and a side chain) in both directions.
   trustless
      Refers to the ability of a network to trustworthily mediate transactions without any of the involved parties to trust anyone else.
   faucet
      A website that dispenses (normally testnet) cryptocurrencies for free. 
   checksum
      A count of the number of bits in a transmission that is included with the unit so that the receiving end can verify that the entirety of the message has been transmitted.   
   ICAP
      Interexchange Client Address Protocol, an IBAN-compatible system for referencing and transacting to client accounts aimed to streamline the process of transferring funds, worry-free between exchanges and, ultimately, making KYC and AML concerns a thing of the past.
   private key
      A private key is a string of characters known only to the owner, that is paired with a public key to set off algorithms for text encryption and decryption.
   public key
      A string of characters derived from a private key that can be made public. The public key can be used to verify the authenticity of any signature created using the private key.
   encryption
      Encryption is the conversion of electronic data into a form unreadable by anyone except the owner of the correct decryption key.
   digital signature
      A mathematical scheme for demonstrating the authenticity of a digital message or documents.
   port
      A network port is a communication endpoint used by a one of the existing standards of establishing a network conversation (e.g. TCP, UDP).
   rpc
      Remote Procedure Call, a protocol that a program uses to request a service from a program located in another computer in a network without having to understand the network details.
   ipc
      Interprocess communication (IPC) is a set of programming interfaces that allow a programmer to coordinate activities among different program processes that can run concurrently in an operating system.
   attach
      The command used to initiate the Ethereum Javascript console. 
   daemon
      A computer program that runs as a background process instead of in direct control by an interactive user.
   system service
      
   base layer service
      Services such as SWARM and Whisper which are built into the Ethereum platform.
   js
      Javascript.
   syncing
      The process of downloading the entire blockchain.
   fast sync
      Instead of processing the entire block-chain one link at a time, and replay all transactions that ever happened in history, fast syncing downloads the transaction receipts along the blocks, and pulls an entire recent state database.
   asic
      Application-specific integrated circuit, in this case referring to an integrated circuit custom built for cryptocurrency mining.
   memory-hard
      Memory hard functions are processes that experiences a drastic decrease in speed or feasibility when the amount of available memory even slightly decreases.
   keyfile
      Every account's private key/address pair exists as a single keyfile. These are JSON text files which contains the encrypted private key of the account, which can only be decrypted with the password entered during account creation. 
   ICAP format
      The format of the IBANs defined using the `Inter-exchange Client Address Protocol <https://github.com/ethereumjs/ethereumjs-icap>`_.
   block(chain) explorer
      A website that allows easy searching and extraction of data from the blockchain.
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



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
   state
   
   blockchain
      An ever-extending series of data blocks that grows as new transactions are confirmed as part of a new block. Each new block is chained to the existing blockchain by a cryptographic proof-of-work.
   peer
      
   signing
      
   discovery (peer)
      
   gas price oracle
      
   light client
      
   etherbase
      
   coinbase
      
   balance
      
   solidity
      
   serpent

   evm
      
   virtual machine
      
   peer to peer network
      
   decentralisation
      
   distributed hash table
      
   NAT
      
   nonce
      Number Used Once or Number Once. A nonce, in information technology, is a number generated for a specific use, such as session authentication. Typically, a nonce is some value that varies with time, although a very large random number is sometimes used. In general usage, nonce means “for the immediate occasion” or “for now.”
      In the case of Blockchain Proof of Work scenarios, the hash value, found by a Miner, matching the network's Difficulty thus proving the Block Validity is called Nonce as well.

   proof of work
      Often seen in its abbreviated form "PoW", it refers to a mathematical value that can act act as the proof of having solved a resource and time consuming computational problem.
   proof of stake
      
   casper
      
   consensus
      
   homestead
      
   metropolis
      
   serenity
      
   frontier
      
   olympic
      
   morden
      
   testnet
      
   private chain
      
   consortium chain
      
   micropayment
      
   sharding
      
   hash
      
   cryptofuel
      
   cryptoeconomics
      
   protocol
      
   validation
      
   blocktime

   difficulty
      
   network hashrate
      
   hashrate
      
   uncle
      Uncles are blockchain blocks found by a miner, when different miner has already found another block for the corresponding place in the blockchain. They are called “stale blocks”. The parent of an Uncle is an ancestor of the inserting block, located at the tip of the blockchain. In contrast to the Bitcoin network, Ethereum rewards stale blocks as well in order to avoid to penalise miners with a bad connection to the network. This is less critical In the Bitcoin network, because the Block Time there is much higher (~10 minutes) than on the Ethereum network (aimed to ~15 seconds, Frontier).

   ghost
      
   patricia merkle tree
      
   DAG
      DAG stands for Directed Acyclic Graph. It is a graph, a set of nodes and links between nodes, that has very special properties.
      Ethereum uses a DAG in Ethash, the Ethereum Proof of Work (POW) algorithm.The Ethash DAG takes a long time to be generated, which is done by a Miner node into a cache file for each Epoch. The file data is then used when a value from this graph is required by the algorithm. Directed Acyclic Graph Daggerav.

   uncle rate
      
   issueance
      
   presale
      
   static node
      
   bootnode
      
   exchange
      
   compiler
      
   genesis block
      
   network id
      
   block header
      
   pending transaction
            
   block propagation
      
   sidechain
      
   pegging
      
   2-way peg
      
   trustless
      
   two weeks
      
   faucet
      
   checksum
      
   ICAP
      
   private key
      
   public key
      
   encryption
      
   digital signature
      
   port
      
   rpc
      
   ipc
      
   attach
      
   daemon
      
   system service
      
   base layer service
      
   js
      
   syncing
      
   fast sync
      
   propagation
      
   gpu/cpu (mining)
      
   asic
      
   memory-hard
      
   keyfile
      
   ICAP format
      
   block(chain) explorer
      
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



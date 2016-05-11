################################################################################
Frequently Asked Questions
################################################################################

.. contents::
  :local:
  :depth: 2

Questions
==============================================================================================

What is Ethereum?
----------------------------------------------------------------------------------------------
Ethereum is a decentralized smart contracts platform that is powered by a cryptocurrency called Ether. A good starting point to learn more about it's workings would be the ":ref:`what-is-ethereum`" page.

I have heard of Ethereum, but what are Geth, Mist, Ethminer, Mix?
----------------------------------------------------------------------------------------------

* **Geth**: This is the Go implementation of an Ethereum node, and is the basis for any interactions with the Ethereum blockchain. Running this locally will allow you to easily interact with the Ethereum blockchain. Read the `go-ethereum installation instructions <https://github.com/ethereum/go-ethereum/wiki/Building-Ethereum>`_.

* **Mist**: This is the equivalent of a web browser, but for the Ethereum platform. It acts as a GUI to display the accounts and contracts that you interact with. It also allows you to create and interact with contracts in a graphical user interface without ever touching the command line. If you are not a developer and just want to store Ether and interact with Ethereum contracts, then Mist is the program to use. Downloads can be found on the `Mist releases page  <https://github.com/ethereum/mist/releases>`_.

* **Ethminer**: A standalone miner. This can be used to mine or benchmark a mining set-up. It is compatible with eth, geth, and pyethereum. Check out the :ref: `mining` page for more information.

* **Mix**: The integrated development environment for DApp authoring. Quickly prototype and debug decentralised applications on the Ethereum platform. More information can be found at the `Mix GitHub Page <https://github.com/ethereum/mix>`_.

How can I store big files on the blockchain?
----------------------------------------------------------------------------------------------
In general you do not want to store large files or pieces of data in the Ethereum blockchain because of the high cost of storage. You will need to use a third party storage solution, such as Swarm or IPFS. Swarm is an Ethereum-specific project for distributed file storage. IPFS is an non-Ethereum project which has close ties to Ethereum; it will be used independently and may be used as an added layer underlying Swarm in the future. See `this Ethereum StackExchange post on the topic <http://ethereum.stackexchange.com/questions/1000/what-are-some-proposed-ways-of-storing-data-in-ethereum/1001#1001>`_ for more information.

Is Ethereum based on Bitcoin?
----------------------------------------------------------------------------------------------
Only in the sense that it uses a blockchain, which Bitcoin pioneered. Ethereum has a separate blockchain that has several significant technical differences from Bitcoin's blockchain. See `this Ethereum StackExchange answer <http://ethereum.stackexchange.com/questions/700/what-are-the-differences-between-bitcoin-blockchain-and-ethereum-blockchain>`_ for a detailed explanation.

What's the future of Ethereum?
----------------------------------------------------------------------------------------------
Ethereum developers are planning a switch from a Proof-of-Work consensus model to a Proof-of-Stake consensus model in the future. They are also investigating scalability solutions and how to store secrets on the blockchain.

What's the difference between account and "wallet contract"?
----------------------------------------------------------------------------------------------
An account is your public / private key pair file that serves as your identity on the blockchain. See "account" in the glossary. A "wallet contract" is an Ethereum contract that secures your ether and identity with features such as multisignature signing and programmed deposit/withdrawal limits. A wallet contract can be easily created in the Mist Ethereum Wallet GUI client.

Are keyfiles only accessible from the computer you downloaded the client on?
----------------------------------------------------------------------------------------------
No, you are welcome to export or move the keyfile, but always remember to backup your keyfiles and be aware of which computers you store your keyfile on.

How long should it take to download the blockchain?
----------------------------------------------------------------------------------------------
The Ethereum blockchain is constantly growing, and is nearing 10GB as of March 2016. The amount of time it will take to download depends on the amount of peers you are able to connect to, your internet connection speed, and other factors. See the :ref: `download-the-blockchain-faster` section for tips on syncing the blockchain more quickly.

How do I get a list of transactions into/out of an address?
----------------------------------------------------------------------------------------------
You would have to pull the transactions manually out of the blockchain to achieve this. Alternatively, you can rely on third party explorers' API's like `Etherchain <https://etherchain.org/apidoc>`_. For contract execution transactions however, you can filter the contract logs to achieve this.

Can a contract pay for its execution?
----------------------------------------------------------------------------------------------
No this is not possible. The gas for the execution must be provided by the address submitting the execution request.

Can a contract call another contract?
----------------------------------------------------------------------------------------------
Yes, this is possible, read `about interactions between contracts <https://dappsforbeginners.wordpress.com/tutorials/interactions-between-contracts/>`_.

Can a transaction be signed offline and then submitted on another online device?
----------------------------------------------------------------------------------------------
Yes, you can refer to the solution from `Icebox <https://github.com/ConsenSys/icebox>`_.

How to get testnet Ether?
----------------------------------------------------------------------------------------------
See :ref: `test-networks`.

Can a transaction be sent by a third party? i.e can transaction broadcasting be outsourced
----------------------------------------------------------------------------------------------
Technically yes, but there is an important restriction as opposed to bitcoin signed transactions: in ethereum the transaction has a nonce (more precisely, each account increases a counter when sending a transaction based on how many transactions total have been sent. If 3 transactions have ever been sent from the account, the account nonce would be 3).

Can Ethereum contracts pull data using third-party APIs?
----------------------------------------------------------------------------------------------
No, Ethereum contracts cannot pull data from external information sources in this way. It is however possible to push data from external sites (e.g. weather sites, stock prices) to Ethereum contracts through transactions. There are "oracle" services that are compatible with the Ethereum network that will pull/push data to the Ethereum network for a fee.

Is the content of the data and contracts sent over the Ethereum network encrypted?
----------------------------------------------------------------------------------------------
Data and contracts on the Ethereum network are encoded, but not encrypted. Everyone can audit the behavior of the contracts and the data sent to them. However, you are always free to encrypt data locally before broadcasting it to the network.

Can I store secrets or passwords on the Ethereum network?
----------------------------------------------------------------------------------------------
All data on Ethereum is public. It is not possible to store secrets or passwords in Ethereum contracts without it being seen by all. There is work being done to make this a possibility through code obfuscation and other techniques. A good read would be this article by `Vitalik Buterin <https://blog.ethereum.org/2016/01/15/privacy-on-the-blockchain/>`_.

How will Ethereum combat centralisation of mining pools?
----------------------------------------------------------------------------------------------
There are two primary ways that the Ethereum PoW based consensus algorithm combats mining centralisation (`Source <http://ethereum.stackexchange.com/questions/549/how-does-ethereum-avoid-mining-pool-centralization>`_).

* The first is by reducing losses due to orphaned blocks, which independent miners are more likely to experience.

  * This portion of the Ethereum mining algorithm, a technique referred to as GHOST, includes the headers only of recently orphaned blocks in return for a reduced reward to both the block producer and the includer of the (otherwise orphaned) block. These included orphans from "grandparent" or earlier blocks are frequently referred to as "uncle" blocks because the gender neutral term "ommer" isn't widely known or understood.

* The second way that the Ethereum PoW consensus algorithm combats mining centralisation is by its use of a Proof of Work function that is ASIC resistant.

  * By preventing mining from becoming dominated by specially designed and produced hardware, independent miners are kept competitive or even given an advantage in terms of their profits and/or levels of hardware investment, because they can make use of readily available commodity hardware (i.e. consumer graphics cards).

How will Ethereum deal with ever increasing blockchain size?
----------------------------------------------------------------------------------------------
There are many discussions around blockchain scalability. This questioned has been partially answered on `this Ethereum StackExchange post <http://ethereum.stackexchange.com/questions/521/what-does-it-mean-to-run-code-on-the-blockchain-wouldnt-blockchain-become-hu>`_ and `this blog post from Vitalik Buterin <https://blog.ethereum.org/2014/02/18/ethereum-scalability-and-decentralization-updates/>`_.

How will Ethereum ensure the network is capable of making 10,000+ transactions-per-second?
----------------------------------------------------------------------------------------------
Ethereum is planning on implementing a proof-of-stake consensus protocol change during the Serenity phase of their development roadmap. More information on the likely Ethereum PoS candidate and how it may increase transactions-per-second can be `found here <https://blog.ethereum.org/2015/08/01/introducing-casper-friendly-ghost/>`_.

Where do the contracts reside?
----------------------------------------------------------------------------------------------
TODO

Your question is still not answered?
----------------------------------------------------------------------------------------------
Ask the community on `Ethereum StackExchange <http://ethereum.stackexchange.com/>`_.

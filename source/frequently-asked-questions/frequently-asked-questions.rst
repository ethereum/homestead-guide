################################################################################
Frequently Asked Questions
################################################################################
* **I have heard of Ethereum, but what are Geth, Mist, Ethminer AlethZero and AlethOne?**
  As you already know, Ethereum is the blockchain-based smart contract platform that this Wiki describes. Akin to Bitcoin, Ethereum needs miners to solve cryptographic puzzles to confirm transactions and bring cryptocurrency into existence, nodes to witness and record any transactions/computations made and 'wallets' to initiate transactions/computations.
    * **Geth**: This is the Go implementation of an Ethereum node, and is the basis for any interactions with the Ethereum blockchain. Running this locally will allow you to easily interact with the Ethereum blockchain.
    * **Mist**: This is the equivalent of a web browser, but then for the Ethereum platform. It acts as a GUI to display the accounts and contracts that you have or use on the Ethereum blockchain. It also allows you to create and interact with contracts in a graphical user interface without ever touching the command line. If you are not a developer and just want to store Ether and interact with Ethereum contracts, then Mist is the program to use. 
    * **AlethZero/AlethOne**: These are hardcore clients for working with Ethereum, with AlethOne being the later version. Once Geth is running in the background, you can use these to deploy contracts, mine for ether, set up private blockchains, etc. 
    * **Ethminer**: This is the dedicated software to use if you want to mine ether.

* **How can I store big files on the blockchain?**
  Swarm_ is an Ethereum-specific project for distributed file storage. IPFS_ is an independent project which has close ties to Ethereum; it will be used independently and may be used as the layer underlying Swarm.
* **Is ethereum based on bitcoin?**
  Only in the sense that it uses a blockchain, which Bitcoin pioneered. Ethereum has a separate blockchain that has several signigicant technical differences from Bitcoin.
* **What other cool apps are being built?** See this list from Ethercasts_.
* **What's the future of Ethereum?** We are planning a switch to Proof of Stake_ in the near future. We are also investigating scalability_ solutions and how to store_ secrets on the blockchain

* **How can I use Ethereum to get information about the future?**
  Augur_ and Gnosis_ are building prediction markets that try to gather the best information about uncertain future events

.. _Swarm: https://www.youtube.com/watch?v=VOC45AgZG5Q&index=11&list=PLJqWcTqh_zKHQUFX4IaVjWjfT2tbS4NVk
.. _IPFS: http://ipfs.io
.. _Ethercasts: http://dapps.ethercasts.com/
.. _Stake: https://www.youtube.com/watch?v=7Y3fWXA6d5k&index=3&list=PLJqWcTqh_zKHQUFX4IaVjWjfT2tbS4NVk
.. _scalability: https://www.youtube.com/watch?v=7Y3fWXA6d5k&index=3&list=PLJqWcTqh_zKHQUFX4IaVjWjfT2tbS4NVk
.. _store: https://blog.ethereum.org/2014/12/26/secret-sharing-daos-crypto-2-0/
.. _Augur: http://www.augur.net/
.. _Gnosis: http://groupgnosis.com/

FAQ1) How is Ethereum better than Bitcoin?

2) How is Ethereum better than Ripple?

3) How is Ethereum better than MaidSafeCoin?

4) How will Ethereum deal with ever increasing blockchain size? It is currently a problem with Bitcoin, current blockchain is over 40GB and growing.

5) How will Ethereum deal with centralisation of mining pools? This was a problem with BTC.

6) How will Ethereum deal with forking?

7) How will Ethereum ensure the network is capable of making 10000 transactions per second and not 1 transaction like Bitcoin? This is a problem for mainstream adoption.

8) How will Ethereum deal with all security issues plaguing Bitcoin?


    Permits all sorts of contracts, allows for faster TXs, will utilise eco-friendly validation.
    It's a trustless system. Not another IOU system.
    Solves more important issues.
    A number of solutions, primarily blockchain sharding.
    Through carefully structured incentives.
    How can anyone deal with forking?
    Through the use of POS validation and aforementioned scaling solutions.
    What security issues?

What's the difference between account and wallet contract?


An account is the primary thing you need, it's your public / private key pair. A wallet is a smart contract that can secure your ETH better than just an account (multisig / daily limit / etc).

Is your wallet only accessible from the computer you downloaded the client on?

I want to sell products for Ether

How long should it take to download the blockchain? self.ethereum

https://www.reddit.com/r/ethereum/comments/4628s0/couple_of_questions_about_ethereum/


https://www.reddit.com/r/ethereum/comments/461ub7/one_cannot_see_the_source_code_of_a_running/


http://ethereum.stackexchange.com/questions/1239/what-is-the-recommended-way-to-safely-store-ether

How do I get a list of transactions into/out-of an address?
ave to pull all the tx'es out of the blockchain and copy them into a db. (or use contracts, which isn't possible in this case)

https://github.com/ethereum/go-ethereum/issues/1897


can a contract pay for its execution ?

can a contract call another contract

can a contract call another contract specfed an input parameter

can a transaction be signed offline

which client is the fastest? :)



################################################################################
Frequently Asked Questions
################################################################################
* **What is Ethereum?** Ethereum is a decentralized smart contracts platform that is powered by a cryptocurrency called Ether. A good starting point to learn more about its workings would be the `Wiki <https://github.com/ethereum/wiki/wiki/What-is-Ethereum>`_.

* **I have heard of Ethereum, but what are Geth, Mist, Ethminer, Mix, and AlethOne?**
  As you already know, Ethereum is the blockchain-based smart contract platform that this Wiki describes. Akin to Bitcoin, Ethereum needs miners to solve cryptographic puzzles to confirm transactions and bring cryptocurrency into existence, nodes to witness and record any transactions/computations made and 'wallets' to initiate transactions/computations.
    * **Geth**: This is the Go implementation of an Ethereum node, and is the basis for any interactions with the Ethereum blockchain. Running this locally will allow you to easily interact with the Ethereum blockchain.
    * **Mist**: This is the equivalent of a web browser, but then for the Ethereum platform. It acts as a GUI to display the accounts and contracts that you have or use on the Ethereum blockchain. It also allows you to create and interact with contracts in a graphical user interface without ever touching the command line. If you are not a developer and just want to store Ether and interact with Ethereum contracts, then Mist is the program to use. Latest releases can be found here: https://github.com/ethereum/mist/releases . 
    * **AlethOne**: The mainline Ethereum desktop miner. It connects and syncs to the Ethereum network and lets you mine, and send transactions. It will also let you do pool mining.  
    * **Ethminer**: A standalone miner. This can be used to check how fast you can mine and will mine for you in concert with eth, geth and pyethereum.
    * **Mix**: The integrated development environment for DApp authoring. Quickly prototype and debug decentralised applications on the Ethereum platform.
* **How can I store big files on the blockchain?**
  Swarm is an Ethereum-specific project for distributed file storage. IPFS is an independent project which has close ties to Ethereum; it will be used independently and may be used as the layer underlying Swarm.
* **Is Ethereum based on bitcoin?**
  Only in the sense that it uses a blockchain, which Bitcoin pioneered. Ethereum has a separate blockchain that has several signigicant technical differences from Bitcoin.
* **What other cool apps are being built?** See this list from Ethercasts.
* **What's the future of Ethereum?** We are planning a switch to Proof of Stake_ in the near future. We are also investigating scalability_ solutions and how to store_ secrets on the blockchain

* **How can I use Ethereum to get information about the future?**
  Augur and Gnosis are building prediction markets that try to gather the best information about uncertain future events. Besides that, there are also other interesting Ethereum-related projects on the market:
    * `Swarm <https://www.youtube.com/watch?v=VOC45AgZG5Q&index=11&list=PLJqWcTqh_zKHQUFX4IaVjWjfT2tbS4NVk>`_
    * `IPFS <http://ipfs.io>`_
    * `Ethercasts  <http://dapps.ethercasts.com/>`_
    * `Stake  <https://www.youtube.com/watch?v=7Y3fWXA6d5k&index=3&list=PLJqWcTqh_zKHQUFX4IaVjWjfT2tbS4NVk>`_
    * `Scalability  <https://www.youtube.com/watch?v=7Y3fWXA6d5k&index=3&list=PLJqWcTqh_zKHQUFX4IaVjWjfT2tbS4NVk>`_
    * `Store  <https://blog.ethereum.org/2014/12/26/secret-sharing-daos-crypto-2-0/>`_
    * `Augur  <http://www.augur.net/>`_
    * `Gnosis  <http://groupgnosis.com/>`_

* **How is Ethereum better than Bitcoin, Ripple, MaidSafeCoin and other cryptocurrencies?** While all these platforms have a currency associated with it, that is where the similarity ends. Ethereum is currently then only platform that allows for decentralized computing through smart contracts. As the Ethereum platform is 'Turing complete', you can build not just new cryptocurrencies and gross settlement systems (a la Ripple), but also many other applications that are not possible on any other platforms.

* **What's the difference between account and wallet contract?** An account is basically your public / private key pair. A wallet is a smart contract that secures your ether and identity with features such as multisignature signing, new addresses for each transaction and password protection. 

* **Is your wallet only accessible from the computer you downloaded the client on?** Yes, if you are using Mist. You can of course export it for use on another computer.

* **How long should it take to download the blockchain? self.ethereum** The Ethereum blockchain is constantly growing, and is nearing 7gb as of February 2016. It can take an hour or two to download. 

* **How can I safely store my ether?** Here are the possible ways to store ether:
    * Accounts
        * Mist/Geth accounts.
        * Paper wallets.
        * Brain wallets.
        * Icebox Air gapped offline signing of transactions
    * Wallet
        * `Mist Multi\-signature <http://ethereum.stackexchange.com/questions/6/how-can-i-create-a-multisignature-address-on-ethereum>_`

* **How do I get a list of transactions into/out-of an address?** You would have to pull the transactions manually out of the blockchain to achieve this. Alternatively, you can rely on thirdparty explorers' API's like `Etherchain <https://etherchain.org/apidoc>`_. For contract execution transactions however, you can filter the logs to achieve this. 

* **Can a contract pay for its execution?** No this is not possible. The gas for the execution must be provided by the address submitting the execution request.

* **Can a contract call another contract?** Yes, this is possible see https://dappsforbeginners.wordpress.com/tutorials/interactions-between-contracts/.

* **Can a transaction be signed offline and then submitted on another online device?** Yes, you can refer to the solution from `Icebox <https://github.com/ConsenSys/icebox>`_.

* **which client is the fastest and most reliable?** For now, the Mist browser is definitely the most stable, reliable and fastest Ethereum client. 

* **How to get testnet Ether?** Testnet ether can either be mined yourself (using Mist for example), or requested from Testnet faucets like: faucet.etherparty.io/ .

* **Can a transaction be sent by a third party? i.e can transaction broadcasting be outsourced** Technically yes but there is an important restriction as opposed to bitcoin signed transactions: in ethereum the transaction has a nonce (more precisely, each account increases counter). 

* **Can Ethereum contracts pull data using third-party APIs?** No, Ethereum contracts cannot pull data from external information sources in this way. It is however possible to push data from external sites (e.g. weather sites, stock prices) to Ethereum contracts through transactions.

* **Is the content of the data and contracts sent over the Ethereum network encrypted?** Data and contracts on the Ethereum network are are encoded, but not encrypted. The purpose of Ethereum is precisely that everyone can audit the behaviour of the contracts and the data sent to them. However, you are always free to encrypt data locally before broadcasting it to the network. 

* **Can I store secrets or passwords on the Ethereum network so that contracts can interact with fiat and other cryptocurrencies?** All data on Ethereum is public. It is not possible to store secrets or passwords to internet banking sites in Ethereum contracts without it being seen by all. There is however work being done to make this a possibility through code obfuscation and other techniques. A good read would be this article by Vitalik Buterin (https://blog.ethereum.org/2016/01/15/privacy-on-the-blockchain/).

##### Need help with thorough expert comments on these questions######

* How will Ethereum deal with ever increasing blockchain size? It is currently a problem with Bitcoin, current blockchain is over 40GB and growing.

* How will Ethereum deal with centralisation of mining pools? This was a problem with BTC.

* How will Ethereum deal with forking?

* How will Ethereum ensure the network is capable of making 10000 transactions per second and not 1 transaction like Bitcoin? This is a problem for mainstream adoption.


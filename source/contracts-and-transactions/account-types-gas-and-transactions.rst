.. _account-types-gas-and-transactions:

********************************************************************************
Account Types, Gas, and Transactions
********************************************************************************

EOA vs contract accounts
================================================================================

There are two types of accounts in Ethereum
  - Externally Owned Accounts
  - Contracts Accounts

Externally owned accounts (EOAs)
--------------------------------------------------------------------------------

- Can have an Ether balance.
- Can send transactions.
- Are controlled by private keys.
- Has no code.

Contract accounts
--------------------------------------------------------------------------------
- Can have an Ether balance.
- Can send transactions.
- Can send messages.
- Contracts are controlled by their contract code.
- Only send transactions in response to other transactions that they have received. Therefore, all action on the Ethereum block chain is set in motion by transactions fired from externally owned accounts.
- Every time a contract account receives a transaction its code activates, allowing it to read and write to internal storage and send other transactions/messages or create contracts.

All Ether balances and values are denominated in units of wei: 1 Ether is 1e18 wei.

.. note:: "Contracts" in Ethereum should not be seen as something that should be "fulfilled" or "complied with"; rather, they are more like "autonomous agents" that live inside of the Ethereum execution environment, always executing a specific piece of code when "poked" by a message or transaction, and having direct control over their own ether balance and their own key/value store to keep track of persistent variables.

What is a transaction?
================================================================================
The term "transaction" is used in Ethereum to refer to the signed data package that stores a message to be sent from an externally owned account.

Transactions contain:
 - The recipient of the message.
 - A signature identifying the sender.
 - ``VALUE`` field - The amount of wei to transfer from the sender to the recipient.
 - An optional data field.
 - A ``STARTGAS`` value, representing the maximum number of computational steps the transaction execution is allowed to take.
 - A ``GASPRICE`` value, representing the fee the sender pays per computational step.

What is a message?
================================================================================
Contracts have the ability to send "messages" to other contracts. Messages are virtual objects that are never serialized and exist only in the Ethereum execution environment.

A message contains:
 - The sender of the message (implicit).
 - The recipient of the message.
 - ``VALUE`` field - The amount of wei to transfer alongside the message to the contract address.
 - An optional data field.
 - A ``STARTGAS`` value.

Essentially, a message is like a transaction, except it is produced by a contract and not an external actor. A message is produced when a contract currently executing code executes the ``CALL`` opcode, which produces and executes a message. Like a transaction, a message leads to the recipient account running its code. Thus, contracts can have relationships with other contracts in exactly the same way that external actors can.

What is gas?
================================================================================
Ethereum implements an execution environment on the blockchain called the Ethereum Virtual Machine (EVM). When you are running a decentralized application (dApp), every instruction is executed on every node of the network. This has a cost: for every operation in a contract that can be executed there is a specified cost, expressed in number of gas units.

Gas is name for the execution fee for every operation made on an Ethereum blockchain. Its price is expressed in ether and it's decided by the miners, which can refuse to process transaction with less than a certain gas price. To get gas you simply need to add ether to your account. The Ethereum client automatically converts Ether to gas and gas to Ether when transactions are processed.

The Ethereum protocol charges a fee per computational step that is executed in a contract or transaction to prevent deliberate attacks and abuse on the Ethereum network. Every transaction is required to include a gas limit and a fee that it is willing to pay per gas. Miners have the choice of including the transaction and collecting the fee or not. If the total number of gas used by the computational steps spawned by the transaction, including the original message and any sub-messages that may be triggered, is less than or equal to the gas limit, then the transaction processes. If the total gas exceeds the gas limit, then all changes are reverted, except that the transaction is still valid and the fee can still be collected by the miner. This means that it is wiser to send transactions with a gas limit well above the estimates

Estimating transaction costs
================================================================================
The total cost of a transaction is based on 2 factors:

``gasUsed`` is the total gas that is consumed by the transaction

``gasPrice`` price (in ether) of one unit of gas specified in the transaction

**Total cost = gasUsed * gasPrice**

gasUsed
--------------------------------------------------------------------------------
Each operation in the EVM was assigned a number of how much gas it consumes. ``gasUsed`` is summing up all the gas for all the operations executed. There is a `spreadsheet <http://ethereum.stackexchange.com/q/52/42>`_ which offers a glimpse to some of the analysis behind them.

For estimating ``gasUsed``, there is an `estimateGas API <http://ethereum.stackexchange.com/q/266/42>`_ that can be used but has some caveats.

gasPrice
--------------------------------------------------------------------------------
A user constructs and signs a transaction, and each user may specify whatever ``gasPrice`` they desire, this includes zero. However, the Ethereum clients launched at Frontier had a default gasPrice of 0.05e12 wei. As miners optimize for their revenue, if most transactions are being submitted with a gasPrice of 0.05e12 wei, it would be difficult to convince a miner to accept a transaction that specified a lower, or zero, gasPrice.

Example transaction cost
--------------------------------------------------------------------------------

Let’s take a contract that just adds 2 numbers. The EVM OPCODE ``ADD`` consumes 3 gas.

The approximate cost, using the default gas price (as of January 2016), would be:

3 \* 0.05e12 = 1.5e11 wei

Since 1 Ether is 1e18 wei, the total cost would be 0.00000015 Ether.

This is a simplification since it ignores some costs, such as the cost
of passing the 2 numbers to contract, before they can even be added.

* `question <http://ethereum.stackexchange.com/q/324/42>`_
* `gas fees <http://ether.fund/tool/gas-fees>`_
* `gas cost calculator <http://ether.fund/tool/calculator>`_
* `Ethereum Gas Prices <https://docs.google.com/spreadsheets/d/1m89CVujrQe5LAFJ8-YAUCcNK950dUzMQPMJBxRtGCqs>`_

=================  =========    =============================
Operation Name     Gas Cost     Remark
=================  =========    =============================
step               1            default amount per an execution cycle
stop               0            free
suicide            0            free
sha3               20
sload              20           get from permanent storage
sstore             100          put into permanent storage
balance            20
create             100          contract creation
call               20           initiating a read only call
memory             1            every additional word when expanding memory
txdata             5            every byte of data or code for a transaction
transaction        500          base fee transaction
contract creation  53000        changed in homestead from 21000
=================  =========    =============================

Account interactions example - betting contract
================================================================================
As previously mentioned, there are two types of accounts:

* **Externally owned account (EOAs)**: an account controlled by a private key, and if you own the private key associated with the EOA you have the ability to send ether and messages from it.
* **Contract**: an account that has its own code, and is controlled by code.

By default, the Ethereum execution environment is lifeless; nothing happens and the state of every account remains the same. However, any user can trigger an action by sending a transaction from an externally owned account, setting Ethereum's wheels in motion. If the destination of the transaction is another EOA, then the transaction may transfer some ether but otherwise does nothing. However, if the destination is a contract, then the contract in turn activates, and automatically runs its code.

The code has the ability to read/write to its own internal storage (a database mapping 32-byte keys to 32-byte values), read the storage of the received message, and send messages to other contracts, triggering their execution in turn. Once execution stops, and all sub-executions triggered by a message sent by a contract stop (this all happens in a deterministic and synchronous order, ie. a sub-call completes fully before the parent call goes any further), the execution environment halts once again, until woken by the next transaction.

Contracts generally serve four purposes:

* Maintain a data store representing something which is useful to either other contracts or to the outside world; one example of this is a contract that simulates a currency, and another is a contract that records membership in a particular organization.
* Serve as a sort of externally owned account with a more complicated access policy; this is called a "forwarding contract" and typically involves simply resending incoming messages to some desired destination only if certain conditions are met; for example, one can have a forwarding contract that waits until two out of a given three private keys have confirmed a particular message before resending it (ie. multisig). More complex forwarding contracts have different conditions based on the nature of the message sent; the simplest use case for this functionality is a withdrawal limit that is overrideable via some more complicated access procedure.
* Manage an ongoing contract or relationship between multiple users. Examples of this include a financial contract, an escrow with some particular set of mediators, or some kind of insurance. One can also have an open contract that one party leaves open for any other party to engage with at any time; one example of this is a contract that automatically pays a bounty to whoever submits a valid solution to some mathematical problem, or proves that it is providing some computational resource.
* Provide functions to other contracts; essentially serving as a software library.

Contracts interact with each other through an activity that is alternately called either "calling" or "sending messages". A "message" is an object containing some quantity of ether (a special internal currency used in Ethereum with the primary purpose of paying transaction fees), a byte-array of data of any size, the addresses of a sender and a recipient. When a contract receives a message it has the option of returning some data, which the original sender of the message can then immediately use. In this way, sending a message is exactly like calling a function.

Because contracts can play such different roles, we expect that contracts will be interacting with each other. As an example, consider a situation where Alice and Bob are betting 100 GavCoin that the temperature in San Francisco will not exceed 35ºC at any point in the next year. However, Alice is very security-conscious, and as her primary account uses a forwarding contract which only sends messages with the approval of two out of three private keys. Bob is paranoid about quantum cryptography, so he uses a forwarding contract which passes along only messages that have been signed with Lamport signatures alongside traditional ECDSA (but because he's old fashioned, he prefers to use a version of Lamport sigs based on SHA256, which is not supported in Ethereum directly).

The betting contract itself needs to fetch data about the San Francisco weather from some contract, and it also needs to talk to the GavCoin contract when it wants to actually send the GavCoin to either Alice or Bob (or, more precisely, Alice or Bob's forwarding contract). We can show the relationships between the accounts thus:

..  image:: ../img/contract_relationship.png
..
   :align: center

When Bob wants to finalize the bet, the following steps happen:

1. A transaction is sent, triggering a message from Bob's EOA to Bob's forwarding contract.
2. Bob's forwarding contract sends the hash of the message and the Lamport signature to a contract which functions as a Lamport signature verification library.
3. The Lamport signature verification library sees that Bob wants a SHA256-based Lamport sig, so it calls the SHA256 library many times as needed to verify the signature.
4. Once the Lamport signature verification library returns 1, signifying that the signature has been verified, it sends a message to the contract representing the bet.
5. The bet contract checks the contract providing the San Francisco temperature to see what the temperature is.
6. The bet contract sees that the response to the messages shows that the temperature is above 35ºC, so it sends a message to the GavCoin contract to move the GavCoin from its account to Bob's forwarding contract.

Note that the GavCoin is all "stored" as entries in the GavCoin contract's database; the word "account" in the context of step 6 simply means that there is a data entry in the GavCoin contract storage with a key for the bet contract's address and a value for its balance. After receiving this message, the GavCoin contract decreases this value by some amount and increases the value in the entry corresponding to Bob's forwarding contract's address. We can see these steps in the following diagram:

..  image:: ../img/contract_relationship2.png
..
   :align: center

Signing transactions offline
================================================================================
[ Maybe add this to the FAQ and point to the ethkey section of turboethereum guide? ]

* `Resilience Raw Transaction Broadcaster <https://github.com/resilience-me/broadcaster/>`_
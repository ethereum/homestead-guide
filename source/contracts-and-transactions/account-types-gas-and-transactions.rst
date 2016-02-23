********************************************************************************
Account Types, Gas, and Transactions
********************************************************************************

EOA vs Contract Accounts
================================================================================

There are two types of accounts in Ethereum
  - Externally Owned Accounts
  - Contracts Accounts

Externally Owned Accounts (EOAs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Can have an Ether balance.
- Can send transactions.
- Are controlled by private keys.
- Has no code.

Contract Accounts:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Can have an Ether balance.
- Can send transactions.
- Can send messages.
- Contracts are controlled by their contract code.
- Only send transactions in response to other transactions that they have received. Therefore, all action on the Ethereum block chain is set in motion by transactions fired from externally owned accounts.
- Every time a contract account receives a transaction it's code activates, allowing it to read and write to internal storage and send other transactions/messages or create contracts.

Note that "contracts" in Ethereum should not be seen as something that should be "fulfilled" or "complied with"; rather, they are more like "autonomous agents" that live inside of the Ethereum execution environment, always executing a specific piece of code when "poked" by a message or transaction, and having direct control over their own ether balance and their own key/value store to keep track of persistent variables.

What is a Transaction?
================================================================================
The term "transaction" is used in Ethereum to refer to the signed data package that stores a message to be sent from an externally owned account.

Transactions contain:
 - The recipient of the message.
 - A signature identifying the sender.
 - ``VALUE`` field - The amount of ether to transfer from the sender to the recipient.
 - An optional data field.
 - A ``STARTGAS`` value, representing the maximum number of computational steps the transaction execution is allowed to take.
 - A ``GASPRICE`` value, representing the fee the sender pays per computational step.

What is a Message?
================================================================================
Contracts have the ability to send "messages" to other contracts. Messages are virtual objects that are never serialized and exist only in the Ethereum execution environment.

A message contains:
 - The sender of the message (implicit).
 - The recipient of the message.
 - ``VALUE`` field - The amount of ether to transfer alongside the message to the contract address.
 - An optional data field.
 - A ``STARTGAS`` value.

Essentially, a message is like a transaction, except it is produced by a contract and not an external actor. A message is produced when a contract currently executing code executes the ``CALL`` opcode, which produces and executes a message. Like a transaction, a message leads to the recipient account running its code. Thus, contracts can have relationships with other contracts in exactly the same way that external actors can.

What is Gas?
================================================================================
Ethereum implements an execution environment on the blockchain called the Ethereum Virtual Machine (EVM). When you are running a decentralized application (dApp), every instruction is executed on every node of the network. This has a cost: for every operation in a contract that can be executed there is a specified cost, expressed in number of gas units.

Gas is name for the execution fee for every operation made on an Ethereum blockchain. Its price is expressed in ether and it's decided by the miners, which can refuse to process transaction with less than a certain gas price. To get gas you simply need to add ether to your account. The Ethereum client automatically converts Ether to gas and gas to Ether when transactions are processed.

The Ethereum protocol charges a fee per computational step that is executed in a contract or transaction to prevent deliberate attacks and abuse on the Ethereum network. Every transaction is required to include a gas limit and a fee that it is willing to pay per gas. Miners have the choice of including the transaction and collecting the fee or not. If the total number of gas used by the computational steps spawned by the transaction, including the original message and any sub-messages that may be triggered, is less than or equal to the gas limit, then the transaction processes. If the total gas exceeds the gas limit, then all changes are reverted, except that the transaction is still valid and the fee can still be collected by the miner. This means that it is wiser to send transactions with a gas limit well above the estimates

Estimating Transaction Costs
================================================================================
The total cost of a transaction is based on 2 factors:

``gasUsed`` is the total gas that is consumed by the transaction

``gasPrice`` price (in ether) of one unit of gas specified in the transaction

**Total cost = gasUsed * gasPrice**

gasUsed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each operation in the EVM was assigned a number of how much gas it consumes. ``gasUsed`` is summing up all the gas for all the operations executed. There is a `spreadsheet <http://ethereum.stackexchange.com/q/52/42>`_ which offers a glimpse to some of the analysis behind them.

For estimating ``gasUsed``, there is an `estimateGas API <http://ethereum.stackexchange.com/q/266/42>`_ that can be used but has some caveats.

gasPrice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A user constructs and signs a transaction, and each user may specify whatever ``gasPrice`` they desire, this includes zero. However, the Ethereum clients launched at Frontier had a default gasPrice of 0.05e12 wei. As miners optimize for their revenue, if most transactions are being submitted with a gasPrice of 0.05e12 wei, it would be difficult to convince a miner to accept a transaction that specified a lower, or zero, gasPrice.

Example Transaction Cost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
operation name     gas cost     Remark
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

Lifecycle of a Transaction
================================================================================
.. todo::
   Lifecycle of a Transaction

Signing Transactions Offline
================================================================================
[ Maybe add this to the FAQ and point to the ethkey section of turboethereum guide? ]

* `Resilience Raw Transaction Broadcaster <https://github.com/resilience-me/broadcaster/>`_


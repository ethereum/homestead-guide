********************************************************************************
Account Types, Gas, and Transactions
********************************************************************************

EOA vs Contract Accounts
================================================================================
There are two types of accounts in Ethereum state:
  - Externally Controlled Accounts
  - Contracts Accounts

Externally Owned Accounts (EOAs):
  - Can have an ether balance.
  - Can send transactions.
  - Are controlled by private keys.
  - Has no code.

Contract Accounts:
  - Can have an ether balance.
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
 - The amount of ether to transfer from the sender to the recipient
 - An optional data field.
 - A ``STARTGAS`` value, representing the maximum number of computational steps the transaction execution is allowed to take.
 - A ``GASPRICE`` value, representing the fee the sender pays per computational step.

What is a Message?
================================================================================
Contracts have the ability to send "messages" to other contracts. Messages are virtual objects that are never serialized and exist only in the Ethereum execution environment.

A message contains:
 - The sender of the message (implicit).
 - The recipient of the message.
 - The amount of ether to transfer alongside the message.
 - An optional data field.
 - A ``STARTGAS`` value.

Essentially, a message is like a transaction, except it is produced by a
contract and not an external actor. A message is produced when a
contract currently executing code executes the ``CALL`` opcode, which
produces and executes a message. Like a transaction, a message leads to
the recipient account running its code. Thus, contracts can have
relationships with other contracts in exactly the same way that external
actors can.

Note that the gas allowance assigned by a transaction or contract
applies to the total gas consumed by that transaction and all
sub-executions. For example, if an external actor A sends a transaction
to B with 1000 gas, and B consumes 600 gas before sending a message to
C, and the internal execution of C consumes 300 gas before returning,
then B can spend another 100 gas before running out of gas.


What is Gas?
================================================================================
[explain that it is the fuel for Ethereum transactions]

Estimating Gas
================================================================================

Transaction Pool
================================================================================

Lifecycle of a Transaction
================================================================================

Signing Transactions Offline
================================================================================
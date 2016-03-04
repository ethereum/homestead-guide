********************************************************************************
The Homestead Release
********************************************************************************

[MOST LIKELY INACCURATE - DO NOT QUOTE]

Milestones of the Ethereum development roadmap
-----------------------------------------------

* Prerelease Step 0: Olympic testnet - launched May 2015
* Release Step One: Frontier - launched 30 July 2015
* Release Step Two: Homestead - to launch Q1 2016
* Release Step Three: Metropolis -
* Release Step Four: Serenity

Homestead is introduced automatically at block number #?

While `the original plan laid out before Frontier <https://blog.ethereum.org/2015/03/03/ethereum-launch-process/>`_ is still valid, the substance behind that thinking changed somewhat.
As the Olympic testnet phase (before Frontier release) saw a lot of major improvements, Frontier was launched right after not including quite a few caveat features (lower mining reward). Naturally then Homestead was meant to be the real deal finally launching Ethereum network improving upon Frontier's wild west and bringing stability and reliability to the network. Our hope is that Homestead delivers on this promise no matter how high the bar is set already.


Homestead  hard fork changes
----------------------------------
Ethereum in the narrow formal sense is a suite of ptotocols.
Homestead comes with a few backward-incompatible protocol changes, and therefore will require a hard fork.

* `EIP 2: <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2.mediawiki>`_

  * cost for creating contracts via a transaction is increased from 21000 to 53000. Contract creation from a contract using the ``CREATE`` opcode is unaffected.
  * transaction signatures whose s-value is greater than ``secp256k1n/2`` are now considered invalid
  * If contract creation does not have enough gas to pay for the final gas fee for adding the contract code to the state, the contract creation fails (ie. goes out-of-gas) rather than leaving an empty contract.
  * Change the difficulty adjustment algorithm
* `EIP 7: DELEGATECALL <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7.md>`_: Add a new opcode, ``DELEGATECALL`` at ``0xf4``, which is similar in idea to ``CALLCODE``, except that it propagates the sender and value from the parent scope to the child scope, ie. the call created has the same sender and value as the original call. See `comments on EIP 7 <https://github.com/ethereum/EIPs/issues/23>`_
* `EIP 8: devp2p Forward Compatibility compliance with the Robustness Principle <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-8.md>`_ Changes to the RLPx Discovery Protocol and RLPx TCP transfer protocol to ensure that all client software in use on the Ethereum network can cope with future network protocol upgrades.

The changes have the following benefits:

* EIP-2/1 eliminates the excess incentive to create contracts via transactions, where the cost is 21000, rather than contracts, where the cost is 32000.
* EIP-2/1 also fixes the protocol "bug" that with the help of suicide refunds, it is currently possible to make a simple ether value transfer using only 11664 gas.
* EIP-2/2 fixes a transaction malleability concern (not a security flaw, but a UI incovenience).
* EIP-2/3 creates a more intuitive "success or fail" distinction in the result of a contract creation process, rather than the current "success, fail, or empty contract" trichotomy
* EIP-2/4 eliminates the excess incentive to set the timestamp difference to exactly 1 in order to create a block that has slightly higher difficulty and that will thus be guaranteed to beat out any possible forks. This guarantees to keep block time in the 10-20 range and according to simulations restores the target 15 second blocktime (instead of the current effective 17s).
* EIP-7 makes it much easier for a contract to store another address as a mutable source of code and ''pass through'' calls to it, as the child code would execute in essentially the same environment (except for reduced gas and increased callstack depth) as the parent.
* EIP-8 makes sure that all client software in use on the Ethereum network can cope with future network protocol upgrades.


* `Reddit discussion on Homestead  hard fork changes <https://www.reddit.com/r/ethereum/comments/3tbwbo/planned_homestead_hard_fork_changes/>`_
* `Homestead homepage preview <http://dipl.me:3000/>`_

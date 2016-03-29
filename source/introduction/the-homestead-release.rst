********************************************************************************
The Homestead Release
********************************************************************************

Homestead is the second major version of the Ethereum platform and is the first production release of Ethereum. It includes several protocol changes and a networking change that provides the ability to do further network upgrades. The first version of Ethereum, called the Frontier release, was essentially a beta release that allowed developers to learn, experiment, and begin building Ethereum decentralized apps and tools. 

Milestones of the Ethereum development roadmap
-----------------------------------------------

The `original development roadmap <https://blog.ethereum.org/2015/03/03/ethereum-launch-process/>`_ laid out before Ethereum went live specified the following milestones:

* Prerelease Step 0: Olympic testnet - launched May 2015
* Release Step One: Frontier - launched 30 July 2015
* Release Step Two: Homestead - launches 14 March 2016 (Pi Day)
* Release Step Three: Metropolis - TBA
* Release Step Four: Serenity - TBA


While still valid, the substance behind it has changed somewhat.
The `Olympic testnet <olympic-testnet>`_ phase (before the `Frontier release <history-of-ethereum.html#the-ethereum-frontier-launch>`_) saw a lot of major improvements, followed by Frontier which was launched immediately after. Homestead marks the exit from a beta product to a stable release.
Homestead is introduced automatically at block number 1,150,000 which should occur roughly around March 14th, 2016, Pi Day.

If you are running a node connected to the live network, it is important that you upgrade to a Homestead-compatible client. Such clients with their versions are listed under :ref:`Ethereum Clients`. Otherwise you will end up on the wrong fork and will no longer be in sync with the rest of the network.

Once the Ethereum blockchain reaches block 1,150,000, the Ethereum network will undergo a hardfork enabling a few major changes such as explained in the following section.

.. _homestead-hard-fork-changes:

Homestead hard fork changes
----------------------------------
Ethereum in the narrow formal sense is a suite of protocols.
Homestead comes with a few backward-incompatible protocol changes, and therefore will require a hard fork. These changes that made their way through the process for :ref:`Ethereum Improvement Proposals <Ethereum Improvement Proposals>` and included are:

* `EIP 2: <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2.mediawiki>`_

  * cost for creating contracts via a transaction is increased from 21000 to 53000. Contract creation from a contract using the ``CREATE`` opcode is unaffected.
  * transaction signatures whose s-value is greater than ``secp256k1n/2`` are now considered invalid
  * If contract creation does not have enough gas to pay for the final gas fee for adding the contract code to the state, the contract creation fails (ie. goes out-of-gas) rather than leaving an empty contract.
  * Change the difficulty adjustment algorithm
* `EIP 7: DELEGATECALL <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7.md>`_: Add a new opcode, ``DELEGATECALL`` at ``0xf4``, which is similar in idea to ``CALLCODE``, except that it propagates the sender and value from the parent scope to the child scope, ie. the call created has the same sender and value as the original call. This means contracts can store pass through information while following msg.sender and ``msg.value`` from its parent contract. Great for contracts which create contracts but don’t repeat additional information which saves gas. See `comments on EIP 7 <https://github.com/ethereum/EIPs/issues/23>`_
* `EIP 8: devp2p Forward Compatibility compliance with the Robustness Principle <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-8.md>`_ Changes to the RLPx Discovery Protocol and RLPx TCP transfer protocol to ensure that all client software in use on the Ethereum network can cope with future network protocol upgrades. For older versions of an Ethereum client, updates to the network protocol weren’t being accepted by older clients and would refuse communication if the hello packets didn’t meet expectations. This update means all future versions of the client will accept incoming network upgrades and handshakes.

The changes have the following benefits:

* EIP-2/1 eliminates the excess incentive to create contracts via transactions, where the cost is 21000, rather than contracts, where the cost is 32000.
* EIP-2/1 also fixes the protocol "bug" that with the help of suicide refunds, it is currently possible to make a simple ether value transfer using only 11664 gas.
* EIP-2/2 fixes a transaction malleability concern (not a security flaw, but a UI incovenience).
* EIP-2/3 creates a more intuitive "success or fail" distinction in the result of a contract creation process, rather than the current "success, fail, or empty contract" trichotomy
* EIP-2/4 eliminates the excess incentive to set the timestamp difference to exactly 1 in order to create a block that has slightly higher difficulty and that will thus be guaranteed to beat out any possible forks. This guarantees to keep block time in the 10-20 range and according to simulations restores the target 15 second blocktime (instead of the current effective 17s).
* EIP-7 makes it much easier for a contract to store another address as a mutable source of code and ''pass through'' calls to it, as the child code would execute in essentially the same environment (except for reduced gas and increased callstack depth) as the parent.
* EIP-8 makes sure that all client software in use on the Ethereum network can cope with future network protocol upgrades.


Additional resources:
- `Reddit discussion on Homestead Release <https://www.reddit.com/r/ethereum/comments/48arax/homestead_release_faq/>`_
- :ref:`Ethereum Improvement Proposals`

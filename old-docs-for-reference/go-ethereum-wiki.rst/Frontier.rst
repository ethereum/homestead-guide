**FRONTIER IS COMING**

-  `Frontier launch final
   steps <https://blog.ethereum.org/2015/07/27/final-steps/>`__
-  `Etherchain API <https://etherchain.org/frontier>`__ look out for
   block #1028201
-  `Olympic network stats <https://stats.ethdev.com/>`__

Ethereum Frontier Release
=========================

Introduction
------------

Frontier is the first in a series of releases that punctuate the roadmap
for the development of Ethereum. Frontier will be followed by
‘Homestead’, ‘Metropolis’ and ‘Serenity’ throughout the coming year,
each adding new features and improving the user friendliness and
security of the platform.

Ethereum is special and different from other software projects in that
its release also involves launching a live network. After a year and a
half of development the Proof of Concept series completed 9 cycles. The
10th iteration resulted in the Olympic testnet, which gradually led to
the Release Candidate client for Frontier.

The Ethereum network goes live when the clients consent on the **genesis
block** and start mining transactions on it. The genesis block will
reference an initial system state where all the accounts set up by the
presale exist with the correct amount of pre-issued ether allocated.
Initially, the network will be in a "thawing" state allowing only blocks
to be mined, but not transactions to be processed. This allows for users
to have a break-in period to connect to the network while also building
up its security.

In conjunction with the Frontier launch several exchanges will likely
start enabling trade of Ether, which will provide necessary liquidity to
the marketplace, allowing users and miners to transfer their holdings to
other users requiring more or less Ether. As opposed to an earlier
strategy, there is no plan to remove any contracts from the blockchain
or otherwise alter the network to carry balances over to Homestead. In
other words, the state in Homestead will be a direct and unmodified
continuation of the state in Frontier.

Mining reward is the full amount of 5 ether per block (as opposed to our
earlier proposal of a reduced amount). Mining rewards are discussed in
detail
`here <https://github.com/ethereum/go-ethereum/wiki/Mining#mining-rewards>`__

Safety warnings
---------------

-  **You are responsible for your own computer security.** If your
   machine is compromised you **will** lose your ether, access to any
   contracts and maybe more.
-  **You are responsible for your own actions.** If you mess something
   up or break any laws while using this software, it's your fault, and
   your fault only.
-  **You are responsible for your own karma.** Don't be a jerk and
   respect others.

**WARNING:** Before you interact with the Ethereum Frontier network,
make sure you read the documentation and understand the caveats and
risks. Please read the `legal
disclaimer <https://github.com/ethereum/go-ethereum/wiki/Disclaimer>`__

Components released
-------------------

The focus of Frontier is the Go implementation of an Ethereum full node,
with a command line interface codenamed "Geth".

By `installing and running
``geth`` <https://github.com/ethereum/go-ethereum/wiki/Geth>`__, you can
take part in the Ethereum live network, mine ether on the blockchain,
transfer funds between addresses, create contracts and send
transactions.

**WARNING**: before you use ``geth`` or interact with the Ethereum
Frontier live network, make sure you read the documentation and fully
understand the `caveats and
risks <https://github.com/ethereum/go-ethereum/wiki/Disclaimer>`__.

Apart from ``geth``, the Go CLI, the Frontier release contains the
following components:

-  ``web3.js`` library implementing the `JavaScript
   API <https://github.com/ethereum/wiki/wiki/JavaScript-API>`__ for
   dapps to conveniently interact with an Ethereum node
-  ``solc`` a standalone solidity compiler. You only need this if you
   want to use your dapp or `console to compile solidity
   code <https://github.com/ethereum/go-ethereum/wiki/Contracts-and-Transactions#compiling-a-contract>`__.
-  ``ethminer`` a standalone miner for openCL `GPU
   mining <https://github.com/ethereum/go-ethereum/wiki/Mining#gpu-mining>`__
-  ``netstat`` a `network monitoring
   GUI <https://github.com/ethereum/wiki/wiki/Network-Status>`__ allows
   you to add your node to the http://stats.ethdev.com page

The actual launch process
-------------------------

Ethereum is not something that’s centrally ‘launched’, but instead
emerges from consensus. Users will have to voluntarily download and run
a specific version of the software, then manually generate and load the
Genesis block to join the official project’s network.

Once Frontier has been installed on their machines, users will need to
generate the Genesis block themselves, then load it into their Frontier
clients. A script and instructions on how to do this will be provided as
part of the new Ethereum website, as well as our various wikis.

We’re often asked how existing users will switch from the test network
to the live network: it will be done through a switch at the Geth
console (--networkId). By default the new build will aim to connect to
the live network, to switch back to the test network you’ll simply
indicate a network id of ‘0’.

Bugs, Issues and Complications
------------------------------

The work on the Frontier software is far from over. Expect weekly
updates which will give you access to better, more stable clients. Many
of the planned Frontier gotchas (which included a chain reset at
Homestead, limiting mining rewards to 10%, and centralized
checkpointing) were deemed unnecessary. However, there are still big
differences between Frontier and Homestead. In Frontier, we’re going to
have issues, we’re going to have updates, and there will be bugs – users
are taking their chances when using the software. There will be big
(BIG) warning messages before developers are able to even install it. In
Frontier, documentation is limited, and the tools provided require
advanced technical skills.

The Canary Contracts
--------------------

The Canary contracts are simple switches holding a value equal to 0 or
1. Each contract is controlled by a different member of the Eth/Dev team
and will be updated to ‘1’ if the internal Frontier Disaster Recovery
Team flags up a consensus issue, such as a fork.

Within each Frontier client, a check is made after each block against 4
contracts. If two out of four of these contracts have a value switched
from 0 to 1, mining stops and a message urging the user to update their
client is displayed. This is to prevent “fire and forget” miners from
preventing a chain upgrade.

This process is centralized and will only run for the duration of
Frontier. It helps preventing the risk of a prolonged period (24h+) of
outage.

Stats, Status and Badblock websites
-----------------------------------

You probably are already familiar with our network stats monitor,
https://stats.ethdev.com/. It gives a quick overview of the health of
the network, block resolution time and Gas statistics. Remember that
participation in the stats page is voluntary, and nodes have to add
themselves before they appear on the panel. See details on `network
monitoring <https://github.com/ethereum/wiki/wiki/Network-Status>`__

In addition to the stats page, we will have a status page at
https://status.ethereum.org/ (no link as the site is not live yet) which
will gives a concise overview of any issue that might be affecting
Frontier. Use it as your first port of call if you think something might
not be right.

Finally, if any of the clients receive an invalid block, they will
refuse to process it send it to the bad block website (AKA ‘Sentinel’).
This could mean a bug, or something more serious, such as a fork. Either
way, this process will alert our developers to potential issues on the
network. The website itself is public and available at
https://badblocks.ethdev.com (currently operating on the testnet).

A Clean Testnet
---------------

During the last couple of months, the Ethereum test network was pushed
to its limits in order to test scalability and block propagation times.
As part of this test we encouraged users to spam the network with
transactions, contract creation code and call to contracts, at times
reaching over 25 transactions per second. This has led the test network
chain to grow to a rather unwieldy size, making it difficult for new
users to catch up. For this reason, and shortly after the Frontier
release, there will be a new test network following the same rules as
Frontier.

Olympic rewards distribution
----------------------------

During the Olympic phase there were a number of rewards for various
achievements including mining prowess. These rewards will not be part of
the Frontier Genesis block, but instead will be handed out by a
Foundation bot during the weeks following the release.

Resources: - `Frontier launch final
steps <https://blog.ethereum.org/2015/07/27/final-steps/>`__ - `Frontier
is
coming <https://blog.ethereum.org/2015/07/22/frontier-is-coming-what-to-expect-and-how-to-prepare/>`__
blogpost by Stephan Tual announcing the launch. - `The frontier
website <https://frontier.ethereum.org>`__ - `Original announcement of
the release
scheme <https://blog.ethereum.org/2015/03/03/ethereum-launch-process>`__
by Vinay Gupta - `Follow-up
blogpost <https://blog.ethereum.org/2015/03/12/getting-to-the-frontier/>`__
- `Least Authority audit
blogpost <https://blog.ethereum.org/2015/07/07/know-ethereum-secure/>`__
with links to the audit report, - `Deja Vu audit
blogpost <http://www.dejavusecurity.com/blog/2015/7/23/deja-vu-security-assists-in-ethereum-release>`__
- `Olympic. Frontier
prerelease <https://blog.ethereum.org/2015/05/09/olympic-frontier-pre-release/>`__,
Vitalik's blogpost detailing olympic rewards.

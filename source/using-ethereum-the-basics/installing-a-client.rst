********************************************************************************
Installing a Client
********************************************************************************

Why are there multiple clients?
================================================================================

A key design decision for Ethereum was to separate the definition of the
protocol (the "Yellow Paper") from the implementation(s) of that protocol
(geth, eth, etc).

From the earlier days of the project there have been multiple interoperable
client implementations across a range of different operating systems.

As we enter the Homestead phase, the Go client is very, very dominant, but
it hasn't always been that way, and won't necessarily be that way in the
future.

In the early days of the project the C++ client was more popular.
BlockApps were able to create the Haskell client in stealth mode and to
"uncloak" at DEVCON1 as part of the Azure partnership.  Ethcore have
brought a Rust client to life in the last few months.  Every client
has its own strengths.

That client diversity is a huge win for the eco-system as a whole.
It lets us verify that the protocol is unambiguous.  It keeps the door
open for new innovation.  It keeps us all honest.

However, it can be very confusing for end-users, because there is no
universal "Ethereum Installer" for them to use.


What clients are currently available, and which support Homestead?
================================================================================

There are a number of "official" clients whose development has been funded
by the Ethereum Foundation, and there are various other clients which have
been built by the community or by other commercial entities.

+------------------------+------------+------------------------+----------------------------------+
| Client                 | Language   | Developers             | Homestead Release                |
+========================+============+========================+==================================+
| `mist (dapp browser)`_ | Javascript | `Ethereum Foundation`_ | `mist-v0.5.1`_                   |
+------------------------+------------+------------------------+----------------------------------+
| `go-ethereum`_         | Go         | `Ethereum Foundation`_ | `geth-v1.3.5`_                   |
+------------------------+------------+------------------------+----------------------------------+
| `cpp-ethereum`_        | C++        | `Ethereum Foundation`_ | `eth-v1.2.1`_                    |
+------------------------+------------+------------------------+----------------------------------+
| `pyethapp`_            | Python     | `Ethereum Foundation`_ | `pyethapp-v1.1.0`_               |
+------------------------+------------+------------------------+----------------------------------+
| `ethereumjs-lib`_      | Javascript | `Ethereum Foundation`_ | `ethereumjs-lib-v3.0.0`_         |
+------------------------+------------+------------------------+----------------------------------+
| `Ethereum(J)`_         | Java       | `ConsenSys`_           | `ethereumJ-v1.2.0-homestead-RC`_ |
+------------------------+------------+------------------------+----------------------------------+
| `ethereumH`_           | Haskell    | `ConsenSys`_           |                                  |
+------------------------+------------+------------------------+----------------------------------+
| `ethereum-ruby`_       | Ruby       | `Digix`_               |                                  |
+------------------------+------------+------------------------+----------------------------------+
| `Parity`_              | Rust       | `Ethcore`_             |                                  |
+------------------------+------------+------------------------+----------------------------------+

.. _mist (dapp browser): http://github.com/ethereum/mist/
.. _go-ethereum: http://github.com/ethereum/go-ethereum/
.. _cpp-ethereum: https://github.com/ethereum/webthree-umbrella
.. _pyethapp: https://github.com/ethereum/pyethapp
.. _ethereumjs-lib: https://github.com/ethereumjs/ethereumjs-lib
.. _Ethereum(J): https://github.com/ethereum/ethereumj
.. _ethereumH: https://github.com/jamshidh/ethereum-client-haskell
.. _ethereum-ruby: https://github.com/DigixGlobal/ethereum-ruby
.. _Parity: https://github.com/ethcore/parity

.. _Ethereum Foundation: https://ethereum.org/foundation
.. _ConsenSys: https://consensys.net/
.. _Digix: https://dgx.io/
.. _Ethcore: https://ethcore.io/

.. _mist-v0.5.1: https://github.com/ethereum/mist/releases/tag/0.5.1
.. _geth-v1.3.5: https://github.com/ethereum/go-ethereum/releases/tag/v1.3.5
.. _eth-v1.2.1: https://github.com/ethereum/webthree-umbrella/releases/tag/v1.2.1
.. _pyethapp-v1.1.0: https://github.com/ethereum/pyethapp/releases/tag/v1.1.0
.. _ethereumjs-lib-v3.0.0: https://github.com/ethereumjs/ethereumjs-lib/tree/v3.0.0
.. _ethereumJ-v1.2.0-homestead-RC: https://github.com/ethereum/ethereumj/releases/tag/1.2.0-homestead-RC


What should I install on my desktop/laptop?
================================================================================

If you have a laptop or desktop machine, you should probably just install
the Ethereum Wallet and you are done.

That is a "single dapp" deployment of the Mist Browser which will be the
centerpiece of the Metropolis phase of development, which comes after
Homestead.   Mist comes with bundled geth and eth binaries and if you are
not running a command-line client then Mist will run one of the bundles
binaries for you.

If you want to interact with Ethereum on the command-line, and to take
advantage of the Javascript console then you will want to install one of
the client applications directly, as well as having the ability to connect
to the network using Mist.

geth and eth are the best place to start, because they have both been
under development since the start of the project, have passed security
audits, work for all platforms and have Ethereum Foundation resources
assigned to their ongoing maintenance and support.  Beyond that, of course,
it is all a matter of personal preference.  Try them all :-)

If you want to do mining then Mist will not be sufficient.  Check out
the Mining section.


What should I install on my mobile/tablet?
================================================================================

We are at the very beginning of our support for mobile devices.   The Go
team are publishing experimental iOS and Android libraries, which some
developers are using to start bootstrapping mobile applications, but there
are not yet any mobile Ethereum clients available.

The main hinderance to the use of Ethereum on mobile devices is that the
Light Client support is still incomplete.   The work which has been done is
off in a private branch, and is only available for the Go client.
doublethinkco will be starting development of Light Client for the C++ client
in the coming months, following grant funding.

Check out Syng.im, who were initially using EthereumJ-Android but have
recently flipped to Geth cross-builds with Light Client.


What should I install on my SBC?
================================================================================

Use EthEmbedded stuff.
And doublethinkco cross-builds.

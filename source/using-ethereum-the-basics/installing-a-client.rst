********************************************************************************
Installing a Client
********************************************************************************

There are a number of "official" clients whose development has been funded
from the resources administered by the Ethereum Foundation.  There are also
various other clients which have been built by the community or by other
commercial entities.

Read more about the specific clients in the
`Ethereum Clients <http://docs.ethereum.org/en/latest/ethereum-clients/index.html>`_ section.

Only a subset of the clients have released versions which are Homestead
compatible.  There are links to those releases in the right-hand column of
the table below.   The clients without links are all working on getting
Homestead-compatible versions released.   Keep checking back.   We will
add links to them here as they are released.

+------------------------+------------+------------------------+----------------------------------+
| Client                 | Language   | Developers             | Homestead Release                |
+========================+============+========================+==================================+
| `mist (dapp browser)`_ | Javascript | `Ethereum Foundation`_ | `mist-v0.5.2`_                   |
+------------------------+------------+------------------------+----------------------------------+
| `go-ethereum`_         | Go         | `Ethereum Foundation`_ | `geth-v1.3.5`_                   |
+------------------------+------------+------------------------+----------------------------------+
| `cpp-ethereum`_        | C++        | `Ethereum Foundation`_ | `eth-v1.2.2`_                    |
+------------------------+------------+------------------------+----------------------------------+
| `pyethapp`_            | Python     | `Ethereum Foundation`_ |                                  |
+------------------------+------------+------------------------+----------------------------------+
| `ethereumjs-lib`_      | Javascript | `Ethereum Foundation`_ | `ethereumjs-lib-v3.0.0`_         |
+------------------------+------------+------------------------+----------------------------------+
| `Ethereum(J)`_         | Java       | `ConsenSys`_           | `ethereumJ-v1.2.0-homestead-RC`_ |
+------------------------+------------+------------------------+----------------------------------+
| `ethereumH`_           | Haskell    | `ConsenSys`_           |                                  |
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
.. _Parity: https://github.com/ethcore/parity

.. _Ethereum Foundation: https://ethereum.org/foundation
.. _ConsenSys: https://consensys.net/
.. _Digix: https://dgx.io/
.. _Ethcore: https://ethcore.io/

.. _mist-v0.5.2: https://github.com/ethereum/mist/releases/tag/0.5.2
.. _geth-v1.3.5: https://github.com/ethereum/go-ethereum/releases/tag/v1.3.5
.. _eth-v1.2.2: https://github.com/ethereum/webthree-umbrella/releases/tag/v1.2.2
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

You have some choice here depending on your skill level, and what you are looking to do.

* Download a fully prepared image(link to page with detailed download & install instructions)

  * If you are new to Ethereum AND SBC boards such as the Raspberry Pi then this is for you! Simply download the image specific to the dev board you are working with, burn it to an SD card, boot your device, and run Ethereum!
  
* Download a pre-compiled application(link to page with detailed download & install instructions)

  * If you already have an SBC running and have a specific, preferred OS or setup that you want to keep, then this is your best option! Depending on the platform, you can simply download the apropriate executable, and with minimal linking of libraries and setting of PATH you can have Ethereum running in your existing environment!
  
* Build from source using customizable scripts(link to page with more detail and individual SBC links to https://github.com/ethembedded)

  * Looking to perform a custom install?  We have scripts available to compile from source "on device". Our scripts contain auto-install of dependencies as well as the client itself. This will allow you to install a specific version of the Ethereum client(i.e.-"develop", "master", etc.), compile your own forked version of a client, and generally play around with the intracacies of the build process.

.. _sec:clients:

*****************************************************
Choosing a client
*****************************************************

Why are there multiple Ethereum clients?
=====================================================================

From the earliest days of the project there have been multiple
client implementations across a range of different operating systems.  That
client diversity is a huge win for the ecosystem as a whole.
It lets us verify that the protocol (specified in the `Yellow Paper <https://github.com/ethereum/yellowpaper>`_)
is unambiguous.  It keeps the door open for new innovation.  It keeps us
all honest.  However, it can be very confusing for end-users, because there
is no universal "Ethereum Installer" for them to use.

As of September 2016, the leading implementations are :ref:`go-ethereum` and :ref:`Parity`.

+------------------------+------------+------------------------+-------------------------------------+
| Client                 | Language   | Developers             | Latest release                      |
+========================+============+========================+=====================================+
| :ref:`go-ethereum`     | Go         | `Ethereum Foundation`_ | `go-ethereum-v1.4.18`_              |
+------------------------+------------+------------------------+-------------------------------------+
| :ref:`Parity`          | Rust       | `Ethcore`_             | `Parity-v1.4.0`_                    |
+------------------------+------------+------------------------+-------------------------------------+
| :ref:`cpp-ethereum`    | C++        | `Ethereum Foundation`_ | `cpp-ethereum-v1.3.0`_              |
+------------------------+------------+------------------------+-------------------------------------+
| :ref:`pyethapp`        | Python     | `Ethereum Foundation`_ | `pyethapp-v1.5.0`_                  |
+------------------------+------------+------------------------+-------------------------------------+
| :ref:`ethereumjs-lib`  | Javascript | `Ethereum Foundation`_ | `ethereumjs-lib-v3.0.0`_            |
+------------------------+------------+------------------------+-------------------------------------+
| :ref:`Ethereum\(J\)`   | Java       | `\<ether.camp\>`_      | `ethereumJ-v1.3.1`_                 |
+------------------------+------------+------------------------+-------------------------------------+
| :ref:`ruby-ethereum`   | Ruby       | `Jan Xie`_             | `ruby-ethereum-v0.9.6`_             |
+------------------------+------------+------------------------+-------------------------------------+
| :ref:`ethereumH`       | Haskell    | `BlockApps`_           | no Homestead release yet            |
+------------------------+------------+------------------------+-------------------------------------+

.. _Ethereum Foundation: https://ethereum.org/foundation
.. _\<ether.camp\>: http://www.ether.camp
.. _BlockApps: http://www.blockapps.net/
.. _Ethcore: https://ethcore.io/
.. _Jan Xie: https://github.com/janx/

.. _go-ethereum-v1.4.18: https://github.com/ethereum/go-ethereum/releases/tag/v1.4.18
.. _cpp-ethereum-v1.3.0: https://github.com/bobsummerwill/cpp-ethereum/releases/tag/v1.3.0
.. _ethereumjs-lib-v3.0.0: https://github.com/ethereumjs/ethereumjs-lib/releases/tag/v3.0.0
.. _ethereumJ-v1.3.1: https://github.com/ethereum/ethereumj/releases/tag/1.3.1
.. _Parity-v1.4.0: https://github.com/ethcore/parity/releases/tag/v1.4.0
.. _pyethapp-v1.5.0: https://github.com/ethereum/pyethapp/releases/tag/v1.5.0
.. _ruby-ethereum-v0.9.6: https://rubygems.org/gems/ruby-ethereum/versions/0.9.6


What should I install on my desktop/laptop?
================================================================================

Most users will likely just install `Mist / Ethereum Wallet <https://github.com/ethereum/mist>`_
and that will be enough for their needs.

The Ethereum Wallet is a "single dapp" deployment of the **Mist Browser**
which will be the centerpiece of the Metropolis phase of development, which
comes after Homestead.

Mist comes with bundled :ref:`go-ethereum` and :ref:`cpp-ethereum` binaries
and if you are not running a command-line Ethereum client when Mist starts
then it will start syncing the blockchain using one of the bundled clients
(defaulting to **geth**).  If you want to use Parity with Mist, or to run Mist against
a private network, just start your node before Mist, and Mist
will connect to your node rather than starting one itself.

**Work is underway to add Parity and other clients as "first-class entities"
to Mist too.**

If you want to interact with Ethereum on the command-line, and to take
advantage of the Javascript console then you will want to install one of
the client applications directly, as well as Mist.  Follow the links in
the table above for further instructions.

If you want to do mining then Mist will not be sufficient.  Check out
the :ref:`mining` section.


What should I install on my mobile/tablet?
================================================================================

We are at the very beginning of our support for mobile devices.   The Go
team are publishing experimental iOS and Android libraries, which some
developers are using to start bootstrapping mobile applications, but there
are not yet any mobile Ethereum clients available.

The main hindrance to the use of Ethereum on mobile devices is that the
Light Client support is still incomplete.   The work which has been done is
off in a private branch, and is only available for the Go client.
doublethinkco will start development of Light Client for the C++ client
in the coming months, following grant funding.

Check out `Status.im <http://status.im>`_, who were initially using
`ethereumj-personal <https://github.com/status-im/ethereumj-personal>`_ based
on :ref:`Ethereum(J)`, but have recently flipped to Geth cross-builds with
Light Client.


What should I install on my SBC?
================================================================================

You have some choice here depending on your skill level, and what you are looking to do.

* Download a fully prepared image(link to page with detailed download & install instructions)

  * If you are new to Ethereum AND SBC boards such as the Raspberry Pi then this is for you! Simply download the image specific to the dev board you are working with, burn it to an SD card, boot your device, and run Ethereum!

* Download a pre-compiled application(link to page with detailed download & install instructions)

  * If you already have an SBC running and have a specific, preferred OS or setup that you want to keep, then this is your best option! Depending on the platform, you can simply download the apropriate executable, and with minimal linking of libraries and setting of PATH you can have Ethereum running in your existing environment!

* Build from source using customizable scripts(link to page with more detail and individual SBC links to https://github.com/ethembedded)

  * Looking to perform a custom install?  We have scripts available to compile from source "on device". Our scripts contain auto-install of dependencies as well as the client itself. This will allow you to install a specific version of the Ethereum client(i.e.-"develop", "master", etc.), compile your own forked version of a client, and generally play around with the intricacies of the build process.


********************************************************************************
Interacting with Clients
********************************************************************************

In order to interact with Ethereum clients programmatically, please refer to the :ref:`Connecting to Clients` section.

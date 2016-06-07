.. _sec:clients:

*****************************************************
Choosing a client
*****************************************************

Why are there multiple Ethereum clients?
=====================================================================


The Ethereum clients are very analogous to a Java VM or .NET runtime.

They enable you to execute "Ethereum programs" on your computer.  They are
implemented to a written specification (the
`Yellow Paper <https://github.com/ethereum/yellowpaper>`_) and by design
are interoperable and somewhat "commodity".

From the earlier days of the project there have been multiple interoperable
client implementations across a range of different operating systems.  That
client diversity is a huge win for the ecosystem as a whole.
It lets us verify that the protocol is unambiguous.  It keeps the door
open for new innovation.  It keeps us all honest.  However, it can be
very confusing for end-users, because there is no universal
"Ethereum Installer" for them to use.

As we enter the Homestead phase, the Go client is very, very dominant, but
it hasn't always been that way, and won't necessarily be that way in the
future.

Only a subset of the clients have released versions which are Homestead
compatible.  There are links to those releases in the right-hand column of
the table below.   The clients without links are all working on getting
Homestead-compatible versions released.   Keep checking back.   We will
add links to them here as they are released.

+------------------------+------------+------------------------+----------------------------------+
| Client                 | Language   | Developers             | Homestead Release                |
+========================+============+========================+==================================+
| :ref:`go-ethereum`     | Go         | `Ethereum Foundation`_ | `geth-v1.4.6`_                   |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`cpp-ethereum`    | C++        | `Ethereum Foundation`_ | `eth-v1.2.7`_                    |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`pyethapp`        | Python     | `Ethereum Foundation`_ | `pyethapp-v1.2.2`_               |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`ethereumjs-lib`  | Javascript | `Ethereum Foundation`_ | `ethereumjs-lib-v3.0.0`_         |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`Ethereum\(J\)`   | Java       | `\<ether.camp\>`_      | `ethereumJ-v1.2.0`_              |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`ethereumH`       | Haskell    | `BlockApps`_           | not available yet                |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`Parity`          | Rust       | `Ethcore`_             | `Parity-v1.1.0`_                 |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`ruby-ethereum`   | Ruby       | `Jan Xie`_             | `ruby-ethereum-v0.9.1`_          |
+------------------------+------------+------------------------+----------------------------------+

.. _Ethereum Foundation: https://ethereum.org/foundation
.. _\<ether.camp\>: http://www.ether.camp
.. _BlockApps: http://www.blockapps.net/
.. _Ethcore: https://ethcore.io/
.. _Jan Xie: https://github.com/janx/

.. _geth-v1.4.6: https://github.com/ethereum/go-ethereum/releases/tag/v1.4.6
.. _eth-v1.2.7: https://github.com/ethereum/webthree-umbrella/releases/tag/v1.2.7
.. _ethereumjs-lib-v3.0.0: https://github.com/ethereumjs/ethereumjs-lib/releases/tag/v3.0.0
.. _ethereumJ-v1.2.0: https://github.com/ethereum/ethereumj/releases/tag/1.2.0
.. _Parity-v1.1.0: https://github.com/ethcore/parity/releases/tag/v1.1.0
.. _pyethapp-v1.2.2: https://github.com/ethereum/pyethapp/releases/tag/v1.2.2
.. _ruby-ethereum-v0.9.1: https://rubygems.org/gems/ruby-ethereum/versions/0.9.1

********************************************************************************
Installing a Client
********************************************************************************

There are a number of "official" clients whose development has been funded
from the resources administered by the Ethereum Foundation.  There are also
various other clients which have been built by the community or by other
commercial entities.

Read more about the specific clients in the specific client sections in this chapter.

What should I install on my desktop/laptop?
================================================================================

If you have a laptop or desktop machine, you should probably just install
the `Ethereum Wallet <https://github.com/ethereum/mist>`_ and you are done.

- Download the latest `Ethereum Wallet ZIP <https://github.com/ethereum/mist/releases/latest>`_ from Github.
- Unzip wherever you like
- Click on the executable (**Ethereum-Wallet, Ethereum-Wallet** or **Ethereum-Wallet.app**)
- The block-chain will be downloaded

The Ethereum Wallet is a "single dapp" deployment of the **Mist Browser**
which will be the centerpiece of the Metropolis phase of development, which
comes after Homestead.

Mist comes with bundled :ref:`go-ethereum` and :ref:`cpp-ethereum` binaries
and if you are not running a command-line Ethereum client when Mist starts
then it will start running one of the bundles clients for you.

If you want to interact with Ethereum on the command-line, and to take
advantage of the Javascript console then you will want to install one of
the client applications directly, as well as Mist.

:ref:`go-ethereum` and :ref:`cpp-ethereum` are the best place to start,
because they have both been under development since the start of the project,
have passed security audits, work for all platforms and have
:ref:`foundation` resources assigned to their ongoing maintenance and
support.

- Follow the :ref:`Installing binaries` instructions for **cpp-ethereum**
- For **go-ethereum**, just unzip the `released binaries <https://github.com/ethereum/go-ethereum/releases>`_

Beyond that, of course, it is all a matter of personal preference.  Try them all :-)

If you want to do mining then Mist will not be sufficient.  Check out
the :ref:`mining` section.


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

Check out `Syng.im <http://syng.io>`_, who were initially using
`ethereumj-personal <https://github.com/syng-im/ethereumj-personal>`_ based
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

  * Looking to perform a custom install?  We have scripts available to compile from source "on device". Our scripts contain auto-install of dependencies as well as the client itself. This will allow you to install a specific version of the Ethereum client(i.e.-"develop", "master", etc.), compile your own forked version of a client, and generally play around with the intracacies of the build process.

.. _Building Linux from source:

##################
Building for Linux
##################


Clone the repository
====================

To clone the source code, execute the following commands:

.. code:: bash

    git clone --recursive https://github.com/ethereum/cpp-ethereum.git
    cd cpp-ethereum
    git submodule update --init


Installing dependencies
=======================

Linux has a horror-show of fragmentation when it comes to packaging systems.

We support a `"one-button" bash script <https://github.com/ethereum/cpp-ethereum/blob/develop/scripts/install_deps.sh>`_
which attempts to make this minefield more navigable for users of common
distros.  It identifies your distro and installs the external packages which
you will need, using whatever combination of package servers and
build-from-source is required for your specific distro version.  This is a
non-trivial task, but by that token is also something which we don't want
anybody to have to replicate themselves.

.. code:: bash

    ./scripts/install_deps.sh

We use the same script within our Appveyor and TravisCI automated builds
and automated runs, so it is continuously tested, which is especially
important on macOS, where Homebrew is a constantly moving target.

The script is known to support the following distros and versions:

* Mac (OS X Mavericks, OS X Yosemite, OS X El Capitan, macOS Sierra)
* Arch Linux
* Alpine Linux (partial)
* Debian (Jesse and Stretch)
* Fedora (partial)
* Mint Linux (Qiana, Rebecca, Rafaela, Rosa, Sarah)
* Ubuntu (Trusty, Vivid, Utopic, Xenial, work-in-progress on Yakkety)

If you try it, and it doesn't work for you, please
`report the problem <https://github.com/ethereum/cpp-ethereum/issues/new>`_
with details of your distro, your version number and any other important
details and we can work together to get it working for your use-case.

We have manual instructions for Fedora, openSUSE and Arch Linux (see below).
If you using some other distro then please contact us and we'll see if we
can get you going.

.. toctree::
   linux-fedora.rst
   linux-opensuse.rst
   linux-arch.rst


Build on the command-line
================================================================================

When you have installed your dependencies you can build.

.. code:: bash

    mkdir build                                              Make a directory for the build output
    cd build                                                 Switch into that directory

    cmake ..                                                 To generate a makefile.
    make                                                     To build that makefile on the command-line
    make -j<number>                                          (or) Execute makefile with multiple cores in parallel


32-bit Linux builds
===================

We have cpp-ethereum building and running successfully on many 32-bit Linux
distros, with the main constraint being the availability of external
dependencies in 32-bit variants.  Probably the most active demand here is
for single-board computers like the Raspberry Pi family.

You will need to disable the JIT and the heavy-weight LLVM dependency which
comes with that.  EVMJIT only supports x86_64.  Other than that, cpp-ethereum
should "just work" on 32-bit platforms.  To disable JIT, you will need to
use the following command for the Makefile generation phase:

.. code:: bash

    cmake .. -DEVMJIT=Off

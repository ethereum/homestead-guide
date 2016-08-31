.. _Building Linux from source:

################################################################################
Building for Linux
################################################################################

NOTE - It may be possible to get the client working for Linux 32-bit, by
disabling EVMJIT and maybe other features too.  We might accept
pull-requests to add such support, but we will not put any of our
own development time into supporting Linux 32-bit builds.

Linux has a horror-show of distro-specific packaging system steps which are
the first thing which we need to do before we can start on
:ref:`Building from source`.   The sections below attempt to capture those
steps.   If you are using as different distro and hit issues, please
`let us know <https://gitter.im/ethereum/cpp-ethereum>`_.


Clone the repository
================================================================================

To clone the source code, execute the following command: ::

    git clone --recursive https://github.com/ethereum/cpp-ethereum.git
    cd cpp-ethereum

Installing dependencies (the easy way)
================================================================================

For the "Homecoming" release (v1.3.0) in July 2016 we added a new "one-button"
script for installing external dependencies, which identifies your distro and
installs the packages which you need.   This script is new and incomplete, but
is a way easier experience than the manual steps described in the next section
of this document.   Give it a go!

**It works for Debian, Ubuntu and macOS and a few other distros already**

If you try it, and it doesn't work for you, please let us know and we will
prioritize fixing your distro!::

    ./scripts/install_deps.sh


Installing dependencies manually (distro-specific)
================================================================================

.. toctree::
   linux-fedora.rst
   linux-opensuse.rst
   linux-arch.rst

Build on the command-line
================================================================================

When you have installed your dependencies you can build. ::

    mkdir build                                              Make a directory for the build output
    cd build                                                 Switch into that directory

    cmake ..                                                 To generate a makefile.
    make                                                     To build that makefile on the command-line
    make -j<number>                                          (or) Execute makefile with multiple cores in parallel

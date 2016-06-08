
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

    git clone --recursive https://github.com/ethereum/webthree-umbrella.git


Installing dependencies (distro-specific)
================================================================================

.. toctree::
   linux-ubuntu.rst
   linux-fedora.rst
   linux-opensuse.rst
   linux-arch.rst

Build on the command-line
================================================================================

**ONLY** after you have installed your dependencies (the rest of this doc!): ::

    mkdir build                                              Make a directory for the build output
    cd build                                                 Switch into that directory

    cmake ..                                                 To generate a makefile.
    make                                                     To build that makefile on the command-line
    make -j <number>                                         (or) Execute makefile with multiple cores in parallel

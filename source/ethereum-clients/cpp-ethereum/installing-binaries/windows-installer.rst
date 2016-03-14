
Windows installer
--------------------------------------------------------------------------------

We generate Windows installers
`for each release <https://github.com/ethereum/webthree-umbrella/releases>`_.

These should work on Windows 7, Windows 8/8.1 and Windows 10, though our
`automated builds <http://ethbuilds.com>`_ are all Windows 8.1 based.

**We only support 64-bit builds.**

It may be possible to get the client working for Windows 32-bit, by building
from source and disabling EVMJIT and maybe other features too.  We might accept
pull-requests to add such support, but we will not put any of our development
time into supporting Windows 32-bit builds.

The vast majority of individuals using Windows have 64-bit hardware now.

Here is the
`cpp-ethereum v1.2.2 Windows installer
<https://build.ethdev.com/cpp-binaries-data/release-1.2.2/Ethereum.exe>`_ for Homestead.

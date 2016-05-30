
Windows installer
--------------------------------------------------------------------------------

We generate Windows installers
`for each release <https://github.com/ethereum/webthree-umbrella/releases>`_.

These should work on Windows 7, Windows 8/8.1, Windows 10 and Windows Server
2012 R2, though our `automated builds <http://ethbuilds.com>`_ are all built
on a Windows 8.1 host machine.

If you hit runtime errors complaining about missing **msvcr120.dll** or
**msvcp120.dll** files then please install the
`Visual C++ Redistributable Packages for Visual Studio 2013 <https://www.microsoft.com/en-ca/download/details.aspx?id=40784>`_
from Microsoft.

**We only support 64-bit builds.**

It may be possible to get the client working for Windows 32-bit, by building
from source and disabling EVMJIT and maybe other features too.  We might accept
pull-requests to add such support, but we will not put any of our development
time into supporting Windows 32-bit builds.

The vast majority of individuals using Windows have 64-bit hardware now.

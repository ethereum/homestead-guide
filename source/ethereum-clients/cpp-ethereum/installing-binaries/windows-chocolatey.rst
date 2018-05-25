
Windows Chocolatey NuGet packages
--------------------------------------------------------------------------------

We aren't generating `Chocolatey <https://chocolatey.org/>`_ packages at
the time of writing, though we have done so in the past.

For anybody who isn't already familiar with the technology, this is essentially
`apt-get for Windows` - a global silent installer for tools.

We would like to
`support Chocolatey <https://github.com/ethereum/webthree-umbrella/issues/345>`_
again in the near future for all the same reasons we support Homebrew on OS X
and have PPAs for Ubuntu.  For technically competent users, doing
command-line operations like so would be very convenient: ::

    choco install cpp-ethereum
    choco update cpp-ethereum

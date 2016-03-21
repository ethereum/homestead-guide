Binaries
========

Download stable binaries
------------------------

All versions of Geth are built and available for download at
https://build.ethereum.org/builds/Windows%20Go%20master%20branch/. The
latest version is always available as
`Geth-Win64-latest.zip <https://build.ethereum.org/builds/Windows%20Go%20master%20branch/Geth-Win64-latest.zip>`__

1. Download zip file
2. Extract geth.exe from zip
3. Open a command terminal
4. chdir
5. open geth.exe

[STRIKEOUT:Installing from Chocolatey]
--------------------------------------

***Note: Chocolatey is stuck at 1.2.2 and deprecated. Consider using
another method***

For master branch:

::

    choco install geth-stable

*For more information see https://chocolatey.org/packages/geth-stable*

For develop branch:

::

    choco install geth-latest

*For more information see https://chocolatey.org/packages/geth-latest*

Source
======

Powershell script for building with Cygwin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

geth < 1.4.0 (MSYS2/GMP dependency):
https://gist.github.com/tgerring/b93057e06960d906574c

geth >= 1.4.0 (Cygwin/MingW):
https://gist.github.com/tgerring/79f018954aadfb3f406e

Building from source with winbuilds
-----------------------------------

1.  Install Git from http://git-scm.com/downloads
2.  Install Golang from
    https://storage.googleapis.com/golang/go1.4.2.windows-amd64.msi
3.  Install winbuilds from
    http://win-builds.org/1.5.0/win-builds-1.5.0.exe to ``c:\winbuilds``
4.  Run win builds here. It's safe to remove big dependencies like QT
    and GTK which aren't needed. *An exact list of dependencies should
    be determined*
5.  Setup environment paths
6.  Add ``GOROOT`` pointed to ``c:\go`` and ``GOPATH`` to ``c:\godev``
    (you are free to pick these paths).
7.  Set ``PATH`` to
    ``%PATH%;%GOROOT%\bin;%GOPATH%\bin;c:\winbuilds\bin``
8.  Open a terminal and install godep first:
    ``go get -u github.com/tools/godep``
9.  Open a terminal and download go-ethereum
    ``go get -d -u github.com/ethereum/go-ethereum``
10. Try building ethereum with go dep, navigate to
    ``c:\godev\src\github.com\ethereum\go-ethereum\cmd\geth`` and run
    ``git checkout develop && godep go install``

If you want to build from an other branch bypass ``godep go install``
for ``go install`` and checkout the dependencies manually.

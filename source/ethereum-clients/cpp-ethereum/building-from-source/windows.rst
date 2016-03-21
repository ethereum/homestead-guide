
Building for Windows
================================================================================

(Start at :ref:`Building from source`. These are the Windows specific steps.
That is the starting point)

We support **only 64-bit** builds and only for the following versions of Windows:

- `Windows 7 <https://en.wikipedia.org/wiki/Windows_7>`_
- `Windows 8/8.1 <https://en.wikipedia.org/wiki/Windows_8>`_
- `Windows 10 <https://en.wikipedia.org/wiki/Windows_10>`_

It may be possible to get the client working for Windows 32-bit, by
disabling EVMJIT and maybe other features too.  We might accept
pull-requests to add such support, but we will not put any of our
own development time into supporting Windows 32-bit builds.


Pre-requisites
--------------------------------------------------------------------------------

You will need to install the following dependencies

+------------------------------+-------------------------------------------------------+
| Software                     | Notes                                                 |
+==============================+=======================================================+
| `7-Zip 14.15`_               | Ensure that 7z.exe has been added to the PATH.        |
+------------------------------+-------------------------------------------------------+
| `Git for Windows 2.7.2`_     | This for retrieving source from Github.               |
+------------------------------+-------------------------------------------------------+
| `CMake-3.4.3`_               | Cross-platform build file generator. Don't use 3.5.0. |
+------------------------------+-------------------------------------------------------+
| either `Windows 7 SDK`_      | For files like winsock2.h and gdi32.lib               |
+------------------------------+-------------------------------------------------------+
| or `Windows 8 SDK`_          | This version if you have Windows 8 installed          |
+------------------------------+-------------------------------------------------------+
| or `Windows 10 SDK`_         | This version if you have Windows 10 installed         |
+------------------------------+-------------------------------------------------------+
| `MS VC++ 2010 SP1 Win64`_    | Runtime files for apps built with VC++ 2010           |
+------------------------------+-------------------------------------------------------+
| `VS Community 2013 Desktop`_ | C++ compiler and dev environment. **No VS2015 yet**   |
+------------------------------+-------------------------------------------------------+

.. _7-Zip 14.15: http://www.7-zip.org/a/7z1514-x64.exe
.. _Git for Windows 2.7.2: https://github.com/git-for-windows/git/releases/download/v2.7.2.windows.1/Git-2.7.2-64-bit.exe
.. _CMake-3.4.3: https://cmake.org/files/v3.4/cmake-3.4.3-win32-x86.exe
.. _Windows 7 SDK: https://www.microsoft.com/en-us/download/details.aspx?id=8279
.. _Windows 8 SDK: https://dev.windows.com/en-us/downloads/windows-8-1-sdk
.. _Windows 10 SDK: https://dev.windows.com/en-us/downloads/windows-10-sdk
.. _MS VC++ 2010 SP1 Win64: https://www.microsoft.com/en-us/download/details.aspx?id=26999
.. _VS Community 2013 Desktop: http://go.microsoft.com/fwlink/?LinkId=517284


Open a command-shell in the root directory which you cloned the source code to, and
then type the following, which does a crude approximation of a package server,
pulling pre-built binaries from our own server for the various external libraries
which we depend on: ::

    cd webthree-helpers\extdep
    getstuff.bat
    cd ..\..


Build from within Visual Studio
--------------------------------------------------------------------------------

Then execute the following commands, which will generate a Visual Studio
solution file using CMake: ::

    mkdir build
    cd build
    cmake -G "Visual Studio 12 2013 Win64" ..

Which should result in the creation of **cpp-ethereum.sln** in that build directory.

Double-clicking on that file should result in Visual Studio firing up.  Please use
the **Release** configuration or **RelWithDebugInfo**.   The **Debug** configuration
is broken at the time of writing, though we are
`working on resolving that issue <https://github.com/ethereum/webthree-umbrella/issues/123>`_.


Build on the command-line
--------------------------------------------------------------------------------

Alternatively, you can build the project on the command-line, like so: ::

    msbuild cpp-ethereum.sln /p:Configuration=Release


Incremental builds
--------------------------------------------------------------------------------

After your first successful build, it should generally be possible to do an
incremental build like so, from the root of the project: ::

    git pull
    del build\CMakeCache.txt
    cd build
    cmake -G "Visual Studio 12 2013 Win64" ..

And then build on command-line or in Visual Studio as before.

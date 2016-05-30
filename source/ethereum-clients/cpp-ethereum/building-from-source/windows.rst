
Building for Windows
================================================================================

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
| `Git for Windows`_           | This for retrieving source from Github.               |
+------------------------------+-------------------------------------------------------+
| `CMake`_                     | Cross-platform build file generator. Don't use 3.5.0. |
+------------------------------+-------------------------------------------------------+
| `Visual Studio 2015`_        | C++ compiler and dev environment.                     |
+------------------------------+-------------------------------------------------------+

.. _Git for Windows: https://git-scm.com/download/win
.. _CMake: https://cmake.org/download/
.. _Visual Studio 2015: https://www.visualstudio.com/products/vs-2015-product-editions


Open a command-shell in the root directory which you cloned the source code to, and
then type the following, which does a crude approximation of a package server,
pulling pre-built binaries from our own server for the various external libraries
which we depend on: ::

    cmake -P webthree-helpers/deps/install_deps.cmake


Clone the repository
--------------------------------------------------------------------------------

To clone the source code, execute the following command: ::

    git clone --recursive https://github.com/ethereum/webthree-umbrella.git


Build from within Visual Studio
--------------------------------------------------------------------------------

Then execute the following commands, which will generate a Visual Studio
solution file using CMake: ::

    mkdir build
    cd build
    cmake -G "Visual Studio 12 2013 Win64" ..

Which should result in the creation of **cpp-ethereum.sln** in that build directory.

Double-clicking on that file should result in Visual Studio firing up. We suggest
building **RelWithDebugInfo** configuration, but all others work.


Build on the command-line
--------------------------------------------------------------------------------

Alternatively, you can build the project on the command-line, like so: ::

    cmake --build . --config RelWithDebInfo


Incremental builds
--------------------------------------------------------------------------------

After your first successful build, it should generally be possible to do an
incremental build like so, from the root of the project: ::

    git pull
    del build\CMakeCache.txt
    cd build
    cmake -G "Visual Studio 12 2013 Win64" ..

And then build on command-line or in Visual Studio as before.

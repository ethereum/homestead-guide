
Building for Windows
================================================================================

We support **only 64-bit** builds and only for the following versions of Windows:

- `Windows 7 <https://en.wikipedia.org/wiki/Windows_7>`_
- `Windows 8/8.1 <https://en.wikipedia.org/wiki/Windows_8>`_
- `Windows 10 <https://en.wikipedia.org/wiki/Windows_10>`_
- `Windows Server 2012 R2 <https://en.wikipedia.org/wiki/Windows_Server_2012_R2>`_

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
| `Git for Windows`_           | Command-line tool for retrieving source from Github.  |
+------------------------------+-------------------------------------------------------+
| `CMake`_                     | Cross-platform build file generator.                  |
+------------------------------+-------------------------------------------------------+
| `Visual Studio 2015`_        | C++ compiler and dev environment.                     |
+------------------------------+-------------------------------------------------------+

.. _Git for Windows: https://git-scm.com/download/win
.. _CMake: https://cmake.org/download/
.. _Visual Studio 2015: https://www.visualstudio.com/products/vs-2015-product-editions


Get the source
--------------------------------------------------------------------------------

Clone the git repository containing all the source code by executing the following command: ::

    git clone --recursive https://github.com/ethereum/cpp-ethereum.git
    cd cpp-ethereum
    

Get the external dependencies
--------------------------------------------------------------------------------

Execute the CMake script that downloads and unpacks pre-built external libraries
needed to build the project: ::

    scripts\install_deps.bat


Generate Visual Studio project files
--------------------------------------------------------------------------------
Then execute the following commands, which will generate a Visual Studio
solution file using CMake: ::

    mkdir build
    cd build
    cmake -G "Visual Studio 14 2015 Win64" ..

Which should result in the creation of **cpp-ethereum.sln** in that build directory.

**NOTE**: We only support Visual Studio 2015 as of cpp-ethereum-v.1.3.0. If you don't
have it already, install the `Visual C++ 2015 Build Tools <http://landinghub.visualstudio.com/visual-cpp-build-tools>`_ **

Double-clicking on that file should result in Visual Studio firing up. We suggest
building **RelWithDebugInfo** configuration, but all others work.


Build on the command-line
--------------------------------------------------------------------------------

Alternatively, you can build the project on the command-line, like so: ::

    cmake --build . --config RelWithDebInfo

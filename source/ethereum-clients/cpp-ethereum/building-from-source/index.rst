.. _Building from source:
 
Building from source
================================================================================

The **cpp-ethereum** codebase is spread over several Git repositories which
are all grouped as sub-modules under the 
`webthree-umbrella <http://github.com/ethereum/webthree-umbrella>`_ repo
on Github.  We use `CMake <https://cmake.org/>`_ to generate build files on all platforms,
meaning that the workflow is very similar whatever operating system you use: ::

    git clone --recursive https://github.com/ethereum/webthree-umbrella.git

    git checkout release                                     Optionally, to switch to "release" branch
    git submodule update                                     perform these two steps.

    mkdir build                                              Make a directory for the build output
    cd build                                                 Switch into that directory

    cmake ..                                                 To generate a makefile.
    make                                                     To build that makefile on the command-line
    make -j <number>                                         Execute makefile with multiple cores in parallel

    cmake -G "Visual Studio 12 2013 Win64" ..                To generate Visual Studio solution
    msbuild cpp-ethereum.sln /p:Configuration=Release        To build that on the command-line

    cmake -G Xcode ..                                        To generate xcode project


Platform-specific instructions
--------------------------------------------------------------------------------

From there, follow the platform-specific instructions below.

.. toctree::
   :maxdepth: 2

   linux.rst
   windows.rst
   osx.rst
   android.rst
   ios.rst
   rpi.rst
   odroid.rst
   beaglebone.rst
   wandboard.rst
   linux-arm.rst


.. _Building from source:
 
Building from source
================================================================================

Overview
--------------------------------------------------------------------------------

The **cpp-ethereum** codebase lives on Github.com in the
`cpp-ethereum <http://github.com/ethereum/cpp-ethereum>`_ repository.

Between October 2015 and August 2016 it was split into various repositories
which were grouped as sub-modules under the 
`webthree-umbrella <http://github.com/ethereum/webthree-umbrella>`_ repository,
and you will likely see many references to **webthree-umbrella** online.  Those
all refer to the **cpp-ethereum** codebase during that period of its development.

We use a common `CMake <https://cmake.org/>`_ build system to generate
platform-specific build files, meaning that the workflow is very similar
whatever operating system you use:

* Install build tools and external packages (these are platform dependent)
* Clone the source code from the **webthree-umbrella** git repository
* Run CMake to generate a build file (makefile, Visual Studio solution, etc)
* Build it


Platform-specific instructions
--------------------------------------------------------------------------------

.. toctree::
   :maxdepth: 2

   linux.rst
   windows.rst
   macos.rst
   freebsd.rst
   android.rst
   ios.rst
   rpi.rst
   odroid.rst
   beaglebone.rst
   wandboard.rst
   linux-arm.rst


.. _Building from source:
 
Building from source
================================================================================

Overview
--------------------------------------------------------------------------------

The **cpp-ethereum** codebase is is mid-transition from several
Git repositories which are all grouped as sub-modules under the 
`webthree-umbrella <http://github.com/ethereum/webthree-umbrella>`_ repo
on Github back to `cpp-ethereum <http://github.com/ethereum/cpp-ethereum>`_.

As of right now (only for the v1.3.0 release), the canonical mainline is at:

https://github.com/bobsummerwill/cpp-ethereum/tree/merge_repos

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


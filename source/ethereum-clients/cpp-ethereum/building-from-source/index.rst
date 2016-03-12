
Building from source
================================================================================

The cpp-ethereum codebase is written in
`Modern C++ style <https://msdn.microsoft.com/en-CA/library/hh279654.aspx>`_,
split across a (probably unnecessarily) large number of libraries and
applications.   The libraries are dynamically linked (DLLs or SOs), although
we `plan to support static linkage
<https://github.com/ethereum/webthree-umbrella/issues/337>`_ soon too.

The build system is implemented in `CMake <https://cmake.org/>`_, which is
used to generate platform-specific build files - GNU makefiles, Visual
Studio solutions, xcode projects, etc.

To get the source code on your machine, the simplest approach is to clone the
whole `webthree-umbrella <http://github.com/ethereum/webthree-umbrella>`_
repository (or your fork of it) from Github, with recursive cloning
enabled, like so: ::

    git clone --recursive https://github.com/ethereum/webthree-umbrella.git

This repository gathers all of the C++ codebase under a single folder using
`git sub-modules <https://git-scm.com/book/en/v2/Git-Tools-Submodules>`_.


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


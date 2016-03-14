.. _Building from source:
 
Building from source
================================================================================

The **cpp-ethereum** codebase is spread over several Git repositories which
are all grouped as sub-modules under the 
`webthree-umbrella <http://github.com/ethereum/webthree-umbrella>`_ repo
on Github.

Clone that repository (or your own fork of it), with recursive cloning
enabled, like so: ::

    git clone --recursive https://github.com/ethereum/webthree-umbrella.git

The default branch is **develop**.   To switch to the latest versioned
release, execute the following command in the directory which you cloned into: ::

    git checkout release

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


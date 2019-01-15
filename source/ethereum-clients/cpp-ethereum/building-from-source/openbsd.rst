
################################################################################
Building for OpenBSD
################################################################################

Note: Working on the latest OpenBSD (v6.4)

Install the cmake, boost and z3 manually
================================================================================

use OpenBSD's package installer to install cmake, boost and z3 that we need to compile::

    pkg_add -iv cmake boost z3

Now we clone and compile: ::

    git clone --recursive https://github.com/ethereum/solidity.git
    cd solidity
    mkdir build
    cd build
    cmake ..
    make
    make install
    
Lets Symlink it to be able to call it just by typing solc:  ::
    
    ln -s /<path>/solidity/build/solc/solc /usr/local/bin/solc
b


################################################################################
Building for Linux
################################################################################

Building for Ubuntu
================================================================================

Building for Fedora
================================================================================

Building for ArchLinux
================================================================================

Install build dependencies: ::

    sudo pacman -S autoconf automake cmake gcc libtool v8-3.15 yasm git clang

Install client dependencies: ::

    sudo pacman -S argtable boost boost-libs curl crypto++ gmp jsoncpp leveldb libedit libjson-rpc-cpp-git libmicrohttpd miniupnpc ncurses libcl opencl-headers openssl python2 qt5-base qt5-declarative qt5-quick1 qt5-quickcontrols qt5-webengine qt5-webkit qt5-graphicaleffects readline snappy llvm scons gperftools``

Compile the source: ::

    mkdir -p build && cd build
    CXXFLAGS=-Wno-deprecated-declarations cmake .. -DCMAKE_INSTALL_PREFIX=/usr
    make -j $(nproc)

Executables can be found in **./build/\***


Building for openSUSE
================================================================================

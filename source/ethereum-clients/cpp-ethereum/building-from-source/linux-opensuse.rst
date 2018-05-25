
################################################################################
Installing dependencies for openSUSE
################################################################################

Here is how to get the dependencies needed to build the latest
webthree-umbrella on OpenSUSE. This was done on Leap 42.1 and 42.2, but there should be equivalent packages available for Tumbleweed and 13.x.

First install dependencies provided by the main repos: ::

    zypper in git automake autoconf libtool cmake gcc gcc-c++ \
        xkeyboard-config leveldb-devel boost-devel gmp-devel \
        libcryptopp-devel libminiupnpc-devel libqt5-qtbase-common-devel \
        libqt5-qtdeclarative-devel libQtWebKit-devel libqt5-qtwebengine-devel \
        libQt5Concurrent-devel Mesa ncurses-devel readline-devel libcurl-devel \
        llvm llvm-clang llvm-clang-devel llvm-devel libLLVM binutils \
        libmicrohttpd-devel jsoncpp-devel opencl-headers-1.2 zlib-devel 

If Opencl-headers-1.2 is not found, you can install it manually from the CLI:
    zypper addrepo http://download.opensuse.org/repositories/home:valmar73:crystfel-releases/openSUSE_13.1/home:valmar73:crystfel-releases.repo
    zypper refresh
    zypper install opencl-headers-1.2


It may be possible to use the generic `libOpenCL1`, but I have only tested with the
AMD proprietary package from the AMD drivers repo `fglrx64_opencl_SUSE421`

These packages are not in the standard repos but can be found using the OpenSUSE
build service package search and YaST 1-Click Install:

- libargtable2-devel
- libv8-3
- v8-devel

If you also have v8 from the chromium repo installed the devel package will
default to the 4.x branch which will not work. Use YaST or zypper to downgrade
this package to 3.x

Note that Opencl-headers is used to mine the chain with GPU. If this is not a requirement, you can bypass it when creating the makefile (cmake -DETHASHCL=0 .. ) instead of (cmake ..)

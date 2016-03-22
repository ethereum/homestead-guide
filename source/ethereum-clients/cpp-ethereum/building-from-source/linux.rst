

################################################################################
Building for Linux
################################################################################

(Start at :ref:`Building from source`. These are the Linux specific steps.
That is the starting point)

NOTE - It may be possible to get the client working for Linux 32-bit, by
disabling EVMJIT and maybe other features too.  We might accept
pull-requests to add such support, but we will not put any of our
own development time into supporting Linux 32-bit builds.

After cloning the **webthree-umbrella** repo, the crux of the build process
on Linux platforms is incredibly simple: ::

    mkdir build
    cd build
    cmake ..
    make               (or make -j <number> for parallel builds)

But before it is possible to get to that stage we have to wade through
a horror-show of distro-specific packaging system steps to install
external packages which we depend on.

The sections below attempt to capture those distro-specific steps for
installing dependencies.   You will need to run through one of these
sequences before you can do the simple build steps above.



Installing dependencies for Ubuntu
================================================================================

Ubuntu Trusty Tahr (14.04)
--------------------------------------------------------------------------------
Steps: ::

    sudo apt-add-repository ppa:george-edison55/cmake-3.x

    sudo apt-get -y update
    sudo apt-get -y install language-pack-en-base
    sudo dpkg-reconfigure locales
    sudo apt-get -y install software-properties-common

    sudo add-apt-repository "deb http://llvm.org/apt/trusty/ llvm-toolchain-trusty-3.7 main"
    wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key | sudo apt-key add -
    sudo apt-get -y update
    sudo apt-get -y install llvm-3.7-dev

    sudo add-apt-repository -y ppa:ethereum/ethereum-qt
    sudo add-apt-repository -y ppa:ethereum/ethereum
    sudo add-apt-repository -y ppa:ethereum/ethereum-dev
    sudo apt-get -y update
    sudo apt-get -y upgrade

    sudo apt-get -y install build-essential git cmake libboost-all-dev libgmp-dev \
	libleveldb-dev libminiupnpc-dev libreadline-dev libncurses5-dev \
	libcurl4-openssl-dev libcryptopp-dev libmicrohttpd-dev libjsoncpp-dev \
	libargtable2-dev libedit-dev mesa-common-dev ocl-icd-libopencl1 opencl-headers \
	libgoogle-perftools-dev qtbase5-dev qt5-default qtdeclarative5-dev \
	libqt5webkit5-dev libqt5webengine5-dev ocl-icd-dev libv8-dev libz-dev
	
    sudo apt-get -y install libjson-rpc-cpp-dev
    sudo apt-get -y install qml-module-qtquick-controls qml-module-qtwebengine

Ubuntu Utopic Unicorn (14.10)
--------------------------------------------------------------------------------
Steps: ::

    sudo apt-get -y update
    sudo apt-get -y install language-pack-en-base
    sudo dpkg-reconfigure locales
    sudo apt-get -y install software-properties-common

    sudo add-apt-repository "deb http://llvm.org/apt/utopic/ llvm-toolchain-utopic-3.7 main"
    wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key | sudo apt-key add -
    sudo apt-get -y update
    sudo apt-get -y install llvm-3.7-dev

    sudo add-apt-repository -y ppa:ethereum/ethereum-qt
    sudo add-apt-repository -y ppa:ethereum/ethereum
    sudo add-apt-repository -y ppa:ethereum/ethereum-dev
    sudo apt-get -y update
    sudo apt-get -y upgrade

    sudo apt-get -y install build-essential git cmake libboost-all-dev libgmp-dev \
	libleveldb-dev libminiupnpc-dev libreadline-dev libncurses5-dev \
	libcurl4-openssl-dev libcryptopp-dev libmicrohttpd-dev libjsoncpp-dev \
	libargtable2-dev libedit-dev mesa-common-dev ocl-icd-libopencl1 opencl-headers \
	libgoogle-perftools-dev qtbase5-dev qt5-default qtdeclarative5-dev \
	libqt5webkit5-dev libqt5webengine5-dev ocl-icd-dev libv8-dev libz-dev

    sudo apt-get -y install libjson-rpc-cpp-dev
    sudo apt-get -y install qml-module-qtquick-controls qml-module-qtwebengine

Ubuntu Vivid Vervet (15.04)
--------------------------------------------------------------------------------
Steps: ::

    sudo apt-get -y update
    sudo apt-get -y install language-pack-en-base
    sudo dpkg-reconfigure locales
    sudo apt-get -y install software-properties-common

    sudo add-apt-repository "deb http://llvm.org/apt/vivid/ llvm-toolchain-vivid-3.7 main"
    wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key | sudo apt-key add -
    sudo apt-get -y update
    sudo apt-get -y install llvm-3.7-dev

    sudo add-apt-repository -y ppa:ethereum/ethereum-qt
    sudo add-apt-repository -y ppa:ethereum/ethereum
    sudo add-apt-repository -y ppa:ethereum/ethereum-dev
    sudo apt-get -y update
    sudo apt-get -y upgrade

    sudo apt-get -y install build-essential git cmake libboost-all-dev libgmp-dev \
	libleveldb-dev libminiupnpc-dev libreadline-dev libncurses5-dev \
	libcurl4-openssl-dev libcryptopp-dev libmicrohttpd-dev libjsoncpp-dev \
	libargtable2-dev libedit-dev mesa-common-dev ocl-icd-libopencl1 opencl-headers \
	libgoogle-perftools-dev qtbase5-dev qt5-default qtdeclarative5-dev \
	libqt5webkit5-dev libqt5webengine5-dev ocl-icd-dev libv8-dev libz-dev

    sudo apt-get -y install libjson-rpc-cpp-dev
    sudo apt-get -y install qml-module-qtquick-controls qml-module-qtwebengine

Ubuntu Wily Werewolf (15.10)
--------------------------------------------------------------------------------
Steps: ::

    sudo apt-get -y update
    sudo apt-get -y install language-pack-en-base
    sudo dpkg-reconfigure locales
    sudo apt-get -y install software-properties-common

    sudo add-apt-repository "deb http://llvm.org/apt/wily/ llvm-toolchain-wiley-3.7 main"
    wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key | sudo apt-key add -
    sudo apt-get -y update
    sudo apt-get -y install llvm-3.7-dev

    sudo add-apt-repository -y ppa:ethereum/ethereum-qt
    sudo add-apt-repository -y ppa:ethereum/ethereum
    sudo add-apt-repository -y ppa:ethereum/ethereum-dev
    sudo apt-get -y update
    sudo apt-get -y upgrade

    sudo apt-get -y install build-essential git cmake libboost-all-dev libgmp-dev \
	libleveldb-dev libminiupnpc-dev libreadline-dev libncurses5-dev \
	libcurl4-openssl-dev libcryptopp-dev libmicrohttpd-dev libjsoncpp-dev \
	libargtable2-dev libedit-dev mesa-common-dev ocl-icd-libopencl1 opencl-headers \
	libgoogle-perftools-dev qtbase5-dev qt5-default qtdeclarative5-dev \
	libqt5webkit5-dev libqt5webengine5-dev ocl-icd-dev libv8-dev libz-dev

    sudo apt-get -y install libjsonrpccpp-dev
    sudo apt-get -y install qml-module-qtquick-controls qml-module-qtwebengine

Ubuntu Xenial Xerus (16.04)
--------------------------------------------------------------------------------

Nobody has reported that they are building for Xenial yet.   Please let us know
if it is broken or works for you.

Installing dependencies for Fedora
================================================================================

Fedora 20
--------------------------------------------------------------------------------
Steps: ::

    yum install git automake autoconf libtool cmake gcc gcc-c++ xkeyboard-config \
            leveldb-devel boost-devel gmp-devel cryptopp-devel miniupnpc-devel \
            qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtquick1-devel qt5-qtwebkit-devel \
            mesa-dri-drivers snappy-devel ncurses-devel readline-devel curl-devel \
            python-devel

Fedora 21
--------------------------------------------------------------------------------
Steps: ::

    yum install git automake autoconf libtool cmake gcc gcc-c++ xkeyboard-config \
            leveldb-devel boost-devel gmp-devel cryptopp-devel miniupnpc-devel \
            qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtquick1-devel qt5-qtwebkit-devel \
            mesa-dri-drivers snappy-devel ncurses-devel readline-devel curl-devel \
            python-devel jsoncpp-devel argtable-devel

Build json-rpc from github as per https://github.com/ethereum/cpp-ethereum/issues/617: ::

    git clone https://github.com/cinemast/libjson-rpc-cpp
    cd libjson-rpc-cpp
    git checkout tags/v0.3.2
    mkdir -p build
    cd build
    cmake .. && make
    sudo make install
    sudo ldconfig

Fedora 22
--------------------------------------------------------------------------------
Steps: ::

Fedora 22 dependencies there may be more depends what you have already installed
    dnf install git automake autoconf libtool cmake gcc gcc-c++ xkeyboard-config \
    leveldb-devel boost-devel gmp-devel cryptopp-devel miniupnpc-devel \
    mesa-dri-drivers snappy-devel ncurses-devel readline-devel curl-devel \
    python-devel jsoncpp-devel argtable-devel

1. install gcc version 4.9! Fedora 22 comes with a different compiler (CC v5.3).
This one wont compile webthree-umbrella 4 me so i installed gcc version 4.9 from SRC!
Ceck that you have a working gcc4.9 install in /usr/local i installed it in
/home/app/gcc49 its your choice read manual how to compile gcc in google! After that
you have to compile everything you need 4 webthree-umbrella with gcc4.9 so before
every cmake "export CXX=/home/app/gcc49/bin/g++" "export CC=/home/app/gcc49/bin/gcc"
with this you use gcc4.9 to compile instat of the one that comes with the Distri F22
its not recommended to uninstall the compiler that comes with your Distri! You can
also work with symlinking.

2. Install from Fedora COPR REPO LLVM3.7 with "dnf copr enable alonid/llvm-3.7"
followed by "dnf install llvm-3.7 llvm-3.7-devel llvm-3.7-static llvm-3.7-libs".
I had to do this because Fedora 22 comes with llvm-3.5 from stock repos! There
may be other solutions but this one worked 4 me

3. Install CryptoPP from SRC https://github.com/weidai11/cryptopp CRYPTOPP_5_6_2
	git clone https://github.com/weidai11/cryptopp
	cd cryptopp
	git checkout release/CRYPTOPP_5_6_2
	Mkdir build
	cd build
	export CXX=/home/app/gcc49/bin/g++ <- be sure to compile with gcc4.9
	export CC=/home/app/gcc49/bin/gcc <- be sure to compile with gcc4.9
	cmake ..
	make
	make install

4. Install QT5 from COPR "dnf copr enable @kdesig/Qt5" newer QT5 version
dnf install qt5-* this should install QT5 version 5.6.0 in COPR repo are other QT5
Packages from other users i didnt test them

5. Install qtwebengine from https://github.com/qtproject/qtwebengine i installed
version 5.6.0 others may also work find it out :D
	git clone https://github.com/qtproject/qtwebengine
	cd qtwebengine
	git checkout release/v5.6.0
	qmake-qt5 <- in other distros its just called qmake in fedora 22 qmake-qt5
	make
	make install
	
6. Install json-rpc from github https://github.com/ethereum/cpp-ethereum/issues/617
    	git clone https://github.com/cinemast/libjson-rpc-cpp
    	cd libjson-rpc-cpp
    	git checkout tags/v0.4.2
    	mkdir -p build
    	cd build
	export CXX=/home/app/gcc49/bin/g++ <- be sure to compile with gcc4.9
	export CC=/home/app/gcc49/bin/gcc <- be sure to compile with gcc4.9	
    	cmake .. && make
    	sudo make install
    	sudo ldconfig

Be sure to check if jsonrpcstub works in console enter "jsonrpcstub" and look if its responding.
If it answers No Argument or s-l-t it works but if you get no such file to blabla.so you have to
symlinking the missing ones to your libs dir /usr/local/lib64 or usr/local/lib depends where the
file blabla.so is try to find it with "updatedb" and than "locate blabla.so"

7. Try to compile now it should work if not there a missing symlinks cause of no such file easyfix
or there are some missing Packages try to find them with dnf like this "dnf search packname*" or
"dnf list packname*" all i can say its not a 5 min compile of webthree-umbrella njoy Tflux99: ::


Installing dependencies for openSUSE
================================================================================

Here is how to get the dependencies needed to build the latest
webthree-umbrella on OpenSUSE. This was done on Leap 42.1, but there should be equivalent packages available for Tumbleweed and 13.x.

First install dependencies provided by the main repos: ::

    zypper in git automake autoconf libtool cmake gcc gcc-c++ \
	xkeyboard-config leveldb-devel boost-devel gmp-devel \
	cryptopp-devel libminiupnpc-devel libqt5-qtbase-common-devel \
	libqt5-qtdeclarative-devel libQTWebKit-devel libqt5-qtwebengine-devel \
	libQt5Concurrent-devel Mesa ncurses-devel readline-devel libcurl-devel \
	llvm llvm-clang llvm-clang-devel llvm-devel libLLVM binutils \
	libmicrohttp-devel jsoncpp-devel opencl-headers-1.2 zlib-devel 

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


Installing dependencies for ArchLinux
================================================================================

Install build dependencies: ::

    sudo pacman -S autoconf automake cmake gcc libtool v8-3.15 yasm git clang

Install client dependencies: ::

    sudo pacman -S argtable boost boost-libs curl crypto++ gmp jsoncpp leveldb libedit libjson-rpc-cpp-git libmicrohttpd miniupnpc ncurses libcl opencl-headers openssl python2 qt5-base qt5-declarative qt5-quick1 qt5-quickcontrols qt5-webengine qt5-webkit qt5-graphicaleffects readline snappy llvm scons gperftools

Compile the source: ::

    mkdir -p build && cd build
    CXXFLAGS=-Wno-deprecated-declarations cmake .. -DCMAKE_INSTALL_PREFIX=/usr
    make -j $(nproc)

Executables can be found in **./build/\***

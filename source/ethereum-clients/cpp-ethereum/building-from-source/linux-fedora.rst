
################################################################################
Installing dependencies for Fedora
################################################################################

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

Fedora 22 dependencies there may be more depends what you have already installed: ::

    dnf install git automake autoconf libtool cmake gcc gcc-c++ xkeyboard-config \
    leveldb-devel boost-devel gmp-devel cryptopp-devel miniupnpc-devel \
    mesa-dri-drivers snappy-devel ncurses-devel readline-devel curl-devel \
    python-devel jsoncpp-devel argtable-devel

Install gcc version 4.9! Fedora 22 comes with a different compiler (CC v5.3).
This one wont compile webthree-umbrella 4 me so i installed gcc version 4.9 from SRC!

Check that you have a working gcc4.9 install in /usr/local i installed it in
/home/app/gcc49 its your choice read manual how to compile gcc in google! After that
you have to compile everything you need 4 webthree-umbrella with gcc4.9 so before
every cmake: ::

    export CXX=/home/app/gcc49/bin/g++
	export CC=/home/app/gcc49/bin/gcc
	
With this you use gcc4.9 to compile instead of the one that comes with the
distro F22.  Its not recommended to uninstall the compiler that comes with your
distro! You can also work with symlinking.

Install from Fedora COPR REPO LLVM3.7 with: ::

    dnf copr enable alonid/llvm-3.7
    dnf install llvm-3.7 llvm-3.7-devel llvm-3.7-static llvm-3.7-libs

I had to do this because Fedora 22 comes with llvm-3.5 from stock repos! There
may be other solutions but this one worked 4 me

Install CryptoPP from SRC https://github.com/weidai11/cryptopp CRYPTOPP_5_6_2: ::

    git clone https://github.com/weidai11/cryptopp
    cd cryptopp
    git checkout release/CRYPTOPP_5_6_2
    mkdir build
    cd build
    export CXX=/home/app/gcc49/bin/g++ <- be sure to compile with gcc4.9
    export CC=/home/app/gcc49/bin/gcc <- be sure to compile with gcc4.9
    cmake ..
    make
    make install

Install QT5 from COPR "dnf copr enable @kdesig/Qt5" newer QT5 version: ::

    dnf install qt5-*
	
this should install QT5 version 5.6.0 in COPR repo are other QT5.  Packages from other users i didnt test them

Install qtwebengine from https://github.com/qtproject/qtwebengine i installed
version 5.6.0 others may also work find it out :D ::

    git clone https://github.com/qtproject/qtwebengine
    cd qtwebengine
    git checkout release/v5.6.0
    qmake-qt5 <- in other distros its just called qmake in fedora 22 qmake-qt5
    make
    make install
	
Install json-rpc from github https://github.com/ethereum/cpp-ethereum/issues/617: ::

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

Try to compile now it should work if not there a missing symlinks cause of no such file easyfix
or there are some missing Packages try to find them with dnf like this "dnf search packname*" or
"dnf list packname*" all i can say its not a 5 min compile of webthree-umbrella enjoy Tflux99.

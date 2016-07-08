
################################################################################
Installing dependencies for Debian
################################################################################

Debian Jessie (8.5)
--------------------------------------------------------------------------------

.. warning::

    GUI applications haven't been tried on Debian. So, to build without GUI applications use: ::

        cmake .. -DGUI=0

Steps: ::

    sudo apt-get -y install gcc
    sudo apt-get -y install g++
    sudo apt-get -y install unzip
    sudo apt-get -y install cmake
Make sure you installed the cmake version 3.5.2. If apt-get installed an older version, compile it from source following the instructions in this `link <https://cmake.org/download/>`_ ::

    sudo apt-get -y install libboost-all-dev
    sudo apt-get -y install libgmp-dev
    sudo apt-get -y install libjsoncpp-dev
    sudo apt-get -y install libleveldb-dev

To install cryptopp it's necessary build from source: ::

    mkdir ~/download
    cd ~/download
    wget https://www.cryptopp.com/cryptopp563.zip
    
    mkdir cryptopp
    mv cryptopp563.zip cryptopp
    cd cryptopp
    unzip -a cryptopp563.zip

    make static dynamic cryptest.exe

Testing installation: ::
	
    ./cryptest.exe v

Verify results, and do another test: ::

    ./cryptest.exe tv

Testing ok? Let's continue: ::

    make libcryptopp.a libcryptopp.so cryptest.exe
    sudo make install PREFIX=/usr/local

CryptoPP installed!: ::

    sudo apt-get -y install libminiupnpc-dev

Now, install LLVM building from source: ::

    sudo apt-get -y install build-essential
    mkdir ~/download/llvm
    cd ~/download/llvm
    wget -c http://llvm.org/releases/3.8.0/llvm-3.8.0.src.tar.xz
    wget -c http://llvm.org/releases/3.8.0/cfe-3.8.0.src.tar.xz
    wget -c http://llvm.org/releases/3.8.0/compiler-rt-3.8.0.src.tar.xz

    tar -xf llvm-3.8.0.src.tar.xz
    tar -xf cfe-3.8.0.src.tar.xz
    tar -xf compiler-rt-3.8.0.src.tar.xz
    
    mv llvm-3.8.0.src llvm-3.8.0
    mv cfe-3.8.0.src cfe
    mv compiler-rt-3.8.0.src compiler-rt

    mv cfe llvm-3.8.0/tools
    mv compiler-rt llvm-3.8.0/projects/

    mkdir build
    cd build

    cmake ../llvm-3.8.0
    make
    sudo make install
    sudo ldconfig

Coming back to apt-get: ::

    sudo apt-get -y install opencl-dev
    sudo apt-get -y install libcurl4-openssl-dev

Install json-rpc-cpp building from source: ::

    sudo apt-get source libmicrohttpd-dev
    sudo apt-get -y install libargtable2-dev
    sudo apt-get -y install libmicrohttpd-dev

    git clone git://github.com/cinemast/libjson-rpc-cpp.git
    mkdir -p libjson-rpc-cpp/build
    cd libjson-rpc-cpp/build
    cmake
    make
    sudo make install
    sudo ldconfig  

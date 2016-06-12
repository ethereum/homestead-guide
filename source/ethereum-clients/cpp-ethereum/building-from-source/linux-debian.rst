
################################################################################
Installing dependencies for Debian
################################################################################

Debian Jessie (8.5)
--------------------------------------------------------------------------------
Steps: ::

    sudo apt-get -y install gcc
    sudo apt-get -y install g++
    sudo apt-get -y install cmake
    sudo apt-get -y install unzip

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
    wget -c http://llvm.org/releases/3.7.1/llvm-3.8.0.src.tar.xz
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

Troubleshooting
+++++++++++++++

* In case of the error below: ::

    CMake Error at libethereum/test/CMakeLists.txt:26 (file):
      file STRINGS file
      "/home/<user>/webthree-umbrella/libethereum/test/./..//./fuzzHelper.cpp"
      cannot be read.

 
    CMake Error at libethereum/test/CMakeLists.txt:34 (add_test):
      add_test given test NAME ""RandomTestCreationSuite"/&createRandomTest"
      which already exists in this directory.


    CMake Error at libethereum/test/CMakeLists.txt:26 (file):
      file STRINGS file
      "/home/<user>/webthree-umbrella/libethereum/test/./..//./createRandomTest.cpp"
      cannot be read.


    CMake Error at libethereum/test/CMakeLists.txt:34 (add_test):
      add_test given test NAME ""RandomTestCreationSuite"/&createRandomTest"
      which already exists in this directory.


    CMake Error at libethereum/test/CMakeLists.txt:26 (file):
      file STRINGS file
      "/home/<user>/webthree-umbrella/libethereum/test/./..//./icap.cpp" cannot
      be read.


     CMake Error at libethereum/test/CMakeLists.txt:34 (add_test):
       add_test given test NAME ""RandomTestCreationSuite"/&createRandomTest"
       which already exists in this directory.

 The workaround is ``$ cmake .. -DGUI=0 -DTESTS=0``

* In case of the error below during ``make``: ::

    [ 49%] Building C object libethereum/libethash/CMakeFiles/ethash.dir/internal.c.o
    /home/<user>/webthree-umbrella/libethereum/libethash/internal.c: In function ‘ethash_light_compute_internal’:
    /home/<user>/webthree-umbrella/libethereum/libethash/internal.c:243:34: error: array subscript is above array bounds [-Werror=array-bounds]
    [   uint32_t reduction = mix->words[w + 0];
                                       ^
 It will necessary an workaround, changing the file ``webthree-helpers/blob/develop/cmake/EthCompilerSettings.cmake``

 First, find the code: ::

    21    # Enables all the warnings about constructions that some users consider questionable,
    22    # and that are easy to avoid.  Also enable some extra warning flags that are not
    23    # enabled by -Wall.   Finally, treat at warnings-as-errors, which forces developers
    24    # to fix warnings as they arise, so they don't accumulate "to be fixed later".
    25    add_compile_options(-Wall)
    26    add_compile_options(-Wextra)
    27    add_compile_options(-Werror)

 and comment line 27 ``add_compile_options(-Werror)``: ::

    27    # add_compile_options(-Werror)

 Now, find the code: ::

     98    # TODO - Nail down exactly where these warnings are manifesting and
     99	   # try to suppress them in a more localized way.   Notes in this file
    100	   # indicate that the first is needed for sepc256k1 and that the
    101    # second is needed for the (clog, cwarn) macros.  These will need
    102    # testing on at least OS X and Ubuntu.
    103    add_compile_options(-Wno-unused-function)
    104    add_compile_options(-Wno-dangling-else)

 and include a new line ``add_compile_options(-Wno-array-bounds)``: ::

    102    # testing on at least OS X and Ubuntu.
    103    add_compile_options(-Wno-unused-function)
    104    add_compile_options(-Wno-dangling-else)
    105    add_compile_optoins(-Wno-array-bounds)


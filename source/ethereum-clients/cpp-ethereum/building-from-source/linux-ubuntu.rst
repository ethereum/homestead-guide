
################################################################################
Installing dependencies for Ubuntu
################################################################################

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

    sudo add-apt-repository "deb http://llvm.org/apt/wily/ llvm-toolchain-wily-3.7 main"
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
Steps: ::

    sudo apt-get -y update
    sudo apt-get -y install language-pack-en-base
    sudo dpkg-reconfigure locales
    sudo apt-get -y install software-properties-common

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
    sudo apt-get -y install qml-module-qtquick-controls qml-module-qtwebengine \
	qml-module-qtquick-privatewidgets qml-module-qtquick-dialogs \
	qml-module-qt-labs-settings qml-module-qtgraphicaleffects


################################################################################
Installing dependencies for Fedora
################################################################################

Fedora 24
--------------------------------------------------------------------------------
Steps: ::
  
    dnf install git automake autoconf libtool cmake gcc gcc-c++ xkeyboard-config \
            leveldb-devel boost-devel gmp-devel cryptopp-devel miniupnpc-devel \
            qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtquick1-devel qt5-qtwebkit-devel \
            mesa-dri-drivers snappy-devel ncurses-devel readline-devel curl-devel \
            python-devel jsoncpp-devel argtable-devel libmicrohttpd-devel


Make sure you have cloned the repository recursively. If not please clone the submodules of the respository as well.
It may happen that after `# make install`, you might not be able to run eth because of linking errors. In that case you have to add the shared objects of eth into your load path for shared objects.           

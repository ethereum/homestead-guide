
################################################################################
Building for FreeBSD
################################################################################

NOTE - Once the packages are in the FreeBSD main ports this guide should be
changed to something much more simple

Install the ports manually
================================================================================
For some of this steps you must require a root access to modify the ports directory.

The webthree-umbrella depends on [libjson-rpc-cpp.shar](https://raw.githubusercontent.com/enriquefynn/webthree-umbrella-port/master/libjson-rpc-cpp.shar) that is also not in the ports system.

First you need to download the shar file and place it on your ports directory under the "devel" session, usually
/usr/ports/devel ::

    curl https://raw.githubusercontent.com/enriquefynn/webthree-umbrella-port/master/libjson-rpc-cpp.shar > /usr/ports/devel/libjson-rpc-cpp.shar

Now we execute the script with: ::

    cd /usr/ports/devel
    sh libjson-rpc-cpp.shar

This will create the libjson-rpc-cpp port. Now you should do the same for the webthree-umbrella port, we should get the [webthree-umbrella](https://raw.githubusercontent.com/enriquefynn/webthree-umbrella-port/master/webthree-umbrella.shar) file and create the port under "net-p2p" directory. ::

    curl https://raw.githubusercontent.com/enriquefynn/webthree-umbrella-port/master/webthree-umbrella.shar> /usr/ports/net-p2p/webthree-umbrella.shar
    cd /usr/ports/net-p2p
    sh webthree-umbrella.shar


Build and Install
================================================================================

Now you can navigate to the webthree-umbrella directory and install the port: ::

    cd /usr/ports/net-p2p/webthree-umbrella
    make install clean

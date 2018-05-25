
################################################################################
Installing dependencies for Arch Linux
################################################################################

Compiling webthree-umbrella on Arch Linux requires dependencies from both the `official repositories <https://wiki.archlinux.org/index.php/Official_repositories>`_
and the `Arch User Repository (AUR) <https://wiki.archlinux.org/index.php/Arch_User_Repository>`_. To install packages from the official repositories `pacman <https://wiki.archlinux.org/index.php/Pacman>`_ is used.
For installation of packages from the AUR, a number of AUR helpers is `available <https://wiki.archlinux.org/index.php/AUR_helpers>`_. For this guide, `yaourt <http://archlinux.fr/yaourt-en>`_ AUR helper is used.

Installing dependencies
================================================================================

    # from official repositories
    sudo pacman -Sy git base-devel cmake boost crypto++ leveldb llvm miniupnpc libcl opencl-headers libmicrohttpd qt5-base qt5-webengine

    # from AUR
    yaourt -Sy libjson-rpc-cpp


Compiling the source code
================================================================================

During this step, an installation folder for the Ethereum can be specified.
Specification of the folder is optional though. If not given, the
binary files will be located in the build folder. However, for this guide,
it is assumed that the Ethereum files will be installed under `/opt/eth`. The reason for
using `/opt` is that it makes much easier to delete the Ethereum files later on,
as compared to having them installed under, e.g., `/usr`. Also `/opt` is commonly used
to install software that is not managed by packaging systems, such as manually 
compiled programs. ::

    # enter webthree-umbrella folder after cloning its github repository
    cd webthree-umbrella

    # make a build folder and enter into it
    mkdir -p build && cd build

    # create build files and specify Ethereum installation folder
    cmake .. -DCMAKE_INSTALL_PREFIX=/opt/eth

    # compile the source code
    make

    # alternatively it is possible to specify number of compilation threads
    # for example to use 4 threads execute make as follows:
    # make -j 4

    # install the resulting binaries, shared libraries and header files into /opt
    sudo make install


After successful compilation and installation, Ethereum binaries can be found in `/opt/eth/bin`,
shared libraries in `/opt/eth/lib`, and header files in `/opt/eth/include`.


Specifying Ethereum libraries path
================================================================================

Since Ethereum was installed in `/opt/eth`, executing its binaries can result in linker error due to not being
able to find the Ethereum shared libraries. To rectify this issue, it is needed to add the folder containing
Ethereum shared libraries into `LD_LIBRARY_PATH` environmental variable: ::

    # update ~/.bashrc
    echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/eth/lib" >> ~/.bashrc

    # reload ~/.bashrc
    source ~/.bashrc


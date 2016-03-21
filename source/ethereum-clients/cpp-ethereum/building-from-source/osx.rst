
Building for OS X
================================================================================

(Start at :ref:`Building from source`. These are the OS X specific steps.
That is the starting point)

It is impossible for us to avoid OS X build breaks because `Homebrew is a "rolling
release" package manager
<https://github.com/ethereum/webthree-umbrella/issues/118>`_
which means that the ground will forever be moving underneath us unless we add
all external dependencies to our
`Homebrew tap <http://github.com/ethereum/homebrew-ethereum>`_, or add them as
git sub-modules within the umbrella projects.  End-user results vary depending
on when they are build the project.  Building yesterday may have worked for
you, but that doesn't guarantee that your friend will have the same result
today on their machine.   Needless to say, this isn't a happy situation.

If you hit build breaks for OS X please look through the `Github issues
<https://github.com/ethereum/webthree-umbrella/issues>`_ to see whether the
issue you are experiencing has already been reported.   If so, please comment
on that existing issue.  If you don't see anything which looks similar,
please create a new issue, detailing your OS X version, cpp-ethereum version,
hardware and any other details you think might be relevant.   Please add
verbose log files via `gist.github.com <http://gist.github.com>`_ or a
similar service.   The `cpp-ethereum gitter channel
<https://gitter.im/ethereum/cpp-ethereum>`_ is where we hang out, and try
to work together to get known issues resolved.

We **only** support the two most recent OS X versions:

- `OS X Yosemite (10.10) <https://en.wikipedia.org/wiki/OS_X_Yosemite>`_
- `OS X El Capitan (10.11) <https://en.wikipedia.org/wiki/OS_X_El_Capitan>`_

The cpp-ethereum code base does not build on older OS X versions and this
is not something which we will ever support.  If you are using an older
OS X version, we recommend that you update to the latest release, not
just so that you can build cpp-ethereum, but for your own peace of mind.


Pre-requisites
--------------------------------------------------------------------------------

All OS X builds require you to `install the Homebrew <http://brew.sh>`_
package manager.  Here's how to `uninstall Homebrew
<https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/FAQ.md#how-do-i-uninstall-homebrew>`_,
if you ever want to start again from scratch.  

Install `xcode <https://developer.apple.com/xcode/download/>`_, which contains
the compiler, the IDE and other Apple development tools.

Install `XQuartz <http://xquartz.macosforge.org/landing/>`_ X11 Window
system if you want to build the GUI apps.


Install external dependencies
--------------------------------------------------------------------------------

Install all required external dependencies ::

    brew update
    brew upgrade
    brew install boost --c++11
    brew install cmake cryptopp miniupnpc leveldb gmp jsoncpp libmicrohttpd libjson-rpc-cpp llvm37
    brew install homebrew/versions/v8-315
    brew install qt5 --with-d-bus

**NB:  The Qt5 step takes many hours on most people's machines.**  This is because it is
using non-default build settings which result in build-from-source.  It also appears
to use around 20Gb of temporary disk space.   Beware!

You can either generate a makefile and build on command-line or generate an
Xcode project and build Ethereum in the IDE.

Generate a makefile
--------------------------------------------------------------------------------

From the project root: ::

    mkdir build
    cd build
    cmake ..
    make -j6
    make install

This will also install the cli tool and libs into /usr/local.

Xcode
--------------------------------------------------------------------------------

From the project root: ::

    mkdir build_xc
    cd build_xc
    cmake -G Xcode ..

This will generate an Xcode project file along with some configs for you: **cpp-ethereum.xcodeproj**. Open this file in XCode and you should be able to build the project


Troubleshooting
--------------------------------------------------------------------------------

* error: verify_app failed - you will need to use the `QTBUG-50155-workaround <https://github.com/ethereum/webthree-umbrella/wiki/QTBUG-50155-workaround>`_
* Build error "non-virtual thunk to CryptoPP::Rijndael::Dec::AdvancedProcessBlocks" - this is due to a `bad bottle for CryptoPP 5.6.3 <https://github.com/ethereum/webthree-umbrella/wiki/CryptoPP-5.6.3-workaround>`_
* Unexpected "No such file or directory (or similar)" error e.g. `Sentinel.h.tmp`, `AdminUtilsFace.h.tmp`. Read the `libjson-rpc-cpp workaround <https://github.com/ethereum/webthree-umbrella/wiki/libjson-rpc-cpp-OS-X-workaround>`_
* Build or runtime errors, complaining about missing `libmicrohttpd.10.dylib <https://github.com/ethereum/webthree-umbrella/wiki/homebrew-47806-workaround>`_

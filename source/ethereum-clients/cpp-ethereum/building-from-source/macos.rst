
Building for OS X
================================================================================

Overview - Here be dragons!
--------------------------------------------------------------------------------

It is impossible for us to avoid OS X build breaks because `Homebrew is a "rolling
release" package manager
<https://github.com/ethereum/webthree-umbrella/issues/118>`_
which means that the ground will forever be moving underneath us unless we add
all external dependencies to our
`Homebrew tap <http://github.com/ethereum/homebrew-ethereum>`_, or add them as
git sub-modules.  End-user results vary depending
on when they are build the project.  Building yesterday may have worked for
you, but that doesn't guarantee that your friend will have the same result
today on their machine.   Needless to say, this isn't a happy situation.

If you hit build breaks for OS X please look through the `Github issues
<https://github.com/ethereum/cpp-ethereum/issues>`_ to see whether the
issue you are experiencing has already been reported.   If so, please comment
on that existing issue.  If you don't see anything which looks similar,
please create a new issue, detailing your OS X version, cpp-ethereum version,
hardware and any other details you think might be relevant.   Please add
verbose log files via `gist.github.com <http://gist.github.com>`_ or a
similar service.

The `cpp-ethereum-development 
<https://gitter.im/ethereum/cpp-ethereum-development>`_ gitter channel is where we hang out, and try
to work together to get known issues resolved.

We only support the following OS X versions:

- `OS X Mavericks (10.9) <https://en.wikipedia.org/wiki/OS_X_Mavericks>`_
- `OS X Yosemite (10.10) <https://en.wikipedia.org/wiki/OS_X_Yosemite>`_
- `OS X El Capitan (10.11) <https://en.wikipedia.org/wiki/OS_X_El_Capitan>`_

The cpp-ethereum code base does not build on older OS X versions and this
is not something which we will ever support.  If you are using an older
OS X version, we recommend that you update to the latest release, not
just so that you can build cpp-ethereum, but for your own security.


Clone the repository
--------------------------------------------------------------------------------

To clone the source code, execute the following command: ::

    git clone --recursive https://github.com/ethereum/cpp-ethereum.git
    cd cpp-ethereum


Pre-requisites and external dependencies
--------------------------------------------------------------------------------

Ensure that you have the latest version of
`xcode installed <https://developer.apple.com/xcode/download/>`_.
This contains the `Clang C++ compiler <https://en.wikipedia.org/wiki/Clang>`_, the
`xcode IDE <https://en.wikipedia.org/wiki/Xcode>`_ and other Apple development
tools which are required for building C++ applications on OS X.
If you are installing xcode for the first time, or have just installed a new
version then you will need to agree to the license before you can do
command-line builds: ::

    sudo xcodebuild -license accept

Our OS X builds require you to `install the Homebrew <http://brew.sh>`_
package manager for installing external dependencies.
Here's how to `uninstall Homebrew
<https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/FAQ.md#how-do-i-uninstall-homebrew>`_,
if you ever want to start again from scratch.

We now have a "one button" script which installs all required external dependencies
on macOS and on numerous Linux distros.   This used to a multi-step manual process: ::

    ./scripts/install_deps.sh


Command-line build
--------------------------------------------------------------------------------

From the project root: ::

    mkdir build
    cd build
    cmake ..
    make -j4             (or different value, depending on your number of CPU cores)


Install your own build
--------------------------------------------------------------------------------

You can also use the same Makefile to install your own build globally on your machine: ::

    make install

This will install binaries into **/usr/local/** and **/usr/bin/**.


Generate xcode project
--------------------------------------------------------------------------------

From the project root: ::

    mkdir build_xc
    cd build_xc
    cmake -G Xcode ..

This will generate an Xcode project file called **cpp-ethereum.xcodeproj**,
which you can then open with xcode and build/debug/run.

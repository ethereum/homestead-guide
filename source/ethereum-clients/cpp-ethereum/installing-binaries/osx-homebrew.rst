
OS X Homebrew packages
--------------------------------------------------------------------------------

We generate Homebrew packages within our automated build system.  We only
generate binaries for Yosemite at the time of writing, which means that
**brew install** on El Capitan machines triggers a (very slow) build from source.

All OS X builds require you to `install the Homebrew <http://brew.sh>`_
package manager before doing anything else.  Here's how to `uninstall Homebrew
<https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/FAQ.md#how-do-i-uninstall-homebrew>`_,
if you ever want to start again from scratch.  

To install the Ethereum C++ components from Homebrew, execute these commands: ::

    brew update
    brew upgrade
    brew tap ethereum/ethereum
    brew install cpp-ethereum
    brew linkapps cpp-ethereum

Or ... ::

    brew install cpp-ethereum --with-gui

... if you want to build
`AlethZero and AlethOne <https://github.com/ethereum/alethzero>`_ and
the `Mix IDE <https://github.com/ethereum/wiki/wiki/Mix:-The-DApp-IDE>`_ too.

To start the applications, type one of these commands in a Terminal window: ::

    open /Applications/AlethZero.app
    open /Applications/AlethOne.app
    open /Applications/Mix.app
    eth

Here is the `Homebrew Formula
<https://github.com/ethereum/homebrew-ethereum/blob/master/cpp-ethereum.rb>`_
which details all the supported command-line options.
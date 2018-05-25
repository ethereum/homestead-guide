
OS X Homebrew packages
--------------------------------------------------------------------------------

We generate Homebrew packages within our automated build system for the
following OS X / Mac versions:

- `OS X Mavericks (10.9) <https://en.wikipedia.org/wiki/OS_X_Mavericks>`_
- `OS X Yosemite (10.10) <https://en.wikipedia.org/wiki/OS_X_Yosemite>`_
- `OS X El Capitan (10.11) <https://en.wikipedia.org/wiki/OS_X_El_Capitan>`_

**We only support 64-bit builds.**

If your system does not support these OS X versions then you
are out of luck.  Sorry!

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

Here is the `Homebrew Formula
<https://github.com/ethereum/homebrew-ethereum/blob/master/cpp-ethereum.rb>`_
which details all the supported command-line options.

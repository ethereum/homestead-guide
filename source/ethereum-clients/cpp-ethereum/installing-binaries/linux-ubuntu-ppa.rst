
Ubuntu PPA (Personal Package Archive)
================================================================================

We have set up PPA instances for the following Ubuntu versions:

- `Ubuntu Trusty Tahr (14.04) <https://wiki.ubuntu.com/TrustyTahr>`_
- `Ubuntu Utopic Unicorn (14.10) <https://wiki.ubuntu.com/UtopicUnicorn>`_
- `Ubuntu Vivid Vervet (15.04) <https://wiki.ubuntu.com/VividVervet>`_
- `Ubuntu Wily Werewolf (15.10) <https://wiki.ubuntu.com/WilyWerewolf>`_
- `Ubuntu Xenial Xerus (16.04) <https://wiki.ubuntu.com/XenialXerus>`_

**We only support 64-bit builds.**  It may be possible to get the
client working for Ubuntu 32-bit, by building from source and disabling
EVMJIT and maybe other features too.  We might accept pull-requests to
add such support, but we will not put any of our development time into
supporting Ubuntu 32-bit builds.

For the latest stable version: ::

    sudo add-apt-repository ppa:ethereum/ethereum
    sudo apt-get update
    sudo apt-get install cpp-ethereum

If you want to use the cutting edge developer version: ::

    sudo add-apt-repository ppa:ethereum/ethereum
    sudo add-apt-repository ppa:ethereum/ethereum-dev
    sudo apt-get update
    sudo apt-get install cpp-ethereum

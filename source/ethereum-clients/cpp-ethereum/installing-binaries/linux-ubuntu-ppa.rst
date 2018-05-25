
Ubuntu PPA (Personal Package Archive)
================================================================================

**NOTE - At the time of writing (31st August 2016), the PPAs are broken,
following significant repository reorganizations and a change of automation
process.  We have not hooked the PPA generation steps back together
yet, though this will happen in the very near future.  In the meantime,
please follow the** :ref:`Building Linux from source` **instructions**, or
install :ref:`linux-ubuntu-snap` (currently in testing).

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

    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:ethereum/ethereum
    sudo apt-get update
    sudo apt-get install cpp-ethereum

If you want to use the cutting edge developer version: ::

    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:ethereum/ethereum
    sudo add-apt-repository ppa:ethereum/ethereum-dev
    sudo apt-get update
    sudo apt-get install cpp-ethereum

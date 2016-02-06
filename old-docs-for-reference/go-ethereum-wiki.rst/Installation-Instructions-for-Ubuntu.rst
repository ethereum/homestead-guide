Installing from PPA
-------------------

For the latest development snapshot, both ``ppa:ethereum/ethereum`` and
``ppa:ethereum/ethereum-dev`` are needed. If you want the stable version
from the last PoC release, add only the first one.

.. code:: shell

    sudo apt-get install software-properties-common
    sudo add-apt-repository -y ppa:ethereum/ethereum
    sudo add-apt-repository -y ppa:ethereum/ethereum-dev
    sudo apt-get update
    sudo apt-get install ethereum

After installing, run ``geth account new`` to create an account on your
node.

You should now be able to run ``geth`` and connect to the network.

Make sure to check the different options and commands with
``geth --help``

You can alternatively install only the ``geth`` CLI with
``apt-get install geth`` if you don't want to install the other
utilities (``bootnode``, ``evm``, ``disasm``, ``rlpdump``, ``ethtest``).

Building from source
--------------------

Building Geth (command line client)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone the repository to a directory of your choosing:

.. code:: shell

    git clone https://github.com/ethereum/go-ethereum

Install latest distribution of Go (v1.4) if you don't have it already:

`See
instructions <https://github.com/ethereum/go-ethereum/wiki/Installing-Go#ubuntu-1404>`__

Building ``geth`` requires some external libraries to be installed:

.. code:: shell

    sudo apt-get install -y build-essential libgmp3-dev golang

Finally, build the ``geth`` program using the following command.

.. code:: shell

    cd go-ethereum
    make geth

You can now run ``build/bin/geth`` to start your node.

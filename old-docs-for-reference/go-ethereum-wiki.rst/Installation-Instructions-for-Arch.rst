Installing from source
----------------------

Install dependencies

.. code:: shell

    pacman -S git go gcc gmp

Download and build geth

.. code:: shell

    git clone https://github.com/ethereum/go-ethereum
    cd go-ethereum
    make geth

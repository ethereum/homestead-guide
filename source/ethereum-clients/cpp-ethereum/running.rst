################################################################################
Running
################################################################################

Running eth without any argument will synchronise your node to the public blockchain.
It is also possible to create or synchronise to another blockchain (see :ref:`custom blockchain using eth <custom-networks-eth>`).

Interacting with your node can be done using either geth or the ethereum console:

**Using geth**

.. code:: Console

   > geth attach //attach geth to a running eth node.

**Using the ethereum console**

The ethereum console is a node.js application which connect to a running eth/geth node and provide access to the web3 object.

.. note:: https://github.com/ethereum/ethereum-console

It can be installed using npm:

.. note:: | > npm install -g ethereum-console
            | > ethconsole

.. note:: | **Usage:**
        | ethconsole [javascript file] [ipc socket]
        | Connects to an ethereum node via ipc in order to control it remotely
        | through global variable web3 (web3.admin is also present).
        | If no arguments are given, connects to the default ipc socket
        | and drops into interactive mode.
        | Arguments:
        | <ipc socket path>  connect to the given ipc socket (use ipc://<path> if it does not end with .ipc)
        | <javascript file>    execute the given javascript file that has to end in .js non-interactively.
        | The script has to call process.exit() in order to terminate the console.

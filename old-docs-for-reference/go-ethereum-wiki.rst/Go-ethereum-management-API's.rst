Overview
========

Beside the official `Dapp
API <https://github.com/ethereum/wiki/wiki/JSON-RPC>`__ interface the go
Ethereum node has support for additional management API's. These API's
are offered using `JSON-RPC <http://www.jsonrpc.org/specification>`__
and follow the same conventions as used in the Dapp API. The go Ethereum
package comes with a console client which has support for all additional
API's.

How to
======

It is possible to specify the set of API's which are offered over an
interface with the ``--${interface}api`` command line argument for the
go ethereum daemon. Where ``${interface}`` can be ``rpc`` for the
``http`` interface or ``ipc`` for an unix socket on unix or named pipe
on Windows.

For example, ``geth --ipcapi "admin,eth,miner" --rpcapi "eth,web3"``
will \* enable the admin, official dapp and miner API over the IPC
interface \* enable the eth and web3 API over the RPC interface

Please note that offering an API over the ``rpc`` interface will give
everyone access to the API who can access this interface (e.g. dapp's).
So be careful which API's you enable. By default geth enables all API's
over the ``ipc`` interface and only the db,eth,net and web3 API's over
the ``rpc`` interface.

To determine which API's an interface provides the ``modules``
transaction can be used, e.g. over an ``ipc`` interface on unix systems:

::

    echo '{"jsonrpc":"2.0","method":"modules","params":[],"id":1}' | nc -U $datadir/geth.ipc

will give all enabled modules including the version number:

::

    {
       "id":1,
       "jsonrpc":"2.0",
       "result":{
          "admin":"1.0",
          "db":"1.0",
          "debug":"1.0",
          "eth":"1.0",
          "miner":"1.0",
          "net":"1.0",
          "personal":"1.0",
          "shh":"1.0",
          "txpool":"1.0",
          "web3":"1.0"
       }
    }

Integration
-----------

These additional API's follow the same conventions as the official dapp
API. Web3 can be
`extended <https://github.com/ethereum/web3.js/pull/229>`__ and used to
consume these additional API's.

The different functions are split into multiple smaller logically
grouped API's. Examples are given for the `Javascript
console <https://github.com/ethereum/go-ethereum/wiki/JavaScript-Console>`__
but can easily be converted to a rpc request.

**2 examples:**

-  Console: ``miner.start()``

-  IPC:
   ``echo '{"jsonrpc":"2.0","method":"miner_start","params":[],"id":1}' | nc -U $datadir/geth.ipc``

-  RPC:
   ``curl -X POST --data '{"jsonrpc":"2.0","method":"miner_start","params":[],"id":74}' localhost:8545``

With the number of THREADS as an arguments:

-  Console: ``miner.start(4)``

-  IPC:
   ``echo '{"jsonrpc":"2.0","method":"miner_start","params":[4],"id":1}' | nc -U $datadir/geth.ipc``

-  RPC:
   ``curl -X POST --data '{"jsonrpc":"2.0","method":"miner_start","params":[4],"id":74}' localhost:8545``

Admin
-----

Provides various functions for managing a geth node \*
`addPeer <#admin_addPeer>`__ \* [peers] (#admin\_peers) \*
`importChain <#admin_importChain>`__ \*
`exportChain <#admin_exportChain>`__ \* `verbosity <#admin_verbosity>`__
\* `setSolc <#admin_setColc>`__ \* `startRPC <#admin_startRPC>`__ \*
`stopRPC <#admin_stopRPC>`__

Db
--

This is the official Dapp API. See for more information `this
page <https://github.com/ethereum/wiki/wiki/JSON-RPC>`__.

Debug
-----

-  `dumpBlock <#debug_dumpBlock>`__
-  [getBlockRlp] (#debug\_getBlockRlp)
-  `printBlock <#debug_printBlock>`__
-  `processBlock <#debug_processBlock>`__
-  `seedHash <#debug_seedHash>`__
-  `setHead <#debug_setHead>`__

Eth
---

This is the official Dapp API. See for more information `this
page <https://github.com/ethereum/wiki/wiki/JSON-RPC>`__.

Miner
-----

Allows full control over the miner and
`DAG <https://github.com/ethereum/wiki/wiki/Ethash-DAG>`__. \*
`start <#miner_start>`__ \* `stop <#miner_stop>`__ \*
`hashrate <#miner_hashrate>`__ \* `setExtra <#miner_setExtra>`__ \*
`setGasPrice <#miner_setGasPrice>`__ \*
`startAutoDAG <#miner_startAutoDAG>`__ \*
`stopAutoDAG <#miner_stopAutoDAG>`__ \* `makeDAG <#miner_makeDAG>`__

Net
---

Network related functions \* `peerCount <#net_peerCount>`__ \*
`listening <#net_listening>`__

Personal
--------

Support for account management. \*
`listAccounts <#personal_listAccounts>`__ \*
`newAccount <#personal_newAccount>`__ \*
`unlockAccount <#personal_unlockAccount>`__

Txpool
------

Gives insight in the transaction pool \* `status <#txpool_status>`__

Web3
----

This is the official Dapp API. See for more information `this
page <https://github.com/ethereum/wiki/wiki/JSON-RPC>`__.

admin\_addPeer
~~~~~~~~~~~~~~

Add peer to node

Parameters
^^^^^^^^^^

-  ``Url``, peer enode url

Return
^^^^^^

``boolean`` indicating if the peer was added

Example
^^^^^^^

``admin.addPeer("enode://4d19a2d...167fa41@XXX.XXX.XXX.XXX:30303")``
\*\*\*

admin\_peers
~~~~~~~~~~~~

This property will show all connected peers.

Example
^^^^^^^

``admin.peers`` \*\*\*

admin\_importChain
~~~~~~~~~~~~~~~~~~

Import an exported chain from file into node. This only works if no
chain already exists: it does not delete any existing data.

Parameters
^^^^^^^^^^

-  ``Filename``, the fully qualified path to the file containing the
   chain to be imported

Return
^^^^^^

``boolean`` indicating if chain was imported

Example
^^^^^^^

``admin.importChain("/tmp/chain.txt")`` \*\*\*

admin\_exportChain
~~~~~~~~~~~~~~~~~~

Export the blockchain to a file

Parameters
^^^^^^^^^^

-  ``Filename``, the fully qualified path to the file where the
   blockchain must be exported

Return
^^^^^^

``boolean`` indicating if chain was exported

Example
^^^^^^^

``admin.exportChain("/tmp/chain.txt")`` \*\*\*

admin\_verbosity
~~~~~~~~~~~~~~~~

Set loglevel

Parameters
^^^^^^^^^^

-  ``Level``, the verbosity level with 0 the least and 6 the most
   verbose

Return
^^^^^^

``boolean`` indicating if chain was exported

Example
^^^^^^^

``admin.verbosity(5)`` \*\*\*

admin\_setSolc
~~~~~~~~~~~~~~

Set the path to the solidity compiler for ``eth.compileSolidity``.

Parameters
^^^^^^^^^^

-  ``Path``, full path to solidity compiler

Return
^^^^^^

``string`` in case the path was valid a brief description about the
solidity compiler

Example
^^^^^^^

``admin.setSolc("/tmp/solc")`` \*\*\*

admin\_startRPC
~~~~~~~~~~~~~~~

Start the HTTP RPC interface

Parameters
^^^^^^^^^^

-  ``ListenAddress``, open listener on this host
-  ``ListenPort``, open listener on this port
-  ``CorsDomain``, the cross origin resource shared header
-  ``Apis``, comma separated list with the API modules which are offered
   over this interface

Return
^^^^^^

``boolean`` indication if the interface was started

Example
^^^^^^^

``admin.startRPC("127.0.0.1", 8545, "*", "eth,net,web3")`` \*\*\*

admin\_stopRPC
~~~~~~~~~~~~~~

Stop the HTTP RPC interface

Return
^^^^^^

``boolean`` indication if the interface was stopped

Example
^^^^^^^

``admin.stopRPC()``

--------------

debug\_dumpBlock
~~~~~~~~~~~~~~~~

Dump block

Parameters
^^^^^^^^^^

``integer``, block number

Return
^^^^^^

``string`` dumped block

Example
^^^^^^^

``debug.dumpBlock(0)`` \*\*\*

debug\_getBlockRlp
~~~~~~~~~~~~~~~~~~

Get RLP encoded block

Parameters
^^^^^^^^^^

``integer``, block number

Return
^^^^^^

``string`` RLP encoded block

Example
^^^^^^^

``debug.getBlockRlp(0)`` \*\*\*

debug\_printBlock
~~~~~~~~~~~~~~~~~

Pretty print block

Parameters
^^^^^^^^^^

``integer``, block number

Return
^^^^^^

``string`` formatted block

Example
^^^^^^^

``debug.printBlock(0)`` \*\*\*

debug\_processBlock
~~~~~~~~~~~~~~~~~~~

Reprocess a block

Parameters
^^^^^^^^^^

``integer``, block number

Return
^^^^^^

``boolean`` indication if the block was successful processed

Example
^^^^^^^

``debug.processBlock(0)``

--------------

debug\_seedHash
~~~~~~~~~~~~~~~

Block seed hash

Parameters
^^^^^^^^^^

``NONE``

Return
^^^^^^

``string`` block seed hash

Example
^^^^^^^

``debug.seedHash(eth.blockNumber)``

--------------

debug\_setHead
~~~~~~~~~~~~~~

Rewind the chain to a specific block

Parameters
^^^^^^^^^^

``integer``, block number

Return
^^^^^^

``boolean`` indication if the new head was successful set

Example
^^^^^^^

``debug.setHead(eth.blockNumber-5000)``

--------------

miner\_start
~~~~~~~~~~~~

This will generates the DAG if necessary and starts the miner

Parameters
^^^^^^^^^^

``integer``, an optional integer which specifies the number of threads,
if not specified the number of CPU's is used

Return
^^^^^^

``boolean`` indicating if the miner was started

Example
^^^^^^^

``miner.start()`` \*\*\*

miner\_stop
~~~~~~~~~~~

This will stop the miner

Parameters
^^^^^^^^^^

none

Return
^^^^^^

``boolean`` indicating if the miner was stopped

Example
^^^^^^^

``miner.stop()``

--------------

miner\_hashrate
~~~~~~~~~~~~~~~

Miner hashrate

Parameters
^^^^^^^^^^

none

Return
^^^^^^

``integer`` hashes p/s

Example
^^^^^^^

``miner.hashrate``

--------------

miner\_setExtra
~~~~~~~~~~~~~~~

Store additional data in a mined block

Parameters
^^^^^^^^^^

``string`` string with extra data (max 1024 bytes)

Return
^^^^^^

``boolean`` indication if the DATA was set

--------------

miner\_setGasPrice
~~~~~~~~~~~~~~~~~~

Set the gas price.

Parameters
^^^^^^^^^^

``string`` gas price, this can be a base8 (start with 0b), base10 (no
prefix) or base16 representation (start with 0x)

Return
^^^^^^

``boolean`` indication if the new price was set

--------------

miner\_startAutoDAG
~~~~~~~~~~~~~~~~~~~

Pregenerate the DAG, this will allow for a seamless transition between
the different epochs. If not enabled the miner will need to generate the
DAG when a new epoch begins (each 30k blocks). This takes some time and
will stop the miner until the DAG is generated.

Parameters
^^^^^^^^^^

none

Return
^^^^^^

``boolean`` indication if the command was successful

--------------

miner\_stopAutoDAG
~~~~~~~~~~~~~~~~~~

Stop DAG pregeneration.

Parameters
^^^^^^^^^^

none

Return
^^^^^^

``boolean`` indication if the command was successful

--------------

miner\_makeDAG
~~~~~~~~~~~~~~

Start the DAG creator process.

Parameters
^^^^^^^^^^

none

Return
^^^^^^

``boolean`` indication if the command was successful

--------------

net\_peerCount
~~~~~~~~~~~~~~

The number of connected peers

Parameters
^^^^^^^^^^

none

Return
^^^^^^

``integer`` number of peers

Example
^^^^^^^

``net.peerCount``

--------------

net\_listening
~~~~~~~~~~~~~~

Indication if this node is currently listening for new peers

Parameters
^^^^^^^^^^

none

Return
^^^^^^

``boolean`` indication if this node accepts new peers

Example
^^^^^^^

``net.listening``

--------------

personal\_listAccounts
~~~~~~~~~~~~~~~~~~~~~~

List all accounts

Parameters
^^^^^^^^^^

none

Return
^^^^^^

``array`` collection with accounts

Example
^^^^^^^

``personal.listAccounts``

--------------

personal\_newAccount
~~~~~~~~~~~~~~~~~~~~

Create a new account

Parameters
^^^^^^^^^^

``string``, passphrase to protect the account

Return
^^^^^^

``string`` address of the new account

Example
^^^^^^^

``personal.newAccount("mypasswd")``

--------------

personal\_unlockAccount
~~~~~~~~~~~~~~~~~~~~~~~

Unlock an account

Parameters
^^^^^^^^^^

``string``, address of the account to delete

``string``, passphrase of the account to delete (optional in console,
user will be prompted)

``integer``, unlock account for duration seconds (optional)

Return
^^^^^^

``boolean`` indication if the account was unlocked

Example
^^^^^^^

``personal.unlockAccount(eth.coinbase, "mypasswd", 300)``

--------------

txpool\_status
~~~~~~~~~~~~~~

Number of pending/queued transactions

Parameters
^^^^^^^^^^

``NONE``

Return
^^^^^^

``pending`` all processable transactions

``queued`` all non-processable transactions

Example
^^^^^^^

``txpool.status``

--------------

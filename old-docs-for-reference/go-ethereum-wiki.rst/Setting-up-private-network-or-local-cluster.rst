This page describes how to set up a local cluster of nodes, advise how
to make it private, and how to hook up your nodes on the eth-netstat
network monitoring app. A fully controlled Ethereum network is useful as
a backend for network integration testing (core developers working on
issues related to networking/blockchain synching/message propagation,
etc or dapp developers testing multi-block and multi-user scenarios).

We assume you are able to build ``geth`` following the `build
instructions <https://github.com/ethereum/go-ethereum/wiki/Building-Ethereum>`__

Setting up multiple nodes
-------------------------

In order to run multiple Ethereum nodes locally, you have to make sure:
- each instance has a separate data directory (``--datadir``) - each
instance runs on a different port (both eth and rpc)
(``--port and --rpcport``) - in case of a cluster the instances must
know about each other - the ipc endpoint is unique or the ipc interface
is disabled (``--ipcpath or --ipcdisable``)

You start the first node (let's make port explicit and disable ipc
interface)

.. code:: bash

    geth --datadir="/tmp/eth/60/01" -verbosity 6 --ipcdisable --port 30301 --rpcport 8101 console 2>> /tmp/eth/60/01.log

We started the node with the console, so that we can grab the enode url
for instance:

::

    > admin.nodeInfo.NodeUrl
    enode://8c544b4a07da02a9ee024def6f3ba24b2747272b64e16ec5dd6b17b55992f8980b77938155169d9d33807e501729ecb42f5c0a61018898c32799ced152e9f0d7@9[::]:30301

``[::]`` will be parsed as localhost (``127.0.0.1``). If your nodes are
on a local network check each individual host machine and find your ip
with ``ifconfig`` (on Linux and MacOS):

.. code:: bash

    $ ifconfig|grep netmask|awk '{print $2}'
    127.0.0.1
    192.168.1.97

If your peers are not on the local network, you need to know your
external IP address (use a service) to construct the enode url.

Now you can launch a second node with:

.. code:: bash

    geth --datadir="/tmp/eth/60/02" --verbosity 6 --ipcdisable --port 30302 --rpcport 8102 console 2>> /tmp/eth/60/02.log

If you want to connect this instance to the previously started node you
can add it as a peer from the console with
``admin.addPeer(enodeUrlOfFirstInstance)``.

You can test the connection by typing in geth console:

.. code:: javascript

    > net.listening
    true
    > net.peerCount
    1
    > admin.peers
    ...

Local cluster
-------------

As an extention of the above, you can spawn a local cluster of nodes
easily. It can also be scripted including account creation which is
needed for mining. See
```gethcluster.sh`` <https://github.com/ethersphere/eth-utils>`__
script, and the README there for usage and examples.

Private network
---------------

An Ethereum network is a private network if the nodes are not connected
to the main network nodes. In this context private only means reserved
or isolated, rather than protected or secure. Since connections between
nodes are valid only if peers have identical protocol version and
network id, you can effectively isolate your network by setting either
of these to a non default value. We recommend using the semantic
``networkid`` command line option for this. Its argument is an integer,
the main network has id 1 (the default). So if you supply your own
custom network id which is different than the main network your nodes
will not connect to other nodes and form a private network.

Monitoring your nodes
---------------------

`This page <https://github.com/ethereum/wiki/wiki/Network-Status>`__
describes how to use the `The Ethereum (centralised) network status
monitor (known sometimes as "eth-netstats") <http://stats.ethdev.com>`__
to monitor your nodes.

`This
page <https://github.com/ethereum/go-ethereum/wiki/Setting-up-monitoring-on-local-cluster>`__
or `this README <https://github.com/ethersphere/eth-utils>`__ describes
how you set up your own monitoring service for a (private or public)
local cluster.

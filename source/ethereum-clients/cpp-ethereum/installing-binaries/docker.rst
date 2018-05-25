Docker
======

We are hosting latest development snapshots (and in the future also
releases) at docker hub. You can run these images as follows:

Preparation
-----------
Before running the image, you should pull the latest version and prepare
the data directories::

    # get the lastest version from dockerhub (redo for updates).
    docker pull ethereum/client-cpp
    # create mountable datadirs; blockchain/account data will be stored there
    mkdir -p ~/.ethereum ~/.web3

These steps need to be done only once. For upgrading to a new version do
the ``docker pull ...`` again.

Execution
---------
The simplest version is to run::

    docker run --rm -it \
        -p 127.0.0.1:8545:8545 \
        -p 0.0.0.0:30303:30303 \
        -v ~/.ethereum:/.ethereum \
        -v ~/.web3:/.web3 \
        -e HOME=/ \
        --user $(id -u):$(id -g) \
        ethereum/client-cpp

This will write data to ``~/.ethereum`` and ``~/.web3/`` on your host and run
the client with your user's permissions.  For most cases this should be
sufficient and the client should behave exactly as if run from a local build.

If you want the rpc port reachable from the network (not recommended, never do this
if you have valuable data or private keys on your machine), replace
``-p 127.0.0.1:8545:8545`` with ``-p 0.0.0.0:8545:8545``.

For convenience, you can create the file ``/usr/local/bin/docker-eth`` with the
following content::

    #!/usr/bin/env sh
    mkdir -p ~/.ethereum ~/.web3
    if ! id -nG $(whoami)|grep -qw "docker"; then SUDO='sudo'; else SUDO=''; fi
    $SUDO docker run --rm -it \
        -p 127.0.0.1:8545:8545 \
        -p 0.0.0.0:30303:30303 \
        -v ~/.ethereum:/.ethereum \
        -v ~/.web3:/.web3 \
        -e HOME=/ \
        --user $(id -u):$(id -g) \
        ethereum/client-cpp $@

And make it executable with ``chmod +x /usr/local/bin/docker-eth``. Now you can
start the client with::

    docker-eth

**Note:** The ``docker-eth`` command will accept the same flags as the raw ``eth``
command.

If you want to attach to the node, you can either just use mist (it will
detect the node automatically), use ``geth attach ipc:/$HOME/.ethereum/geth.ipc``
or ethereum-console as described in :ref:`Running cpp-ethereum`.

Advanced usage:
---------------

Due to https://github.com/docker/libnetwork/issues/552 multicast is not working
yet without ``--net=host``. You can still run the client with network isolation
and use ``-p 127.0.0.1:8545:8545 -p 30303:30303 -p 30303:30303/udp`` for
publishing the rpc, discovery and p2p ports. If you want to be discoverable
from the outside, you will need to

- add your public ip address with the ``--public-ip`` flag,
- create a port forwarding with your NAT

(syncing will still work without it).

Running in Docker
=================

We keep a Docker image with recent snapshot builds from the ``develop``
branch `on
DockerHub <https://registry.hub.docker.com/u/ethereum/client-go>`__. Run
this first:

.. code:: shell

    docker pull ethereum/client-go

Start a node with:

.. code:: shell

    docker run -it -p 30303:30303 ethereum/client-go

To start a node that runs the JSON-RPC interface on port **8545**, run:

.. code:: shell

    docker run -it -p 8545:8545 -p 30303:30303 ethereum/client-go --rpc --rpcaddr "0.0.0.0"

**WARNING: This opens your container to external calls. "0.0.0.0" should
*not* be used when exposed to public networks**

To use the interactive JavaScript console, run:

.. code:: shell

    docker run -it -p 30303:30303 ethereum/client-go console

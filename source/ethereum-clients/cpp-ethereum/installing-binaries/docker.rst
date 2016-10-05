
Docker
======

We are hosting latest development snapshots (and in the future also
releases) at docker hub. You can run these images as follows:

    docker pull ethereum/cpp-client
    sudo docker run -v ~/.ethereum:/root/.ethereum -v ~/.web3:/root/.web3/ ethereum/client-cpp

This will make your local directories ``~/.ethereum`` and ``~/.web3/``
available to the docker instance, so please be careful about the data
stored there.

If you want to attach to the node, you can either just use mist (it will
detect the node automatically), use ``geth attach`` or ethereum-console
as described in :ref:`Running cpp-ethereum`.

**Note:** The docker image system is not really nice to use yet,
but it works. Issues we want to address in the future:

 - the permissions are not nice yet - you have to run it as root
 - the image is quite large because it contains the full source and
   intermediate build results

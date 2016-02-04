Windows
~~~~~~~

Download and run the installer found at http://golang.org/doc/install

OS X
~~~~

Download an install the darwin binary from https://golang.org/dl/

Linux
~~~~~

Ubuntu 14.04
^^^^^^^^^^^^

The apt-get repositories for 14.04 contain golang 1.2.1. Version 1.4.2
is required, so you can download directly (as above). Alternatively, you
can `add the ethereum apt
repository <https://github.com/ethereum/go-ethereum/wiki/Installation-Instructions-for-Ubuntu#installing-from-ppa>`__,
which hosts golang 1.4.2. Then you can use
``sudo apt-get install golang`` to install. You will still have to set
the $GOPATH and $PATH variables as specified below.

If you are getting 'error 2' when building Geth or 'expected target'
errors, it's because you compiled geth while using Go 1.3.x. Run 'make
clean' in the go-ethereum folder then run 'make geth' again to solve the
issue.

Other distros
^^^^^^^^^^^^^

Download the latest distribution

``curl -O https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz``

Unpack it to the ``/usr/local`` (might require sudo)

``tar -C /usr/local -xzf go1.4.2.linux-amd64.tar.gz``

Set GOPATH and PATH
^^^^^^^^^^^^^^^^^^^

For Go to work properly, you need to set the following two environment
variables:

-  Setup a go folder
   ``mkdir -p ~/go; echo "export GOPATH=$HOME/go" >> ~/.bashrc``
-  Update your path
   ``echo "export PATH=$PATH:$HOME/go/bin:/usr/local/go/bin" >> ~/.bashrc``
-  Read the environment variables into current session:
   ``source ~/.bashrc``

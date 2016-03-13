We assume you have a GOPATH set up appropriately. If not, you can read
about setting it up here: http://golang.org/doc/code.html#GOPATH.

In order to 'build edge', we need to switch 3 repos to their 'develop'
branch

-  Begin by getting the newest version of the go client source and their
   dependencies:

   ::

       go get -u -d github.com/obscuren/serpent-go
       go get -u -d github.com/ethereum/go-ethereum/ethereum
       go get -u -d github.com/ethereum/go-ethereum/mist

-  Init the serpent submodule

   ::

       cd $GOPATH/src/github.com/obscuren/serpent-go
       git submodule init
       git submodule update

-  Switch to the ``develop`` branch the necessary repos:

   ::

       cd $GOPATH/src/github.com/ethereum/go-ethereum
       git checkout develop

       cd $GOPATH/src/github.com/ethereum/eth-go
       git checkout develop

       cd $GOPATH/src/github.com/obscuren/mutan
       git checkout develop

-  Go forth and build away:

   ::

       cd $GOPATH/src/github.com/ethereum/go-ethereum/ethereum
       go install -v

       cd $GOPATH/src/github.com/ethereum/go-ethereum/mist
       go install -v

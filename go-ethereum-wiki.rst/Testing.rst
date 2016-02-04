Running tests on go-ethereum
============================

This page assumes go-ethereum has been configured according to the
`Developers
Guide <https://github.com/ethereum/go-ethereum/wiki/Developers'-Guide>`__.
All commands (unless stated otherwise) are assumed to be run from
``$GOPATH/src/github.com/ethereum/go-ethereum``

Unit tests
----------

See `Travis <https://travis-ci.org/ethereum/go-ethereum/builds>`__ or
`Coveralls <https://coveralls.io/r/ethereum/go-ethereum>`__ for status.

Test the full codebase locally by changing to the repository directory
and running

::

    test ./...

Integration tests
-----------------

Integration tests for Go are included in the ``tests`` directory and can
be run with standard go testing (i.e. ``go test``). To run all the
integration tests simply run:

::

    go test ./tests/

Ethtest
~~~~~~~

Alternatively, there is a CLI application, ``ethtest`` who can be used
to run these tests without Go. The binary can be built from
``./cmd/ethtest`` and then run from anywhere (such as the root directory
of the test files). Some examples:

Run all tests from current directory, looking in their respective sub
directories for json files: ``ethtest``

Run all VM json tests from ./VMTests/ directory
``ethtest --test "vm" --file "./VMTests/"``

Run all tests in a cousin directory supplied by environment variable
``ETHEREUM_TEST_PATH="../../tests/files" ethtest --test "all"``

Run a single transaction test
``ethtest --test "tx" --file "./TransactionTests/ttTransactionTest.json"``

Flags:

::

       --test "all"     Test type (string): VMTests, TransactionTests, StateTests, BlockTests
       --file "."       Test file or directory. Directories are searched for .json files 1 level deep [$ETHEREUM_TEST_PATH]
       --continue       Continue running tests on error (true) or exit immediately (false)

VM
^^

`VM Test wiki <https://github.com/ethereum/tests/wiki/VM-Tests>`__

::

    go test ./tests/vm_test.go

State
^^^^^

`State Test wiki <https://github.com/ethereum/tests/wiki/State-tests>`__

::

    go test ./tests/state_test.go

Transaction
^^^^^^^^^^^

`Transaction Test
wiki <https://github.com/ethereum/tests/wiki/Transaction-Tests>`__

::

    go test ./tests/transaction_test.go

Blockchain
^^^^^^^^^^

`Blockchain Test
wiki <https://github.com/ethereum/tests/wiki/Blockchain-Tests-II>`__

::

    go test ./tests/block_test.go

RPC
~~~

`RPC Tests repo <https://github.com/ethereum/rpc-tests>`__

1. Load test JSON with

   ::

       geth blocktest <pathToTheTestRepo>/BlockTests/bcRPC_API_Test.json RPC_API_Test rpc

2. Run rpc-tests (https://github.com/ethereum/rpc-tests#usage)

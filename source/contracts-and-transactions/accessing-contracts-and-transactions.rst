********************************************************************************
Accessing Contracts and Transactions
********************************************************************************

RPC
================================================================================

In previous sections we have seen how contracts can be written, deployed and interacted with. Now it's time to dive in the details of communicating
with the Ethereum network and smart contracts.

An Ethereum node offers a `RPC <https://wikipedia.org/wiki/Remote_procedure_call>`_ interface. This interface gives Ðapp's access to the Ethereum
blockchain and functionality that the node provides, such as compiling smart contract code. It uses a subset of the
`JSON-RPC 2.0 <http://www.jsonrpc.org/specification>`_ specification (no support for notifications or named parameters) as serialisation protocol and
is available over HTTP and IPC (unix domain sockets on linux/OSX and named pipe's on Windows).

If you are not interested in the details but are looking for an easy to use javascript library you can skip the following sections and continue with :ref:`Using Web3 <using_web3.js>`.

Conventions
================================================================================
The RPC interface uses a couple of conventions that are not part of the JSON-RPC 2.0 specification:

* Numbers are hex encoded. This decision was made because some languages have no or limited support for working with extremly large numbers. To prevent
  these type of errors numbers are hex encoded and it is up to the deverloper to parse these numbers and handle them appropriately. See the
  `hex encoding section <https://github.com/ethereum/wiki/wiki/JSON-RPC#output-hex-values>`_ on the wiki for examples.
* Default block number, several RPC methods accept a block number. In some cases it's not possible to give a block number or not very convenient. For
  these cases the default block number can be one of these strings ["earliest", "latest", "pending"]. See the
  `wiki page <https://github.com/ethereum/wiki/wiki/JSON-RPC#the-default-block-parameter>`_ for a list of RPC methods that use the default block parameters.


Deploy contract
================================================================================
We will go through the different steps to deploy the following contract using only the RPC interface.

.. code:: js

   contract Multiply7 {
      event Print(uint);
      function multiply(uint input) returns (uint) {
         Print(input * 7);
         return input * 7;
      }
   }

The first thing to do is make sure the HTTP RPC interface is enabled. This means for geth we supply the ``--rpc`` flag on startup and for eth the ``-j``
flag. In this example we use the geth node on a private development chain. Using this approach we don't need ether on the real network.

.. code:: bash

    > geth --rpc --dev --mine --minerthreads 1 --unlock 0 console 2>>geth.log

This will start the HTTP RPC interface on ``http://localhost:8545``.

.. note:: geth supports `CORS <https://en.wikipedia.org/wiki/Cross-origin_resource_sharing>`_, see the ``--rpccorsdomain`` flag for more information.

We can verify that the interface is running by retrieving the coinbase address and balance using `curl <https://curl.haxx.se/download.html>`_. Please
note that data in these examples will differ on your local node. If you want to try these command replace the request params accordingly.

.. code:: bash

    > curl --data '{"jsonrpc":"2.0","method":"eth_coinbase", "id":1}' localhost:8545
    {"id":1,"jsonrpc":"2.0","result":["0xeb85a5557e5bdc18ee1934a89d8bb402398ee26a"]}

    > curl --data '{"jsonrpc":"2.0","method":"eth_getBalance", "params": ["0xeb85a5557e5bdc18ee1934a89d8bb402398ee26a"], "id":2}' localhost:8545
    {"id":2,"jsonrpc":"2.0","result":"0x1639e49bba16280000"}

Remember when we said that numbers are hex encoded? In this case the balance is returned in Wei as a hex string. If we want to have the balance in
Ether as a number we can use web3 from the geth console.

.. code:: js

    > web3.fromWei("0x1639e49bba16280000", "ether")
    "410"

Now that we have some ether on our private development chain we can deploy the contract. The first step is to verify that the solidity compiler is
available. We can retrieve available compilers using the ``eth_getCompilers`` RPC method.

.. code:: bash

   > curl --data '{"jsonrpc":"2.0","method": "eth_getCompilers", "id": 3}' localhost:8545
   {"id":3,"jsonrpc":"2.0","result":["Solidity"]}

We can see that the solidity compiler is available. If it's not available follow `these <http://solidity.readthedocs.org/en/latest/installing-solidity.html>`_
instructions.

The next step is to compile the Multiply7 contract to byte code that can be send to the EVM.

.. code:: bash

   > curl --data '{"jsonrpc":"2.0","method": "eth_compileSolidity", "params": ["contract Multiply7 { event Print(uint); function multiply(uint input) returns (uint) { Print(input * 7); return input * 7; } }"], "id": 4}' localhost:8545
   {"id":4,"jsonrpc":"2.0","result":{"Multiply7":{"code":"0x6060604052605f8060106000396000f3606060405260e060020a6000350463c6888fa18114601a575b005b60586004356007810260609081526000907f24abdb5865df5079dcc5ac590ff6f01d5c16edbc5fab4e195d9febd1114503da90602090a15060070290565b5060206060f3","info":{"source":"contract Multiply7 { event Print(uint); function multiply(uint input) returns (uint) { Print(input * 7); return input * 7; } }","language":"Solidity","languageVersion":"0.2.2","compilerVersion":"0.2.2","compilerOptions":"--bin --abi --userdoc --devdoc --add-std --optimize -o /tmp/solc205309041","abiDefinition":[{"constant":false,"inputs":[{"name":"input","type":"uint256"}],"name":"multiply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"","type":"uint256"}],"name":"Print","type":"event"}],"userDoc":{"methods":{}},"developerDoc":{"methods":{}}}}}}

Now that we have the compiled code we need to determine how much gas it costs to deploy it. The RPC interface has an ``eth_estimateGas`` method that will
give us an estimate.

.. code:: bash

   > curl --data '{"jsonrpc":"2.0","method": "eth_estimateGas", "params": [{"from": "0xeb85a5557e5bdc18ee1934a89d8bb402398ee26a", "data": "0x6060604052605f8060106000396000f3606060405260e060020a6000350463c6888fa18114601a575b005b60586004356007810260609081526000907f24abdb5865df5079dcc5ac590ff6f01d5c16edbc5fab4e195d9febd1114503da90602090a15060070290565b5060206060f3"}], "id": 5}' localhost:8545
   {"id":5,"jsonrpc":"2.0","result":"0xb8a9"}

And finally deploy the contract.

.. code:: bash

   > curl --data '{"jsonrpc":"2.0","method": "eth_sendTransaction", "params": [{"from": "0xeb85a5557e5bdc18ee1934a89d8bb402398ee26a", "gas": "0xb8a9", "data": "0x6060604052605f8060106000396000f3606060405260e060020a6000350463c6888fa18114601a575b005b60586004356007810260609081526000907f24abdb5865df5079dcc5ac590ff6f01d5c16edbc5fab4e195d9febd1114503da90602090a15060070290565b5060206060f3"}], "id": 6}' localhost:8545
   {"id":6,"jsonrpc":"2.0","result":"0x3a90b5face52c4c5f30d507ccf51b0209ca628c6824d0532bcd6283df7c08a7c"}

The transaction is accepted by the node and a transaction hash is returned. We can use this hash to track the transaction.

The next step is to determine the address where our contract is deployed. Each executed transaction will create a receipt. This receipt contains
various information about the transaction such as in which block the transaction was included and how much gas was used by the EVM. If a transaction
creates a contract it will also contain the contract address. We can retrieve the receipt with the ``eth_getTransactionReceipt`` RPC method.

.. code:: bash

   > curl --data '{"jsonrpc":"2.0","method": "eth_getTransactionReceipt", "params": ["0x3a90b5face52c4c5f30d507ccf51b0209ca628c6824d0532bcd6283df7c08a7c"], "id": 7}' localhost:8545
   {"id":7,"jsonrpc":"2.0","result":{"transactionHash":"0x3a90b5face52c4c5f30d507ccf51b0209ca628c6824d0532bcd6283df7c08a7c","transactionIndex":"0x0","blockNumber":"0x4c","blockHash":"0xe286656e478a1b99030e318d0f5c3a61a644f25e63deaa8be52e80da1e7b0c47","cumulativeGasUsed":"0xb8a9","gasUsed":"0xb8a9","contractAddress":"0x6ff93b4b46b41c0c3c9baee01c255d3b4675963d","logs":[]}}

We can see that our contract was created on ``0x6ff93b4b46b41c0c3c9baee01c255d3b4675963d``. If you got null instead of a receipt the transaction has
not been included in a block yet. Wait for a moment and check if your miner is running and retry it.


Interacting with smart contracts
================================================================================
Now that our contract is deployed we can interact with it. There are 2 methods for this, sending a transaction or :ref:`using call as previously explained <interacting_with_a_contract>`. In this example we will be sending a transaction to the multiply method of the contract.

If we look at the documentation for the `eth_sendTransaction <https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_sendtransaction>`_ we can see that we need to supply
several arguments. In our case we need to specify the ``from``, ``to`` and ``data`` arguments. ``From`` is the public address of our account and ``to``
the contract address. The ``data`` argument is a bit harder. It contains a payload that defines which method must be called and with which arguments.
This is were the ABI comes into play. The ABI defines how to define and encode data for the EVM. You can read 
`all the details about the ABI here <https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI>`_.

The bytes of the payload is the function selector and defines which method is called. This is done by taking the first 4 bytes from the Keccak hash
over the function name and its argument types and hex encode it. The `multiply` function accepts an `uint` which is an
`alias <http://solidity.readthedocs.org/en/latest/types.html#integers>`_ for `uint256`. This leaves us with:

.. code:: js

   > web3.sha3("multiply(uint256)").substring(0, 8)
   "c6888fa1"

See for details `this page <https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI#function-selector>`_.

The next step is to encode the arguments. We only have one uint256, lets assume we supply the value 6. The ABI has a
`section <https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI#argument-encoding>`_ which specifies how to encode uint256 types.

   `int<M>: enc(X) is the big-endian two's complement encoding of X, padded on the higher-oder (left) side with 0xff for negative X and with zero bytes
   for positive X such that the length is a multiple of 32 bytes.`

This encodes to ``0000000000000000000000000000000000000000000000000000000000000006``.

Combining the function selector and the encoded argument our ``data`` will be ``0xc6888fa10000000000000000000000000000000000000000000000000000000000000006``.

Lets try it:

.. code:: bash

   > curl --data '{"jsonrpc":"2.0","method": "eth_sendTransaction", "params": [{"from": "0xeb85a5557e5bdc18ee1934a89d8bb402398ee26a", "to": "0x6ff93b4b46b41c0c3c9baee01c255d3b4675963d", "data": "0xc6888fa10000000000000000000000000000000000000000000000000000000000000006"}], "id": 8}' localhost:8545
   {"id":8,"jsonrpc":"2.0","result":"0x759cf065cbc22e9d779748dc53763854e5376eea07409e590c990eafc0869d74"}

Since we sent a transaction we got the transaction hash returned. If we retrieve the receipt we can see something new:

.. code-block:: js
   :emphasize-lines: 7

   {
      blockHash: "0xbf0a347307b8c63dd8c1d3d7cbdc0b463e6e7c9bf0a35be40393588242f01d55",
      blockNumber: 268,
      contractAddress: null,
      cumulativeGasUsed: 22631,
      gasUsed: 22631,
      logs: [{
         address: "0x6ff93b4b46b41c0c3c9baee01c255d3b4675963d",
         blockHash: "0xbf0a347307b8c63dd8c1d3d7cbdc0b463e6e7c9bf0a35be40393588242f01d55",
         blockNumber: 268,
         data: "0x000000000000000000000000000000000000000000000000000000000000002a",
         logIndex: 0,
         topics: ["0x24abdb5865df5079dcc5ac590ff6f01d5c16edbc5fab4e195d9febd1114503da"],
         transactionHash: "0x759cf065cbc22e9d779748dc53763854e5376eea07409e590c990eafc0869d74",
         transactionIndex: 0
     }],
     transactionHash: "0x759cf065cbc22e9d779748dc53763854e5376eea07409e590c990eafc0869d74",
     transactionIndex: 0
   }

The receipt contains a log. This log was generated by the EVM on transaction execution and included in the receipt. If we look at the multipy function
we can see that the Print event was raised with the input times 7. Since the argument for the Print event was a uint256 we can decode it according to
the ABI rules which will leave us with the expected decimal 42. Apart from the data it is worth noting that topics can be used to determine which
event created the log:

.. code:: js

   > web3.sha3("Print(uint256)")
   "24abdb5865df5079dcc5ac590ff6f01d5c16edbc5fab4e195d9febd1114503da"

You can read more about events, topics and indexing in the `Solidity tutorial <http://solidity.readthedocs.org/en/latest/contracts.html#events>`_.

This was just a brief introduction into some of the most common tasks. See for a full list of available RPC methods the
`RPC wiki page <https://github.com/ethereum/wiki/wiki/JSON-RPC#json-rpc-methods>`_.

.. _using_web3.js:

Web3.js
================================================================================
As we have seen in the previous example using the JSON-RPC interface can be quite tedious and error-prone, especially when we have to deal with the
ABI. Web3.js is a javascript library that works on top of the Ethereum RPC interface. Its goal is to provide a more user friendly interface and
reducing the chance for errors.

Deploying the Multiply7 contract using web3 would look like:

.. code:: js

   var source = 'contract Multiply7 { event Print(uint); function multiply(uint input) returns (uint) { Print(input * 7); return input * 7; } }';
   var compiled = web3.eth.compile.solidity(source);
   var code = compiled.Multiply7.code;
   var abi = compiled.Multiply7.info.abiDefinition;

   web3.eth.contract(abi).new({from: "0xeb85a5557e5bdc18ee1934a89d8bb402398ee26a", data: code}, function (err, contract) {
      if (!err && contract.address)
         console.log("deployed on:", contract.address);
      }
   );

   deployed on: 0x0ab60714033847ad7f0677cc7514db48313976e2

Load a deployed contract and send a transaction:

.. code:: js

   var source = 'contract Multiply7 { event Print(uint); function multiply(uint input) returns (uint) { Print(input * 7); return input * 7; } }';
   var compiled = web3.eth.compile.solidity(source);
   var Multiply7 = web3.eth.contract(compiled.Multiply7.info.abiDefinition);
   var multi = Multiply7.at("0x0ab60714033847ad7f0677cc7514db48313976e2")
   multi.multiply.sendTransaction(6, {from: "0xeb85a5557e5bdc18ee1934a89d8bb402398ee26a"})

Register a callback which is called when the ``Print`` event created a log.

.. code:: js

   multi.Print(function(err, data) { console.log(JSON.stringify(data)) })
   {"address":"0x0ab60714033847ad7f0677cc7514db48313976e2","args": {"":"21"},"blockHash":"0x259c7dc07c99eed9dd884dcaf3e00a81b2a1c83df2d9855ce14c464b59f0c8b3","blockNumber":539,"event":"Print","logIndex":0, "transactionHash":"0x5c115aaa5418118457e96d3c44a3b66fe9f2bead630d79455d0ecd832dc88d48","transactionIndex":0}

See for more information the `web3.js <https://github.com/ethereum/wiki/wiki/JavaScript-API>`_ wiki page.

Console
================================================================================

The geth `console <https://github.com/ethereum/go-ethereum/wiki/JavaScript-Console>`_ offers a command line interface with a javascript runtime. It
can connect to a local or remote geth or eth node. It will load the web3.js library that users can use. This allows users to deploy and interact with
smart contract from the console using web3.js. In fact the examples in the :ref:`Web3.js <using_web3.js>` section can by copied into the console.


Viewing Contracts and Transactions
================================================================================

There are several online blockchain explorers available that will allow you to inspect the Ethereum blockchain.
See for a list: :ref:`Blockchain explorers <blockchain_explorers>`.


.. _blockchain_explorers:

Hosted blockchain explorers
--------------------------------------------------------------------------------

-  `EtherChain <https://www.etherchain.org/>`_
-  `EtherCamp <https://live.ether.camp/>`_
-  `EtherScan <http://etherscan.io/>`_ (and for `Testnet <http://testnet.etherscan.io>`_)

Other Resources
--------------------------------------------------------------------------------

* `EtherNodes <http://ethernodes.org/>`_ - Geographic distribution of nodes and split by client
* `EtherListen <http://www.etherlisten.com>`_ - Realtime Ethereum transaction visualizer and audializer


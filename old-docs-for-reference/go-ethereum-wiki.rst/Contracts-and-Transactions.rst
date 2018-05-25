Account types and transactions
==============================

There are two types of accounts in Ethereum state: \* Normal or
externally controlled accounts and \* contracts, i.e., snippets of code,
think a class.

Both types of accounts have an ether balance.

Transactions can be fired from both types of accounts, though contracts
only fire transactions in response to other transactions that they have
received. Therefore, all action on the Ethereum block chain is set in
motion by transactions fired from externally-controlled accounts.

The simplest transactions are ether transfer transactions. But before we
go into that you should read up on
`accounts <https://github.com/ethereum/go-ethereum/wiki/Managing-your-accounts>`__
and perhaps on
`mining <https://github.com/ethereum/go-ethereum/wiki/Mining>`__.

Ether transfer
==============

Assuming the account you are using as sender has sufficient funds,
sending ether couldn't be easier. Which is also why you should probably
be careful with this! You have been warned.

.. code:: js

    eth.sendTransaction({from: '0x036a03fc47084741f83938296a1c8ef67f6e34fa', to: '0xa8ade7feab1ece71446bed25fa0cf6745c19c3d5', value: web3.toWei(1, "ether")})

Note the unit conversion in the ``value`` field. Transaction values are
expressed in weis, the most granular units of value. If you want to use
some other unit (like ``ether`` in the example above), use the function
``web3.toWei`` for conversion.

Also, be advised that the amount debited from the source account will be
slightly larger than that credited to the target account, which is what
has been specified. The difference is a small transaction fee, discussed
in more detail later.

Contracts can receive transfers just like externally controlled
accounts, but they can also receive more complicated transactions that
actually run (parts of) their code and update their state. In order to
understand those transactions, a rudimentary understanding of contracts
is required.

Writing a contract
==================

Contracts live on the blockchain in an Ethereum-specific binary format
(Ethereum Virtual Machine (=EVM) bytecode). However, contracts are
typically written in some high level language such as
`solidity <https://github.com/ethereum/wiki/wiki/Solidity-Tutorial>`__
and then compiled into byte code to be uploaded on the blockchain.

Note that other languages also exist, notably
`serpent <https://github.com/ethereum/wiki/wiki/Serpent>`__ and
`LLL <https://github.com/ethereum/cpp-ethereum/wiki/LLL>`__. Legacy
Mutan (an early c-like language) is no longer officially maintained.

Language Resources
------------------

Solidity
~~~~~~~~

Docs and tutorials
^^^^^^^^^^^^^^^^^^

-  `Ethereum wiki
   tutorial <https://github.com/ethereum/wiki/wiki/Solidity-Tutorial>`__
-  `Solidity FAQ - Ethereum
   forum <https://forum.ethereum.org/discussion/1460/solidity-faq>`__
-  `The Solidity Programming Language ·
   ethereum/wiki <https://github.com/ethereum/wiki/wiki/The-Solidity-Programming-Language>`__
-  `Ethereum ÐΞVcon-0: Solidity, Vision and Roadmap - YouTube
   Video <https://www.youtube.com/watch?v=DIqGDNPO5YM>`__
-  `Dapps for beginners <https://dappsforbeginners.wordpress.com/>`__
-  `Tutorial
   1 <https://forum.ethereum.org/discussion/1634/tutorial-1-your-first-contract/p1>`__
-  `Tutorial
   2 <https://forum.ethereum.org/discussion/1635/tutorial-2-rainbow-coin>`__
-  `Tutorial 3 (JavaScript API for
   Ethereum) <https://forum.ethereum.org/discussion/1636/tutorial-3-introduction-to-the-javascript-api>`__
   (Outdated)
-  `Solidity tutorial 1 by Eris
   Industries <https://eng.erisindustries.com/tutorials/2015/03/11/solidity-1/>`__
-  `dapp tutorials by Andreas Olofsson (Eris
   Industries) <https://www.youtube.com/playlist?list=PL_kFomDrqPoZBu5uxd8OBGColQPYbuz3i>`__
-  `Eris Solidity
   resources <https://github.com/eris-ltd/solidity-resources>`__

Examples
^^^^^^^^

-  `A dapp
   listing <https://github.com/ethereum/wiki/wiki/FAQ#where-can-i-find-example-%C3%90apps>`__
-  `Solidity Contracts on Ethereum -
   Ether.Fund <https://ether.fund/contracts/solidity>`__
-  `Ethereum dapp bin <https://github.com/ethereum/dapp-bin/>`__
-  `Solidity Standard
   Library <https://github.com/ethereum/wiki/wiki/Solidity-standard-library>`__
-  `Whisper chat
   dapp <https://github.com/ethereum/meteor-dapp-whisper-chat-client/tree/master/dist/deploy>`__
   written in meteor
-  `order statistic
   tree <https://github.com/drcode/ethereum-order-statistic-tree>`__ by
   Conrad Bars

Compilers
^^^^^^^^^

-  `Solidity realtime
   compiler <https://chriseth.github.io/browser-solidity/>`__

Serpent
~~~~~~~

-  `source on github <https://github.com/ethereum/serpent>`__
-  `serpent language
   spec <https://github.com/ethereum/wiki/wiki/Serpent>`__

Contract/dapp development environments and frameworks
-----------------------------------------------------

-  `Mix standalone
   IDE <https://github.com/ethereum/wiki/wiki/Mix:-The-DApp-IDE>`__ by
   ETHDEV
-  in-browser `Cosmo <http://meteor-dapp-cosmo.meteor.com>`__ that
   connects to ``geth`` via RPC. By Nick Dodson
-  `embark
   framework <https://github.com/iurimatias/embark-framework/>`__ by
   Iuri Mathias
-  `truffle <https://github.com/ConsenSys/truffle>`__ by Tim Coulter

Compiling a contract
====================

Contracts live on the blockchain in an Ethereum-specific binary format
(Ethereum Virtual Machine (=EVM) bytecode). However, contracts are
typically written in some high level language such as
`solidity <https://github.com/ethereum/wiki/wiki/Solidity-Tutorial>`__
and then compiled into byte code to be uploaded on the blockchain.

For the frontier release, ``geth`` supports solidity compilation through
system call to ``solc``, the command line `solidity
compiler <https://github.com/ethereum/cpp-ethereum/tree/develop/solc>`__
by Christian R. and Lefteris K. You can try `Solidity realtime
compiler <https://chriseth.github.io/cpp-ethereum/>`__ (by Christian R)
or `Cosmo <http://meteor-dapp-cosmo.meteor.com>`__ or
`Mix <https://github.com/ethereum/wiki/wiki/Mix:-The-DApp-IDE>`__.

If you start up your ``geth`` node, you can check if the solidity
compiler is available. This is what happens, if it is not:

.. code:: js

    > eth.compile.solidity("")
    eth_compileSolidity method not available: solc (solidity compiler) not found
        at InvalidResponse (<anonymous>:-57465:-25)
        at send (<anonymous>:-115373:-25)
        at solidity (<anonymous>:-104109:-25)
        at <anonymous>:1:1

After you found a way to install ``solc``, you make sure it's in the
path. If
```eth.getCompilers()`` <https://github.com/ethereum/wiki/wiki/JavaScript-API#web3ethgetcompilers>`__
still does not find it (returns an empty array), you can set a custom
path to the ``solc`` executable on the command line using th ``solc``
flag.

::

    geth --datadir ~/frontier/00 --solc /usr/local/bin/solc --natspec

You can also set this option at runtime via the console:

.. code:: js

    > admin.setSolc("/usr/local/bin/solc")
    solc v0.9.32
    Solidity Compiler: /usr/local/bin/solc
    Christian <c@ethdev.com> and Lefteris <lefteris@ethdev.com> (c) 2014-2015
    true

Let us take this simple contract source:

.. code:: js

    > source = "contract test { function multiply(uint a) returns(uint d) { return a * 7; } }"

This contract offers a unary method: called with a positive integer
``a``, it returns ``a * 7``.

You are ready to compile solidity code in the ``geth`` JS console using
```eth.compile.solidity`` <https://github.com/ethereum/wiki/wiki/JavaScript-API#web3ethcompilesolidity>`__:

.. code:: js

    > contract = eth.compile.solidity(source).test
    {
      code: '605280600c6000396000f3006000357c010000000000000000000000000000000000000000000000000000000090048063c6888fa114602e57005b60376004356041565b8060005260206000f35b6000600782029050604d565b91905056',
      info: {
        language: 'Solidity',
        languageVersion: '0',
        compilerVersion: '0.9.13',
        abiDefinition: [{
          constant: false,
          inputs: [{
            name: 'a',
            type: 'uint256'
          } ],
          name: 'multiply',
          outputs: [{
            name: 'd',
            type: 'uint256'
          } ],
          type: 'function'
        } ],
        userDoc: {
          methods: {
          }
        },
        developerDoc: {
          methods: {
          }
        },
        source: 'contract test { function multiply(uint a) returns(uint d) { return a * 7; } }'
      }
    }

The compiler is also available via
`RPC <https://github.com/ethereum/wiki/wiki/JSON-RPC>`__ and therefore
via
`web3.js <https://github.com/ethereum/wiki/wiki/JavaScript-API#web3ethcompilesolidity>`__
to any in-browser Ðapp connecting to ``geth`` via RPC/IPC.

The following example shows how you interface ``geth`` via JSON-RPC to
use the compiler.

::

    ./geth --datadir ~/eth/ --loglevel 6 --logtostderr=true --rpc --rpcport 8100 --rpccorsdomain '*' --mine console  2>> ~/eth/eth.log
    curl -X POST --data '{"jsonrpc":"2.0","method":"eth_compileSolidity","params":["contract test { function multiply(uint a) returns(uint d) { return a * 7; } }"],"id":1}' http://127.0.0.1:8100

The compiler output for one source will give you contract objects each
representing a single contract. The actual return value of
``eth.compile.solidity`` is a map of contract name -- contract object
pairs. Since our contract's name is ``test``,
``eth.compile.solidity(source).test`` will give you the contract object
for the test contract containing the following fields:

-  ``code``: the compiled EVM code
-  ``info``: the rest of the metainfo the compiler outputs
-  ``source``: the source code
-  ``language``: contract language (Solidity, Serpent, LLL)
-  ``languageVersion``: contract language version
-  ``compilerVersion``: compiler version
-  ``abiDefinition``: `Application Binary Interface
   Definition <https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI>`__
-  ``userDoc``: `NatSpec user
   Doc <https://github.com/ethereum/wiki/wiki/Ethereum-Natural-Specification-%20Format>`__
-  ``developerDoc``: `NatSpec developer
   Doc <https://github.com/ethereum/wiki/wiki/Ethereum-Natural-Specification-Format>`__

The immediate structuring of the compiler output (into ``code`` and
``info``) reflects the two very different **paths of deployment**. The
compiled EVM code is sent off to the blockchain with a contract creation
transaction while the rest (info) will ideally live on the decentralised
cloud as publicly verifiable metadata complementing the code on the
blockchain.

If your source contains multiple contracts, the output will contain an
entry for each contact, the corresponding contract info object can be
retrieved with the name of the contract as attribute name. You can try
this by inspecting the most current GlobalRegistrar code:

.. code:: js

    contracts = eth.compile.solidity(globalRegistrarSrc)

Creating and deploying a contract
=================================

Now that you got both an unlocked account as well as some funds, you can
create a contract on the blockchain by `sending a
transaction <https://github.com/ethereum/wiki/wiki/JavaScript-API#web3ethsendtransaction>`__
to the empty address with the evm code as data. Simple, eh?

.. code:: js

    primaryAddress = eth.accounts[0]
    MyContract = eth.contract(abi);
    contact = MyContract.new(arg1, arg2, ...,{from: primaryAddress, data: evmCode})

All binary data is serialised in hexadecimal form. Hex strings always
have a hex prefix ``0x``.

Note that ``arg1, arg2, ...`` are the arguments for the contract
constructor, in case it accepts any.

Also note that this step requires you to pay for execution. Your balance
on the account (that you put as sender in the ``from`` field) will be
reduced according to the gas rules of the VM once your transaction makes
it into a block. More on that later. After some time, your transaction
should appear included in a block confirming that the state it brought
about is a consensus. Your contract now lives on the blockchain.

The asynchronous way of doing the same looks like this:

.. code:: js

    MyContract.new([arg1, arg2, ...,]{from: primaryAccount, data: evmCode}, function(err, contract) {
      if (!err && contract.address)
        console.log(contract.address);
    });

Gas and transaction costs
=========================

So how did you pay for all this? Under the hood, the transaction
specified a gas limit and a gasprice, both of which could have been
specified directly in the transaction object.

Gas limit is there to protect you from buggy code running until your
funds are depleted. The product of ``gasPrice`` and ``gas`` represents
the maximum amount of Wei that you are willing to pay for executing the
transaction. What you specify as ``gasPrice`` is used by miners to rank
transactions for inclusion in the blockchain. It is the price in Wei of
one unit of gas, in which VM operations are priced.

The gas expenditure incurred by running your contract will be bought by
the ether you have in your account at a price you specified in the
transaction with ``gasPrice``. If you do not have the ether to cover all
the gas requirements to complete running your code, the processing
aborts and all intermediate state changes roll back to the
pre-transaction snapshot. The gas used up to the point where execution
stopped were used after all, so the ether balance of your account will
be reduced. These parameters can be adjusted on the transaction object
fields ``gas`` and ``gasPrice``. The ``value`` field is used the same as
in ether transfer transactions between normal accounts. In other words
transferring funds is available between any two accounts, either normal
(i.e. externally controlled) or contract. If your contract runs out of
funds, you should see an insufficient funds error.

For testing and playing with contracts you can use the test network or
`set up a private node (or
cluster) <https://github.com/ethereum/go-ethereum/wiki/Setting-up-private-network-or-local-cluster>`__
potentially isolated from all the other nodes. If you then mine, you can
make sure that your transaction will be included in the next block. You
can see the pending transactions with:

.. code:: js

    eth.getBlock("pending", true).transactions

You can retrieve blocks by number (height) or by their hash:

.. code:: js

    genesis = eth.getBlock(0)
    eth.getBlock(genesis.hash).hash == genesis.hash
    true

Use ``eth.blockNumber`` to get the current blockchain height and the
"latest" magic parameter to access the current head (newest block).

.. code:: js

    currentHeight = eth.blockNumber()
    eth.getBlock("latest").hash == eth.getBlock(eth.blockNumber).hash
    true

Contract info (metadata)
========================

In the previous sections we explained how you create a contract on the
blockchain. Now we deal with the rest of the compiler output, the
**contract metadata** or contract info. The idea is that

-  contract info is uploaded somewhere identifiable by a ``url`` which
   is publicly accessible
-  anyone can find out what the ``url`` is only knowing the contracts
   address

These requirements are achieved very simply by using a 2 step blockchain
registry. The first step registers the contract code (hash) with a
content hash in a contract called ``HashReg``. The second step registers
a url with the content hash in the ``UrlHint`` contract. These `simple
registry
contracts <https://github.com/ethereum/go-ethereum/blob/develop/common/registrar/contracts.go>`__
will be part of the frontier proposition.

By using this scheme, it is sufficient to know a contract's address to
look up the url and fetch the actual contract metadata info bundle. Read
on to learn why this is good.

So if you are a conscientious contract creator, the steps are the
following:

1. Deploy the contract itself to the blockchain
2. Get the contract info json file.
3. Deploy contract info json file to any url of your choice
4. Register codehash ->content hash -> url

The JS API makes this process very easy by providing helpers. Call
```admin.register`` <>`__ to extract info from the contract, write out
its json serialisation in the given file, calculates the content hash of
the file and finally registers this content hash to the contract's code
hash. Once you deployed that file to any url, you can use
```admin.registerUrl`` <>`__ to register the url with your content hash
on the blockchain as well. (Note that in case a fixed content addressed
model is used as document store, the url-hint is no longer necessary.)

.. code:: js

    source = "contract test { function multiply(uint a) returns(uint d) { return a * 7; } }"
    // compile with solc
    contract = eth.compile.solidity(source).test
    // create contract object
    var MyContract = eth.contract(contract.info.abiDefinition)
    // extracts info from contract, save the json serialisation in the given file,
    contenthash = admin.saveInfo(contract.info, "~/dapps/shared/contracts/test/info.json")
    // send off the contract to the blockchain
    MyContract.new({from: primaryAccount, data: contract.code}, function(error, contract){
      if(!error && contract.address) {
        // calculates the content hash and registers it with the code hash in `HashReg`
        // it uses address to send the transaction.
        // returns the content hash that we use to register a url
        admin.register(primaryAccount, contract.address, contenthash)
        // here you deploy ~/dapps/shared/contracts/test/info.json to a url
        admin.registerUrl(primaryAccount, hash, url)
      }
    });

Interacting with contracts
==========================

```eth.contract`` <https://github.com/ethereum/wiki/wiki/JavaScript-API#web3ethcontract>`__
can be used to define a contract *class* that will comply with the
contract interface as described in its `ABI
definition <https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI>`__.

.. code:: js

    var Multiply7 = eth.contract(contract.info.abiDefinition);
    var myMultiply7 = Multiply7.at(address);

Now all the function calls specified in the abi are made available on
the contract instance. You can just call those methods on the contract
instance and chain ``sendTransaction(3, {from: address})`` or
``call(3)`` to it. The difference between the two is that ``call``
performs a "dry run" locally, on your computer, while
``sendTransaction`` would actually submit your transaction for inclusion
in the block chain and the results of its execution will eventually
become part of the global consensus. In other words, use ``call``, if
you are interested only in the return value and use ``sendTransaction``
if you only care about "side effects" on the state of the contract.

In the example above, there are no side effects, therefore
``sendTransaction`` only burns gas and increases the entropy of the
universe. All "useful" functionality is exposed by ``call``:

.. code:: js

    myMultiply7.multiply.call(6)
    42

Now suppose this contract is not yours, and you would like documentation
or look at the source code. This is made possible by making available
the contract info bundle and register it in the blockchain. The
``admin`` API provides convenience methods to fetch this bundle for any
contract that chose to register. To see how it works, read about
`Contract
Metadata <https://github.com/ethereum/wiki/wiki/Contract-metadata>`__ or
read the contract info deployment section of this document.

.. code:: js

    // get the contract info for contract address to do manual verification
    var info = admin.getContractInfo(address) // lookup, fetch, decode
    var source = info.source;
    var abiDef = info.abiDefinition

NatSpec
=======

This section will further elaborate what you can do with contracts and
transactions building on a protocol NatSpec. Solidity implements smart
comments doxigen style which then can be used to generate various
facades meta documents of the code. One such use case is to generate
custom messages for transaction confirmation that clients can prompt
users with.

So we now extend the ``multiply7`` contract with a smart comment
specifying a custom confirmation message (notice).

.. code:: js

    contract test {
       /// @notice Will multiply `a` by 7.
       function multiply(uint a) returns(uint d) {
           return a * 7;
       }
    }

The comment has expressions in between backticks which are to be
evaluated at the time the transaction confirmation message is presented
to the user. The variables that refer to parameters of method calls then
are instantiated in accordance with the actual transaction data sent by
the user (or the user's dapp). NatSpec support for confirmation notices
is fully implemented in ``geth``. NatSpec relies on both the abi
definition as well as the userDoc component to generate the proper
confirmations. Therefore in order to access that, the contract needs to
have registered its contract info as described above.

Let us see a full example. As a very conscientious smart contract dev,
you first create your contract and deploy according to the recommended
steps above:

.. code:: js

    source = "contract test {
       /// @notice Will multiply `a` by 7.
       function multiply(uint a) returns(uint d) {
           return a * 7;
       }
    }"
    contract = eth.compile.solidity(source).test
    MyContract = eth.contract(contract.info.abiDefinition)
    contenthash = admin.saveInfo(contract.info, "~/dapps/shared/contracts/test/info.json")
    MyContract.new({from: primary, data: contract.code}, function(error, contract){
      if(!error && contract.address) {
        admin.register(primary, contract.address, contenthash)
        // put it up on your favourite oldworld site:
        admin.registerUrl(contentHash, "http://dapphub.com/test/info.json")
      }
    });

Note that if we use content addressed storage system like swarm the
second step is unnecessary, since the contenthash is (deterministically
translates to) the unique address of the content itself.

For the purposes of a painless example just simply use the file url
scheme (not exactly the cloud, but will show you how it works) without
needing to deploy.

.. code:: js

    admin.registerUrl(contentHash, "file:///home/nirname/dapps/shared/contracts/test/info.json")

Now you are done as a dev, so swap seats as it were and pretend that you
are a user who is sending a transaction to the infamous ``multiply7``
contract.

You need to start the client with the ``--natspec`` flag to enable smart
confirmations and contractInfo fetching. You can also set it on the
console with ``admin.startNatSpec()`` and ``admin.stopNatSpec()``.

::

    geth --natspec --unlock primary console 2>> /tmp/eth.log

Now at the console type:

.. code:: js

    // obtain the abi definition for your contract
    var info = admin.getContractInfo(address)
    var abiDef = info.abiDefinition
    // instantiate a contract for transactions
    var Multiply7 = eth.contract(abiDef);
    var myMultiply7 = Multiply7.at(address);

And now try to send an actual transaction:

.. code:: js

    > myMultiply7.multiply.sendTransaction(6, {from: eth.accounts[0]})
    NatSpec: Will multiply 6 by 7.
    Confirm? [y/n] y
    >

When this transaction gets included in a block, somewhere on a lucky
miner's computer, 6 will get multiplied by 7, with the result ignored.
Mission accomplished.

If the transaction is not picked up, we can see it with:

.. code:: js

    eth.pendingTransactions

This accumulates all the transactions sent, even the ones that were
rejected and are not included in the current mined block (trans state).
These latter can be shown by:

.. code:: js

    eth.getBlock("pending", true).transactions()

if you identify the index of your rejected transaction, you can resend
it with modified gas limit and gas price (both optional parameters):

.. code:: js

    tx = eth.pendingTransactions[1]
    eth.resend(tx, newGasPrice, newGasLimit)

Testing contracts and transactions
==================================

Often you need to resort to a low level strategy of testing and
debugging contracts and transactions. This section introduces some debug
tools and practices you can use. In order to test contracts and
transactions without real-word consequences, you best test it on a
private blockchain. This can be achieved with configuring an alternative
network id (select a unique integer) and/or disable peers. It is
recommended practice that for testing you use an alternative data
directory and ports so that you never even accidentally clash with your
live running node (assuming that runs using the defaults. Starting your
``geth`` with in VM debug mode with profiling and highest logging
verbosity level is recommended:

.. code:: js

    geth --datadir ~/dapps/testing/00/ --port 30310 --rpcport 8110 --networkid 4567890 --nodiscover --maxpeers 0 --vmdebug --verbosity 6 --pprof --pprofport 6110 console 2>> ~/dapp/testint/00/00.log

Before you can submit any transactions, you need mine some ether on your
private chain and for that you need an account. See the sections on
`Mining <https://github.com/ethereum/go-ethereum/wiki/Mining>`__ and
`Accounts <https://github.com/ethereum/go-ethereum/wiki/Managing-Your-Accounts>`__

.. code:: js

    // create account. will prompt for password
    personal.newAccount("mypassword");
    // name your primary account, will often use it
    primary = eth.accounts[0];
    // check your balance (denominated in ether)
    balance = web3.fromWei(eth.getBalance(primary), "ether");

.. code:: js

    // assume an existing unlocked primary account
    primary = eth.accounts[0];

    // mine 10 blocks to generate ether

    // starting miner
    miner.start(8);
    // sleep for 10 blocks.
    admin.sleepBlocks(10);
    // then stop mining (just not to burn heat in vain)
    miner.stop()  ;
    balance = web3.fromWei(eth.getBalance(primary), "ether");

After you create transactions, you can force process them with the
following lines:

::

    miner.start(1);
    admin.sleepBlocks(1);
    miner.stop()  ;

you can check your pending transactions with

.. code:: js

    // shows transaction pool
    txpool.status
    // number of pending txs
    eth.getBlockTransactionCount("pending");
    // print all pending txs
    eth.getBlock("pending", true).transactions

If you submitted contract creation transaction, you can check if the
desired code actually got inserted in the current blockchain:

.. code:: js

    txhash = eth.sendTansaction({from:primary, data: code})
    //... mining
    contractaddress = eth.getTransactionReceipt(txhash);
    eth.getCode(contractaddress)

Registrar services
==================

The frontier chain comes with some very basic baselayer services, most
of all the registrar. The registrar is composed of 3 components.

-  GlobalRegistrar to associate names (strings) to accounts (addresses).
-  HashReg to associate hashes to hashes (map any object to a 'content'
   hash.
-  UrlHint to associate content hashes to a hint for the location of the
   content. This is needed only if content storage is not content
   addressed, otherwise content hash is already the content address. If
   it is used, content fetched from the url should hash to content hash.
   In order to check authenticity of content one can check if this
   verifies.

Create and deploy GlobalRegistrar, HashReg and UrlHint
------------------------------------------------------

If the registrar contracts are not hardcoded in the blockchain (they are
not at the time of writing), the registrars need to be deployed at least
once on every chain.

If you are on *the main live chain*, the address of the main global
registrar is hardcoded in the latest clients and therefore *you do not
need to do anything*. If you want to change this or you are on a private
chain you need to deploy these contracts at least once:

.. code:: js

    primary = eth.accounts[0];

    globalRegistrarAddr = admin.setGlobalRegistrar("", primary);
    hashRegAddr = admin.setHashReg("", primary);
    urlHintAddr = admin.setUrlHint("", primary);

You need to mine or wait till the txs are all picked up. Initialise the
registrar on the new address and check if the other registrars' names
resolve to the correct addresses:

.. code:: js

    registrar = GlobalRegistrar.at(globalRegistrarAddr);
    primary == registrar.owner("HashReg");
    primary == registrar.owner("UrlHint");
    hashRegAddr == registrar.addr("HashReg");
    urlHintAddr registrar.addr("UrlHint");

and the following ones return correct code:

.. code:: js

    eth.getCode(registrar.address);
    eth.getCode(registrar.addr("HashReg"));
    eth.getCode(registrar.addr("UrlHint"));

From the second time onwards on the same chain as well as on other
nodes, you simply seed with the GlobalRegistrars address, the rest is
handled through it.

.. code:: js

    primary = eth.accounts[0];
    globalRegistrarAddr = "0x225178b4829bbe7c9f8a6d2e3d9d87b66ed57d4f"

    // set the global registrar address
    admin.setGlobalRegistrar(globalRegistrarAddr)
    // set HashReg address via globalRegistrar
    hashRegAddr = admin.setHashReg()
    // set UrlHint address via globalRegistrar
    urlHintAddr = admin.setUrlHint()

    // (re)sets the registrar variable to a GlobalRegistrar contract instance
    registrar = GlobalRegistrar.at(globalRegistrarAddr);

If this is successful, you should be able to check with the following
commands if the registrar returns addresses:

.. code:: js

    registrar.owner("HashReg");
    registrar.owner("UrlHint");
    registrar.addr("HashReg");
    registrar.addr("UrlHint");

and the following ones return correct code:

.. code:: js

    eth.getCode(registrar.address);
    eth.getCode(registrar.addr("HashReg"));
    eth.getCode(registrar.addr("UrlHint"));

Using the registrar services
----------------------------

Can provide useful interfaces between contracts and dapps.

Global registrar
~~~~~~~~~~~~~~~~

To reserve a name register an account address with it, you need the
following:

::

    registrar.reserve.sendTransaction(name, {from:primary})
    registrar.setAddress.sendTransaction (name, address, true, {from: primary})

You need to wait for the transactions to be picked up (or force mine
them if you are on a private chain). To check you query the registrar:

.. code:: js

    registrar.owner(name)
    registrar.addr(name)

HashReg and UrlHint
~~~~~~~~~~~~~~~~~~~

HashReg and UrlHint can be used with the following abis:

.. code:: js

    hashRegAbi = '[{"constant":false,"inputs":[],"name":"setowner","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"_key","type":"uint256"},{"name":"_content","type":"uint256"}],"name":"register","outputs":[],"type":"function"}]'
    urlHintAbi = '[{"constant":false,"inputs":[{"name":"_hash","type":"uint256"},{"name":"idx","type":"uint8"},{"name":"_url","type":"uint256"}],"name":"register","outputs":[],"type":"function"}]'

setting up the contract instances:

.. code:: js

    hashReg = eth.contract(hashRegAbi).at(registrar.addr("HashReg")));
    urlHint = eth.contract(UrlHintAbi).at(registrar.addr("UrlHint")));

Associate a content hash to a key hash:

.. code:: js

    hashReg.register.sendTransaction(keyhash, contenthash, {from:primary})

Associate a url to a content hash:

.. code:: js

    urlHint.register.sendTransaction(contenthash, url, {from:primary})

To check resolution:

.. code:: js

    contenthash = hashReg._hash(keyhash);
    url = urlHint._url(contenthash);

Example script
==============

The example script below demonstrates most features discussed in this
tutorial. You can run it with the
`JSRE <https://github.com/ethereum/go-ethereum/wiki/JavaScript-Console>`__
as ``geth js script.js 2>>geth.log`` . If you want to run this test on a
local private chain, then start geth with:

::

    geth --maxpeers 0 --networkid 123456 --nodiscover --unlock primary js script.js 2>> geth.log

Note that ``networkid`` can be any arbitrary non-negative integer, 0 is
always the live net.

::

    personal.newAccount("")

    primary = eth.accounts[0];
    balance = web3.fromWei(eth.getBalance(primary), "ether");
    personal.unlockAccount(primary, "00");
    // miner.setEtherbase(primary)

    miner.start(8); admin.sleepBlocks(10); miner.stop()  ;

    // 0xc6d9d2cd449a754c494264e1809c50e34d64562b
    primary = eth.accounts[0];
    balance = web3.fromWei(eth.getBalance(primary), "ether");

    globalRegistrarTxHash = admin.setGlobalRegistrar("0x0");
    //'0x0'
    globalRegistrarTxHash = admin.setGlobalRegistrar("", primary);
    //'0xa69690d2b1a1dcda78bc7645732bb6eefcd6b188eaa37abc47a0ab0bd87a02e8'
    miner.start(1); admin.sleepBlocks(1); miner.stop();
    //true
    globalRegistrarAddr = eth.getTransactionReceipt(globalRegistrarTxHash).contractAddress;
    //'0x3d255836f5f8c9976ec861b1065f953b96908b07'
    eth.getCode(globalRegistrarAddr);
    //...
    admin.setGlobalRegistrar(globalRegistrarAddr);
    registrar = GlobalRegistrar.at(globalRegistrarAddr);

    hashRegTxHash = admin.setHashReg("0x0");
    hashRegTxHash = admin.setHashReg("", primary);
    txpool.status
    miner.start(1); admin.sleepBlocks(1); miner.stop();
    hashRegAddr = eth.getTransactionReceipt(hashRegTxHash).contractAddress;
    eth.getCode(hashRegAddr);

    registrar.reserve.sendTransaction("HashReg", {from:primary});
    registrar.setAddress.sendTransaction("HashReg",hashRegAddr,true, {from:primary});
    miner.start(1); admin.sleepBlocks(1); miner.stop();
    registrar.owner("HashReg");
    registrar.addr("HashReg");

    urlHintTxHash = admin.setUrlHint("", primary);
    miner.start(1); admin.sleepBlocks(1); miner.stop();
    urlHintAddr = eth.getTransactionReceipt(urlHintTxHash).contractAddress;
    eth.getCode(urlHintAddr);

    registrar.reserve.sendTransaction("UrlHint", {from:primary});
    registrar.setAddress.sendTransaction("UrlHint",urlHintAddr,true, {from:primary});
    miner.start(1); admin.sleepBlocks(1); miner.stop();
    registrar.owner("UrlHint");
    registrar.addr("UrlHint");

    globalRegistrarAddr = "0xfd719187089030b33a1463609b7dfea0e5de25f0"
    admin.setGlobalRegistrar(globalRegistrarAddr);
    registrar = GlobalRegistrar.at(globalRegistrarAddr);
    admin.setHashReg("");
    admin.setUrlHint("");

    ///// ///////////////////////////////

    admin.stopNatSpec();
    primary = eth.accounts[0];
    personal.unlockAccount(primary, "00")

    globalRegistrarAddr = "0xfd719187089030b33a1463609b7dfea0e5de25f0";
    admin.setGlobalRegistrar(globalRegistrarAddr);
    registrar = GlobalRegistrar.at(globalRegistrarAddr);
    admin.setHashReg("0x0");
    admin.setHashReg("");
    admin.setUrlHint("0x0");
    admin.setUrlHint("");


    registrar.owner("HashReg");
    registrar.owner("UrlHint");
    registrar.addr("HashReg")
    registrar.addr("UrlHint");


    /////////////////////////////////////
    eth.getBlockTransactionCount("pending");
    miner.start(1); admin.sleepBlocks(1); miner.stop();

    source = "contract test {\n" +
    "   /// @notice will multiply `a` by 7.\n" +
    "   function multiply(uint a) returns(uint d) {\n" +
    "      return a * 7;\n" +
    "   }\n" +
    "} ";
    contract = eth.compile.solidity(source).test;
    txhash = eth.sendTransaction({from: primary, data: contract.code});

    eth.getBlock("pending", true).transactions;

    miner.start(1); admin.sleepBlocks(1); miner.stop();
    contractaddress = eth.getTransactionReceipt(txhash).contractAddress;
    eth.getCode(contractaddress);

    multiply7 = eth.contract(contract.info.abiDefinition).at(contractaddress);
    fortytwo = multiply7.multiply.call(6);

    /////////////////////////////////

    // register a name for the contract
    registrar.reserve.sendTransaction(primary,  {from: primary});
    registrar.setAddress.sendTransaction("multiply7", contractaddress, true, {from: primary});
    ////////////////////////

    admin.stopNatSpec();
    filename = "/info.json";
    contenthash = admin.saveInfo(contract.info, "/tmp" + filename);
    admin.register(primary, contractaddress, contenthash);
    eth.getBlock("pending", true).transactions;
    miner.start(1); admin.sleepBlocks(1); miner.stop();

    admin.registerUrl(primary, contenthash, "file://" + filename);
    eth.getBlock("pending", true).transactions;
    miner.start(1); admin.sleepBlocks(1); miner.stop();

    ////////////////////

    // retrieve contract address using global registrar entry with 'multply7'
    contractaddress = registrar.addr("multiply7);
    // retrieve the info using the url
    info = admin.getContractInfo(contractaddress);
    multiply7 = eth.contract(info.abiDefinition).at(contractaddress);
    // try Natspec
    admin.startNatSpec();
    fortytwo = multiply7.multiply.sendTransaction(6, { from: primary });

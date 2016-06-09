.. _Contracts:

********************************************************************************
Contracts
********************************************************************************

What is a contract?
================================================================================

A contract is a collection of code (its functions) and data (its state) that
resides at a specific address on the Ethereum blockchain. Contract accounts are
able to pass messages between themselves as well as doing practically Turing
complete computation. Contracts live on the blockchain in a Ethereum-specific
binary format called Ethereum Virtual Machine (EVM) bytecode.

Contracts are typically written in some high level language such as `Solidity
<https://solidity.readthedocs.org/en/latest/>`_ and then compiled into bytecode
to be uploaded on the blockchain.

.. seealso:: Other languages also exist, notably Serpent and LLL, which are described further in the :ref:`ethereum-high-level-languages` section of this documentation.

:ref:`IDE-or-development-framework` lists the integrated development environments, developer tools that help you develop in these languages, offering testing, and deployment support among other features.

.. _ethereum-high-level-languages:

Ethereum high level languages
===========================================================================

Contracts live on the blockchain in an Ethereum-specific binary format (EVM bytecode) that is executed by the Ethereum Virtual Machine (EVM). However, contracts are typically written in a higher level language and then compiled using the EVM compiler into byte code to be deployed to the blockchain.

Below are the different high level languages developers can use to write smart contracts for Ethereum.

Solidity
--------------------------------------------------------------------------------

Solidity is a language similar to JavaScript which allows you to develop contracts and compile to EVM bytecode. It is currently the flagship language of Ethereum and the most popular.

* `Solidity Documentation <http://solidity.readthedocs.org/en/latest/>`_ - Solidity is the flagship Ethereum high level language that is used to write contracts.
* `Solidity online realtime compiler <http://ethereum.github.io/browser-solidity/>`_
* `Standardized Contract APIs <https://github.com/ethereum/wiki/wiki/Standardized_Contract_APIs>`__
* `Useful Ðapp Patterns <https://github.com/ethereum/wiki/wiki/Useful-Ðapp-Patterns>`__ - Code snippets which are useful for Ðapp development.

Serpent
--------------------------------------------------------------------------------

Serpent is a language similar to Python which can be used to develop contracts and compile to EVM bytecode. It is intended to be maximally clean and simple, combining many of the efficiency benefits of a low-level language with ease-of-use in programming style, and at the same time adding special domain-specific features for contract programming. Serpent is compiled using _`LLL`.

* `Serpent on the ethereum wiki <https://github.com/ethereum/wiki/wiki/Serpent>`_
* `Serpent EVM compiler <https://github.com/ethereum/serpent>`_

LLL
--------------------------------------------------------------------------------

`Lisp Like Language (LLL) <https://github.com/ethereum/libethereum/tree/develop/liblll>`_ is a low level language similar to Assembly. It is meant to be very simple and minimalistic; essentially just a tiny wrapper over coding in EVM directly.

* `LIBLLL in GitHub <https://github.com/ethereum/libethereum/tree/develop/liblll>`_
* `Examples of LLL <https://www.reddit.com/r/ethereum/comments/3secu1/anyone_have_a_copy_of_the_old_lll_tutorials/>`_

Mutan (deprecated)
--------------------------------------------------------------------------------

`Mutan <https://github.com/obscuren/mutan>`_ is a statically typed, C-like language designed and developed by Jeffrey Wilcke. It is no longer maintained.


Writing a contract
================================================================================

No language would be complete without a Hello World program. Operating within
the Ethereum environment, Solidity has no obvious way of "outputting" a string.
The closest we can do is to use a *log event* to place a string into the
blockchain:

.. code:: js

	contract HelloWorld {
		event Print(string out);
		function() { Print("Hello, World!"); }
	}

This contract will create a log entry on the blockchain of type Print with a
parameter "Hello, World!" each time it is executed.

.. seealso:: `Solidity docs <https://solidity.readthedocs.org/en/latest/>`_ has more examples and guidelines to writing Solidity code.

Compiling a contract
================================================================================

Compilation of solidity contracts can be accomplished via a number of
mechanisms.

* Using the ``solc`` compiler via the command line.
* Using ``web3.eth.compile.solidity`` in the javascript console provided by
  ``geth`` or ``eth`` (This still requires the ``solc`` compiler to be
  installed).
* The `online Solidity realtime compiler <https://ethereum.github.io/browser-solidity/>`_.
* The `Meteor dapp Cosmo for building solidity contracts <https://github.com/SilentCicero/meteor-dapp-cosmo>`_.
* The `Mix IDE <https://github.com/ethereum/wiki/wiki/Mix:-The-DApp-IDE>`_.
* The `Ethereum Wallet <https://github.com/ethereum/mist/releases>`_.

.. note::  More information on solc and compiling Solidity contract code can be found `here <https://solidity.readthedocs.org/en/latest/frequently-asked-questions.html#how-do-i-compile-contracts>`_.


Setting up the solidity compiler in geth
--------------------------------------------------------------------------------

If you start up your ``geth`` node, you can check which compilers are
available.

.. code:: bash

    > web3.eth.getCompilers();
    ["lll", "solidity", "serpent"]

This command returns an array of strings indicating which compilers are
currently available.

.. note::
    The ``solc`` compiler is installed with ``cpp-ethereum``.  Alternatively,
    you can `build it yourself
    <https://github.com/ethereum/go-ethereum/wiki/Building-Ethereum>`_.


If your ``solc`` executable is in a non-standard location you can specify a
custom path to the ``solc`` executable using th ``--solc`` flag.

.. code:: bash

    $ geth --solc /usr/local/bin/solc

Alternatively, you can set this option at runtime via the console:

.. code:: bash

    > admin.setSolc("/usr/local/bin/solc")
    solc, the solidity compiler commandline interface
    Version: 0.2.2-02bb315d/.-Darwin/appleclang/JIT linked to libethereum-1.2.0-8007cef0/.-Darwin/appleclang/JIT
    path: /usr/local/bin/solc

.. _compile_a_simple_contract:

Compiling a simple contract
--------------------------------------------------------------------------------

Let's compile a simple contract source:

.. code:: bash

    > source = "contract test { function multiply(uint a) returns(uint d) { return a * 7; } }"

This contract offers a single method **multiply** which is called with a
positive integer ``a`` and returns ``a * 7``.

You are ready to compile solidity code in the ``geth`` JS console using
`eth\.compile\.solidity\(\)
<https://github.com/ethereum/wiki/wiki/JavaScript-API#web3ethcompilesolidity>`_:


.. code:: bash

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

.. note::
    The compiler is also available via `RPC
    <https://github.com/ethereum/wiki/wiki/JSON-RPC>`__ and therefore via
    `web3\.js <https://github.com/ethereum/wiki/wiki/JavaScript
    API#web3ethcompilesolidity>`__ to any in-browser Ðapp connecting to
    ``geth`` via RPC/IPC.


The following example shows how you interface ``geth`` via JSON-RPC to
use the compiler.

.. code:: bash

    $ geth --datadir ~/eth/ --loglevel 6 --logtostderr=true --rpc --rpcport 8100 --rpccorsdomain '*' --mine console  2>> ~/eth/eth.log
    $ curl -X POST --data '{"jsonrpc":"2.0","method":"eth_compileSolidity","params":["contract test { function multiply(uint a) returns(uint d) { return a * 7; } }"],"id":1}' http://127.0.0.1:8100

The compiler output for one source will give you contract objects each
representing a single contract. The actual return value of
``eth.compile.solidity`` is a map of contract name to contract object pairs.
Since our contract's name is ``test``, ``eth.compile.solidity(source).test``
will give you the contract object for the test contract containing the
following fields:


.. glossary::

    ``code``
        The compiled EVM bytecode

    ``info``
        Additional metadata output from the compiler

    ``source``
        The source code

    ``language``
        The contract language (Solidity, Serpent, LLL)

    ``languageVersion``
        The contract language version

    ``compilerVersion``
        The solidity compiler version that was used to compile this contract.

    ``abiDefinition``
        The `Application Binary Interface Definition <https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI>`__

    ``userDoc``
        The `NatSpec Doc <https://github.com/ethereum/wiki/wiki/Ethereum-Natural-Specification-Format>`__ for users.

    ``developerDoc``
        The `NatSpec Doc <https://github.com/ethereum/wiki/wiki/Ethereum-Natural-Specification-Format>`__ for developers.


The immediate structuring of the compiler output (into ``code`` and ``info``)
reflects the two very different **paths of deployment**. The compiled EVM code
is sent off to the blockchain with a contract creation transaction while the
rest (info) will ideally live on the decentralised cloud as publicly verifiable
metadata complementing the code on the blockchain.

If your source contains multiple contracts, the output will contain an entry
for each contact, the corresponding contract info object can be retrieved with
the name of the contract as attribute name. You can try this by inspecting the
most current GlobalRegistrar code:

.. code:: js

    contracts = eth.compile.solidity(globalRegistrarSrc)


Create and deploy a contract
================================================================================

Before you begin this section, make sure you have both an unlocked account as
well as some funds.

You will now create a contract on the blockchain by `sending a transaction <https://github.com/ethereum/wiki/wiki/JavaScript-API#web3ethsendtransaction>`__ to the empty address with the EVM code from the previous section as data.

.. note::
    This can be accomplished much easier using the `online Solidity realtime
    compiler <https://ethereum.github.io/browser-solidity/>`_ or the `Mix IDE
    <https://github.com/ethereum/wiki/wiki/Mix:-The-DApp-IDE>`_ program.


.. code:: js

    primaryAddress = eth.accounts[0]
    abi  = [{ constant: false, inputs: [{ name: 'a', type: 'uint256' } ]
    MyContract = eth.contract.abi;
    contract = MyContract.new(arg1, arg2, ...,{from: primaryAddress, data: evmByteCodeFromPreviousSection})

All binary data is serialised in hexadecimal form. Hex strings always have a
hex prefix ``0x``.

.. note::
    Note that ``arg1, arg2, ...`` are the arguments for the contract
    constructor, in case it accepts any.  If the contract does not require any
    constructor arguments then these arguments can be omitted.

It is worth pointing out that this step requires you to pay for execution. Your
balance on the account (that you put as sender in the ``from`` field) will be
reduced according to the gas rules of the EVM once your transaction makes it
into a block. After some time, your transaction should appear included in a
block confirming that the state it brought about is a consensus. Your contract
now lives on the blockchain.

The asynchronous way of doing the same looks like this:

.. code-block:: js

    MyContract.new([arg1, arg2, ...,]{from: primaryAccount, data: evmCode}, function(err, contract) {
      if (!err && contract.address)
        console.log(contract.address);
    });


.. _interacting_with_a_contract:

Interacting with a contract
================================================================================

Interaction with a contract is typically done using an abstraction layer such
as the `eth.contract\(\)
<https://github.com/ethereum/wiki/wiki/JavaScript-API#web3ethcontract>`_
function which returns a javascript object with all of the contract functions
available as callable functions in javascript.

The standard way to describe the available functions of a contract is the `ABI
definition <https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI>`_.
This object is an array which describles the call signature and return values
for each available contract function.

.. code-block:: js

    var Multiply7 = eth.contract(contract.info.abiDefinition);
    var myMultiply7 = Multiply7.at(address);

Now all the function calls specified in the ABI are made available on the
contract instance. You can just call those methods on the contract instance
in one of two ways.

.. code-block:: js

    > myMultiply7.multiply.sendTransaction(3, {from: address})
    "0x12345"
    > myMultiply7.multiply.call(3)
    21

When called using ``sendTransaction`` the function call is executed via sending
a transaction.  This will cost ether to send and the call will be recorded
forever on the blockchain.  The return value of calls made in this manner is
the hash of the stransaction.

When called using ``call`` the function is executed locally in the EVM and the
return value of the function is returned with the function.  Calls made in this
manner are not recorded on the blockchain and thus, cannot modify the internal
state of the contract.  This manner of call is referred to as a **constant**
function call.  Calls made in this manner do not cost any ether.


You should use ``call`` if you are interested only in the return value and use
``sendTransaction`` if you only care about *side effects* on the state of the
contract.

In the example above, there are no side effects, therefore ``sendTransaction``
only burns gas and increases the entropy of the universe.


Contract metadata
================================================================================

In the previous sections we explained how you create a contract on the
blockchain. Now we will deal with the rest of the compiler output, the
**contract metadata** or contract info.

When interacting with a contract you did not create you might want
documentation or to look at the source code.  Contract authors are encouraged
to make such information available by registering it on the blockchain or
through a third party service, such as `EtherChain
<https://www.etherchain.org/contracts>`_. The ``admin`` API provides
convenience methods to fetch this bundle for any contract that chose to
register.

.. code:: js

    // get the contract info for contract address to do manual verification
    var info = admin.getContractInfo(address) // lookup, fetch, decode
    var source = info.source;
    var abiDef = info.abiDefinition


The underlying mechanism that makes this work is is that:

*  contract info is uploaded somewhere identifiable by a *URI* which
   is publicly accessible
*  anyone can find out what the *URI* is only knowing the contracts
   address

These requirements are achieved using a 2 step blockchain registry. The first
step registers the contract code (hash) with a content hash in a contract
called ``HashReg``. The second step registers a url with the content hash in
the ``UrlHint`` contract. These `registry contracts
<https://github.com/ethereum/go-ethereum/blob/develop/common/registrar/contracts.go>`__
were part of the Frontier release and have carried on into Homestead.

By using this scheme, it is sufficient to know a contract's address to look up the url and fetch the actual contract metadata info bundle.

So if you are a conscientious contract creator, the steps are the following:

1. Deploy the contract itself to the blockchain
2. Get the contract info json file.
3. Deploy contract info json file to any url of your choice
4. Register codehash ->content hash -> url

The JS API makes this process very easy by providing helpers. Call
``admin.register`` to extract info from the contract, write out its json
serialisation in the given file, calculates the content hash of the file and
finally registers this content hash to the contract's code hash. Once you
deployed that file to any url, you can use ``admin.registerUrl`` to register
the url with your content hash on the blockchain as well. (Note that in case a
fixed content addressed model is used as document store, the url-hint is no
longer necessary.)

.. code-block:: js

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


Testing contracts and transactions
================================================================================

Often you need to resort to a low level strategy of testing and debugging
contracts and transactions. This section introduces some debug tools and
practices you can use. In order to test contracts and transactions without
real-word consequences, you best test it on a private blockchain. This can be
achieved with configuring an alternative network id (select a unique integer)
and/or disable peers. It is recommended practice that for testing you use an
alternative data directory and ports so that you never even accidentally clash
with your live running node (assuming that runs using the defaults. Starting
your ``geth`` with in VM debug mode with profiling and highest logging
verbosity level is recommended:

.. code:: bash

    geth --datadir ~/dapps/testing/00/ --port 30310 --rpcport 8110 --networkid 4567890 --nodiscover --maxpeers 0 --vmdebug --verbosity 6 --pprof --pprofport 6110 console 2>> ~/dapp/testint/00/00.log

Before you can submit any transactions, you need set up your private test
chain. See :ref:`test-networks`.

.. code:: js

    // create account. will prompt for password
    personal.newAccount();
    // name your primary account, will often use it
    primary = eth.accounts[0];
    // check your balance (denominated in ether)
    balance = web3.fromWei(eth.getBalance(primary), "ether");

.. code:: js

    // assume an existing unlocked primary account
    primary = eth.accounts[0];

    // mine 10 blocks to generate ether

    // starting miner
    miner.start(4);
    // sleep for 10 blocks (this can take quite some time).
    admin.sleepBlocks(10);
    // then stop mining (just not to burn heat in vain)
    miner.stop();
    balance = web3.fromWei(eth.getBalance(primary), "ether");

After you create transactions, you can force process them with the following lines:

.. code:: js

    miner.start(1);
    admin.sleepBlocks(1);
    miner.stop();

You can check your pending transactions with:

.. code:: js

    // shows transaction pool
    txpool.status
    // number of pending txs
    eth.getBlockTransactionCount("pending");
    // print all pending txs
    eth.getBlock("pending", true).transactions

If you submitted contract creation transaction, you can check if the desired code actually got inserted in the current blockchain:

.. code:: js

    txhash = eth.sendTansaction({from:primary, data: code})
    //... mining
    contractaddress = eth.getTransactionReceipt(txhash);
    eth.getCode(contractaddress)

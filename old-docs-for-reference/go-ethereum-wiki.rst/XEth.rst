eXtended Ethereum API
=====================

***NOTE:** This documentation is out-of-date and in need of refresh
against current codebase*

General, easy to use, Ethereum query interface. This API allows you to
easily interface with Ethereum's state and their respective objects,
create transactions and directly evaluate contract code.

.. code:: go

    import "github.com/ethereum/go-ethereum/xeth"

Be aware that all methods return something. Nil isn't ever returned
unless explicitly specified.

Objects
~~~~~~~

-  ``XEth``: Top level query interface
-  ``World``: world object through which you can query Ethereum's state
   and objects.
-  ``Config``: config object through which you can query the ``Config``
   contract if available.
-  ``Object``: object which functions as a proxy for ``StateObject``.
   Returned by ``config``

Functions
~~~~~~~~~

-  ``New(ethchain.EthManager) *XEth``: instantiate a new ethpipe object.

``XEth`` Methods
~~~~~~~~~~~~~~~~

-  ``World() *world``: returns the world object through which you can
   query Ethereum's state.
-  ``Balance(address []byte) *Value``: returns the balance of the given
   ``address``.
-  ``Exists(address []byte) bool``: returns whether an object with the
   given ``address`` exists.
-  ``Nonce(address []byte) *uint64``: returns the the nonce of the given
   ``address``.
-  ``Block(hash []byte) *Block``: returns the given block by ``hash``.
-  ``Storage(address, storage []byte) *Value``: returns the given object
   by ``address``'s value given by the ``storage`` address.
-  ``ToAddress(privateKey []byte) []byte``: converts a private key to an
   Ethereum address.
-  ``Execute(address, data []byte, value, gas, price *Value) []byte``:
   Simulates an evaluation of the object's code given by the ``address``
   and returns the outcome.
-  ``ExecuteObject(object *Object, data []byte, value, gas, price *Value) []byte``:
   Similar to the above only takes an actual ``StateObject`` instead of
   an address.
-  ``Transact(key *KeyPair, address []byte, value, gas, price *Value, data []byte) ([]byte, error)``:
   creates a new transaction using the given ``key``.

``World`` Methods
~~~~~~~~~~~~~~~~~

-  ``State() *State``: returns the current state of the Ethereum
   ``world`` object.
-  ``Get(addres []byte) *StateObject``: returns the object given by the
   ``address``. Returns ``nil`` if no object associated with the
   ``address`` can be found.
-  ``Config() *config``
-  ``IsListening() bool``: returns whether the client is listening for
   connections.
-  ``IsMining() bool``: returns whether the client is mining.
-  ``Peers() *list.List``: returns the current connected peers.
-  ``Coinbase() *StateObject``: TODO

``Config`` Methods
~~~~~~~~~~~~~~~~~~

-  ``Get(name string) object``: returns the associated object given by
   the ``name``.
-  ``Exist() bool``: returns whether the config object exist in
   Ethereum's present state.

``Object`` Methods
~~~~~~~~~~~~~~~~~~

-  ``StorageString(str string) *Value``: returns the storage value given
   by the key as ``str`` (Note, right pads zero to length of 32).
-  ``Storage(addr []byte)``: return the storage value given by the key
   as ``address``.

Example
-------

.. code:: go

    import "github.com/ethereum/go-ethereum/xeth"

    xeth := xeth.New(ethereum)

    var addr, privy, recp, data []byte
    var object *ethstate.StateObject
    var key *ethcrypto.KeyPair

    world := xeth.World()
    world.Get(addr)
    world.Coinbase()
    world.IsMining()
    world.IsListening()
    world.State()
    peers := world.Peers()
    peers.Len()

    // Shortcut functions
    xeth.Balance(addr)
    xeth.Nonce(addr)
    xeth.Block(addr)
    xeth.Storage(addr, addr)
    xeth.ToAddress(privy)
    // Doesn't change state
    xeth.Execute(addr, nil, Val(0), Val(1000000), Val(10))
    // Doesn't change state
    xeth.ExecuteObject(object, nil, Val(0), Val(1000000), Val(10))

    conf := world.Config()
    namereg := conf.Get("NameReg")
    namereg.Storage(addr)

    var err error
    // Transact
    tx_hash, err = xeth.Transact(key, recp, ethutil.NewValue(0), ethutil.NewValue(0), ethutil.NewValue(0), nil)
    if err != nil {
        t.Error(err)
    }
    // Create
    contract_addr, err = xeth.Transact(key, nil, ethutil.NewValue(0), ethutil.NewValue(0), ethutil.NewValue(0), data)
    if err != nil {
        t.Error(err)
    }

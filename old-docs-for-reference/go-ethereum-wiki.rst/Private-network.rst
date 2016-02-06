Setting up a private network using Geth is relatively easy and
straightforward. Geth allows you to operate on multiple chains, although
not at the same time. It does so by allowing different genesis block to
be inserted in to the database. The only thing you need to do when
switching between chains is give up the path to the genesis block file
(in a later version of Geth a hash will suffice when it has previously
been imported).

To set up and import a new genesis block please fetch an
`example <http://jev.io/example_genesis.json>`__ genesis block. You are
free to add any accounts to this block by inserting it within the
``alloc`` object:

::

    "alloc": {
        "0xaddress": { "balance": "amount denoted in Wei" }
    }

Now start Geth with the genesis flag pointing to the genesis file
``geth --genesis /path/to/file``. This will import and set the canonical
genesis block for your chain or switches to a different previous imports
chain.

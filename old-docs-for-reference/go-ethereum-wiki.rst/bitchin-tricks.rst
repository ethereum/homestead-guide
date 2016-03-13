Bitchin' tricks
===============

Geth
~~~~

General
^^^^^^^

-  My [STRIKEOUT:shit] client doesn't work! :fu:

::

    git pull

Mining
^^^^^^

-  I only want to mine when there are transactions!

.. code:: javascript

    var mining_threads = 1

    function checkWork() {
        if (eth.getBlock("pending").transactions.length > 0) {
            if (eth.mining) return;
            console.log("== Pending transactions! Mining...");
            miner.start(mining_threads);
        } else {
            miner.stop(0);  // This param means nothing
            console.log("== No transactions! Mining stopped.");
        }
    }

    eth.filter("latest", function(err, block) { checkWork(); });
    eth.filter("pending", function(err, block) { checkWork(); });

    checkWork();

Curtesy @chfast

Quick scripts
^^^^^^^^^^^^^

-  I want to get some data out without running a node!

::

    $ geth --exec "eth.accounts" console 2>/dev/null

    ["0x0000000000000000000000000000000000000000"]

-  I want to get some data out without RPC magic!

::

    $ geth --exec "eth.accounts" attach

    ["0x0000000000000000000000000000000000000000"]

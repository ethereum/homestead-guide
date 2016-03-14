.. _Ethereum Clients:

################################################################################
Ethereum Clients
################################################################################

Why are there multiple Ethereum clients?
--------------------------------------------------------------------------------

The Ethereum clients are very analogous to a Java VM or .NET runtime.

They enable you to execute "Ethereum programs" on your computer.  They are
implemented to a written specification (the "Yellow Paper") and by design
are interoperable and somewhat "commodity".

From the earlier days of the project there have been multiple interoperable
client implementations across a range of different operating systems.  That
client diversity is a huge win for the eco-system as a whole.
It lets us verify that the protocol is unambiguous.  It keeps the door
open for new innovation.  It keeps us all honest.  However, it can be
very confusing for end-users, because there is no universal
"Ethereum Installer" for them to use.

As we enter the Homestead phase, the Go client is very, very dominant, but
it hasn't always been that way, and won't necessarily be that way in the
future.

Only a subset of the clients have released versions which are Homestead
compatible.  There are links to those releases in the right-hand column of
the table below.   The clients without links are all working on getting
Homestead-compatible versions released.   Keep checking back.   We will
add links to them here as they are released.

+------------------------+------------+------------------------+----------------------------------+
| Client                 | Language   | Developers             | Homestead Release                |
+========================+============+========================+==================================+
| `mist (dapp browser)`_ | Javascript | `Ethereum Foundation`_ | `mist-v0.5.2`_                   |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`go-ethereum`     | Go         | `Ethereum Foundation`_ | `geth-v1.3.5`_                   |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`cpp-ethereum`    | C++        | `Ethereum Foundation`_ | `eth-v1.2.2`_                    |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`pyethapp`        | Python     | `Ethereum Foundation`_ | v1.2.0 release imminent          |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`ethereumjs-lib`  | Javascript | `Ethereum Foundation`_ | `ethereumjs-lib-v3.0.0`_         |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`Ethereum\(J\)`   | Java       | `ConsenSys`_           | `ethereumJ-v1.2.0-homestead-RC`_ |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`ethereumH`       | Haskell    | `ConsenSys`_           | not available yet                |
+------------------------+------------+------------------------+----------------------------------+
| :ref:`Parity`          | Rust       | `Ethcore`_             | v1.0.0 release imminent          |
+------------------------+------------+------------------------+----------------------------------+

.. _mist (dapp browser): http://github.com/ethereum/mist/

.. _Ethereum Foundation: https://ethereum.org/foundation
.. _ConsenSys: https://consensys.net/
.. _Ethcore: https://ethcore.io/

.. _mist-v0.5.2: https://github.com/ethereum/mist/releases/tag/0.5.2
.. _geth-v1.3.5: https://github.com/ethereum/go-ethereum/releases/tag/v1.3.5
.. _eth-v1.2.2: https://github.com/ethereum/webthree-umbrella/releases/tag/v1.2.2
.. _ethereumjs-lib-v3.0.0: https://github.com/ethereumjs/ethereumjs-lib/tree/v3.0.0
.. _ethereumJ-v1.2.0-homestead-RC: https://github.com/ethereum/ethereumj/releases/tag/1.2.0-homestead-RC


Meet the clients
--------------------------------------------------------------------------------

.. toctree::
   :maxdepth: 2

   cpp-ethereum/index.rst
   go-ethereum/go-ethereum.rst
   pyethapp/pyethapp.rst
   ethereumjs-lib/ethereumjs-lib.rst
   ethereumj/ethereumj.rst
   ethereumh/ethereumh.rst
   parity/parity.rst

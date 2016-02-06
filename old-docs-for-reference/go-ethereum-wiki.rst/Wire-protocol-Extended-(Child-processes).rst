Ethereum Child processes allow any node to connect to an existing node
and share it's parent process to handle all network communication and
data persisting. This will allow for multiple Ethereum light nodes on
the same host with full access to the block chain through the parent
process.

Message Type
~~~~~~~~~~~~

Intercom messages range from 0x30 - X all messages are specified as

Get block
^^^^^^^^^

-  ``[0x30, [block hash]]``
-  Retrieve the block by hash or empty if block couldn't be found

Block
^^^^^

-  ``[0x31, [block]]``
-  Returns the given block as a reply on ``get block``.

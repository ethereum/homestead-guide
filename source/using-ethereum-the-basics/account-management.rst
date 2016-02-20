********************************************************************************
Account Management
********************************************************************************
What are accounts?
================================================================================
From the Introduction, we know that, “accounts are a central part of the network and are an essential part of any transaction or contract”.

In Ethereum, there are two types of accounts: **Externally Owned accounts** and **Contract accounts**. We will encounter Contract accounts later. For now, we’ll focus on Externally Owned accounts, which will be referred to simply as **accounts**.

Keyfiles
================================================================================
Every account is defined by a pair of keys, a private key and an address (or public key). Every private key/address pair exists as a single **keyfile**. Keyfiles are JSON text files which you can open and view in any text editor. The critical component of the keyfile, your account’s private key, is always encrypted, and it is encrypted with the password you enter when you create the account. Keyfiles are found in the ``keystore`` subdirectory of your Ethereum node’s data directory. Make sure you backup your keyfiles regularly! See the section `Backup and restore of accounts`_ for more information.

The newest format of the keyfiles is: ``UTC--<created_at UTC ISO8601>-<address hex>``. The order of accounts when listing, is lexicographic, but as a consequence of the timestamp format, it is actually order of creation.

It is safe to transfer the entire directory or the individual keyfiles therein between ethereum nodes. Note that in case you are adding keyfiles to your node from a different node, the order of accounts may change. So make sure you do not rely or change the index in your scripts or code snippets.

Creating an account
================================================================================
**WARNING:** Remember your password.

If you lose the password you use to encrypt your account, you will not be able to access that account. Repeat: It is NOT possible to access your account without a password and there is no *forgot my password* option here. Do not forget it.


Using the Console
--------------------------------------------------------------------------------
(Already done. Move here?)

Using EthKey
--------------------------------------------------------------------------------
TODO

Using Mist
--------------------------------------------------------------------------------
Just link into Homestead website where the MIST wallet will be described?

Using RPC
--------------------------------------------------------------------------------
TODO

Using the ``geth account new`` command
--------------------------------------------------------------------------------
Once you have the geth client installed, creating an account is merely a case of executing the ``geth account new`` command in a terminal.

Note that you do not have to run the geth client or sync up with the blockchain to use the ``geth account`` command.

::

	$ geth account new
	Your new account is locked with a password. Please give a password. Do not forget this password.
	Passphrase:
	Repeat Passphrase:
	Address: {168bc315a2ee09042d83d7c5811b533620531f67}

For non-interactive use you supply a plaintext password file as argument to the ``--password`` flag. The data in the file consists of the raw characters of the password, followed by a single newline.
Note, this is meant to be used for testing only, it is a bad idea to save your password to file or expose it in any other way.

::

	$ geth --password /path/to/password account new

To list all the accounts with keyfiles currently in your ``keystore`` folder use the ``list`` subcommand of the ``geth account`` command:

::

	$ geth account list
	account #0: {a94f5374fce5edbc8e2a8697c15331677e6ebf0b}
	account #1: {c385233b188811c9f355d4caec14df86d6248235}
	account #2: {7f444580bfef4b9bc7e14eb7fb2a029336b07c9d}


By importing a private key
--------------------------------------------------------------------------------
::

	geth account import /path/to/<keyfile>

Imports an unencrypted private key from the plain text file ``<keyfile>`` and creates a new account and prints the address.
The keyfile is assumed to contain an unencrypted private key as canonical EC raw bytes encoded into hex.
The account is saved in encrypted format, you are prompted for a passphrase. You must remember this passphrase to unlock your account in the future.

An example where the data directory is specified. If the ``--datadir`` flag is not used, the new account will be created in the default data directory.

::

	$ geth --datadir /someOtherEthDataDir  account import ./key.prv
	The new account will be encrypted with a passphrase.
	Please enter a passphrase now.
	Passphrase:
	Repeat Passphrase:
	Address: {7f444580bfef4b9bc7e14eb7fb2a029336b07c9d}

For non-interactive use the passphrase can be specified with the ``--password`` flag:

::

	geth --password <passwordfile> account import <keyfile>


**Note:** Since you can directly copy your encrypted accounts to another ethereum instance, this import/export mechanism is not needed when you transfer an account between nodes.

**Warning:** When you copy keys into an existing node's ``keystore``, the order of accounts you are used to may change. Therefore you make sure you either do not rely on the account order or double-check and update the indexes used in your scripts.

**Warning:** If you use the ``--password`` flag with a password file, best to make sure the file is not readable or even listable for anyone but you. You achieve this with:

::

	touch /path/to/password
	chmod 700 /path/to/password
	cat > /path/to/password
	>I type my pass

Updating an existing account
================================================================================
You can update an existing account on the command line with the ``update`` subcommand with the account address or index as parameter.

::

	geth account update b0047c606f3af7392e073ed13253f8f4710b08b6
	geth account update 2

For example:

::

	$ geth account update a94f5374fce5edbc8e2a8697c15331677e6ebf0b
	Unlocking account a94f5374fce5edbc8e2a8697c15331677e6ebf0b | Attempt 1/3
	Passphrase:
	0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b
	account 'a94f5374fce5edbc8e2a8697c15331677e6ebf0b' unlocked.
	Please give a new password. Do not forget this password.
	Passphrase:
	Repeat Passphrase:
	0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b

The account is saved in the newest version in encrypted format, you are prompted for a passphrase to unlock the account and another to save the updated file.

This same command can therefore be used to migrate an account of a deprecated format to the newest format or change the password for an account.

For non-interactive use the passphrase can be specified with the ``--password`` flag:

::

	geth --password <passwordfile> account new

Since only one password can be given, only format update can be performed, changing your password is only possible interactively.

**Note:** account update has the side effect that the order of your accounts changes.
After a successful update, all previous formats/versions of that same key will be removed!

.. _`Backup and restore of accounts`:

Backup and restore of accounts
================================================================================
You must have an account’s keyfile to be able to send any transaction from that account. Keyfiles are found in the keystore subdirectory of your Ethereum node’s data directory. The default data directory locations are platform specific:

- Windows: ``C:\Users\username\%appdata%\Roaming\Ethereum\keystore``
- Linux: ``~/.ethereum/keystore``
- Mac: ``~/Library/Ethereum/keystore``

To backup your keyfiles (accounts), copy either the individual keyfiles within the ``keystore`` subdirectory or copy the entire ``keystore`` folder.

To restore your keyfiles (accounts), copy the keyfiles back into the ``keystore`` subdirectory, where they were originally.

**This is IMPORTANT:** Accessing an account
--------------------------------------------------------------------------------
For anyone to send transactions from an account, including sending ether of course, they must have BOTH the keyfile and the password. So be absolutely sure to have a copy of your keyfile AND remember the password for that keyfile, and store them both as securely as possible. There are no escape routes here; lose the keyfile or forget your password and all your ether is gone.




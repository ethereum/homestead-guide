Managing accounts
=================

**WARNING** Remember your password.

If you lose the password you use to encrypt your account, you will not
be able to access that account. Repeat: It is NOT possible to access
your account without a password and there is no *forgot my password*
option here. Do not forget it.

**Note**: the key file name naming convention changed as of ``0.9.36``.
This document is meant to reflect accurate information on accounts as
used by the frontier release.

The Ethereum CLI ``geth`` provides account management via the
``account`` subcommand:

::

    account command [arguments...]

Manage accounts lets you create new accounts, list all existing
accounts, import a private key into a new account, migrate to newest key
format and change your password.

It supports interactive mode, when you are prompted for password as well
as non-interactive mode where passwords are supplied via a given
password file. Non-interactive mode is only meant for scripted use on
test networks or known safe environments.

Make sure you remember the password you gave when creating a new account
(with new, update or import). Without it you are not able to unlock your
account.

Note that exporting your key in unencrypted format is NOT supported.

Keys are stored under ``<DATADIR>/keystore``. Make sure you backup your
keys regularly! See `DATADIR backup &
restore <https://github.com/ethereum/go-ethereum/wiki/Backup-&-restore>`__
for more information. The newest format of the keyfiles is:
``UTC--<created_at UTC ISO8601>-<address hex>``. The order of accounts
when listing, is lexicographic, but as a consequence of the timestamp
format, it is actually order of creation

It is safe to transfer the entire directory or the individual keys
therein between Ethereum nodes. Note that in case you are adding keys to
your node from a different node, the order of accounts may change. So
make sure you do not rely or change the index in your scripts or code
snippets.

And finally. **DO NOT FORGET YOUR PASSWORD**

::

    SUBCOMMANDS:

            list    print account addresses
            new     create a new account
            update  update an existing account
            import  import a private key into a new account


You can get info about further subcommands by
``geth account help <subcommand>``

Accounts can also be managed via the `Javascript
Console <https://github.com/ethereum/go-ethereum/wiki/JavaScript-Console>`__

Examples
--------

Interactive use
~~~~~~~~~~~~~~~

creating an account
^^^^^^^^^^^^^^^^^^^

::

    $ geth account new
    Your new account is locked with a password. Please give a password. Do not forget this password.
    Passphrase:
    Repeat Passphrase:
    Address: {168bc315a2ee09042d83d7c5811b533620531f67}

Listing accounts
^^^^^^^^^^^^^^^^

::

    $ geth account list
    Account #0: {a94f5374fce5edbc8e2a8697c15331677e6ebf0b}
    Account #1: {c385233b188811c9f355d4caec14df86d6248235}
    Account #2: {7f444580bfef4b9bc7e14eb7fb2a029336b07c9d}

Import private key
^^^^^^^^^^^^^^^^^^

::

    $ geth --datadir /someOtherEthDataDir  account import ./key.prv
    The new account will be encrypted with a passphrase.
    Please enter a passphrase now.
    Passphrase:
    Repeat Passphrase:
    Address: {7f444580bfef4b9bc7e14eb7fb2a029336b07c9d}

Account update
^^^^^^^^^^^^^^

::

    $ geth account update a94f5374fce5edbc8e2a8697c15331677e6ebf0b
    Unlocking account a94f5374fce5edbc8e2a8697c15331677e6ebf0b | Attempt 1/3
    Passphrase:
    0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b
    Account 'a94f5374fce5edbc8e2a8697c15331677e6ebf0b' unlocked.
    Please give a new password. Do not forget this password.
    Passphrase:
    Repeat Passphrase:
    0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b

Non-interactive use
~~~~~~~~~~~~~~~~~~~

You supply a plaintext password file as argument to the ``--password``
flag. The data in the file consists of the raw characters of the
password, followed by a single newline.

**Note**: Supplying the password directly as part of the command line is
not recommended, but you can always use shell trickery to get round this
restriction.

::

    $ geth --password /path/to/password account new

    $ geth --password /path/to/password account update b0047c606f3af7392e073ed13253f8f4710b08b6

    $ geth account list

    $ geth --datadir /someOtherEthDataDir --password /path/to/anotherpassword account import ./key.prv

Creating accounts
=================

Creating a new account
----------------------

::

    geth account new

Creates a new account and prints the address.

On the console, use:

::

    > personal.newAccount("passphrase")

The account is saved in encrypted format. You **must** remember this
passphrase to unlock your account in the future.

For non-interactive use the passphrase can be specified with the
``--password`` flag:

::

    geth --password <passwordfile> account new

Note, this is meant to be used for testing only, it is a bad idea to
save your password to file or expose in any other way.

Creating an account by importing a private key
----------------------------------------------

::

        geth account import <keyfile>

Imports an unencrypted private key from ``<keyfile>`` and creates a new
account and prints the address.

The keyfile is assumed to contain an unencrypted private key as
canonical EC raw bytes encoded into hex.

The account is saved in encrypted format, you are prompted for a
passphrase.

You must remember this passphrase to unlock your account in the future.

For non-interactive use the passphrase can be specified with the
``--password`` flag:

::

    geth --password <passwordfile> account import <keyfile>

**Note**: Since you can directly copy your encrypted accounts to another
Ethereum instance, this import/export mechanism is not needed when you
transfer an account between nodes.

**Warning:** when you copy keys into an existing node's keystore, the
order of accounts you are used to may change. Therefore you make sure
you either do not rely on the account order or doublecheck and update
the indexes used in your scripts.

**Warning:** If you use the password flag with a password file, best to
make sure the file is not readable or even listable for anyone but you.
You achieve this with:

::

    touch /path/to/password
    chmod 700 /path/to/password
    cat > /path/to/password
    >I type my pass here^D

Updating an existing account
----------------------------

You can update an existing account on the command line with the
``update`` subcommand with the account address or index as parameter.

::

    geth account update b0047c606f3af7392e073ed13253f8f4710b08b6
    geth account update 2

The account is saved in the newest version in encrypted format, you are
prompted for a passphrase to unlock the account and another to save the
updated file.

This same command can therefore be used to migrate an account of a
deprecated format to the newest format or change the password for an
account.

For non-interactive use the passphrase can be specified with the
``--password`` flag:

::

    geth --password <passwordfile> account new

Since only one password can be given, only format update can be
performed, changing your password is only possible interactively.

**Note**: Account update has the a side effect that the order of your
accounts changes.

After a successful update, all previous formats/versions of that same
key will be removed!

Importing your presale wallet
=============================

Importing your presale wallet is very easy. If you remember your
password that is:

::

    geth wallet import /path/to/my/presale.wallet

will prompt for your password and imports your ether presale account. It
can be used non-interactively with the --password option taking a
passwordfile as argument containing the wallet password in cleartext.

Listing accounts and checking balances
======================================

Listing your current accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the command line, call the CLI with:

::

    $ geth account list
    Account #0: {d1ade25ccd3d550a7eb532ac759cac7be09c2719}
    Account #1: {da65665fc30803cb1fb7e6d86691e20b1826dee0}
    Account #2: {e470b1a7d2c9c5c6f03bbaa8fa20db6d404a0c32}
    Account #3: {f4dd5c3794f1fd0cdc0327a83aa472609c806e99}

to list your accounts in order of creation.

**Note**: This order can change if you copy keyfiles from other nodes,
so make sure you either do not rely on indexes or make sure if you copy
keys you check and update your account indexes in your scripts.

When using the console:

::

    > eth.accounts
    ['0x407d73d8a49eeb85d32cf465507dd71d507100c1']

or via RPC:

::

    # Request
    $ curl -X POST --data '{"jsonrpc":"2.0","method":"eth_accounts","params":[],"id":1} http://127.0.0.1:8545'

    # Result
    {
      "id":1,
      "jsonrpc": "2.0",
      "result": ["0x407d73d8a49eeb85d32cf465507dd71d507100c1"]
    }

If you want to use an account non-interactively, you need to unlock it.
You can do this on the command line with the ``--unlock`` option which
takes a whitespace separated list of accounts (in hex or index) as
argument so you can unlock the accounts programmatically for one
session. This is useful if you want to use your account from dapps via
RPC. ``--unlock`` will unlock the first account. This is useful when you
created your account programmatically, you do not need to know the
actual account to unlock it.

Unlocking one account:

::

    geth --password <(echo this is not secret!) account new
    geth --password <(echo this is not secret!) --unlock primary --rpccorsdomain localhost --verbosity 6 2>> geth.log

Instead of the account address, you can use integer indexes which refers
to the address position in the account listing (and corresponds to order
of creation)

The command line allows you to unlock multiple accounts. In this case
the argument to unlock is a whitespace delimited list of accounts
addresses or indexes.

::

    geth --unlock "0x407d73d8a49eeb85d32cf465507dd71d507100c1 0 5 e470b1a7d2c9c5c6f03bbaa8fa20db6d404a0c32"

If this construction is used non-interactively, your password file will
need to contain the respective passwords for the accounts in question,
one per line.

On the console you can also unlock accounts (one at a time).

::

    personal.unlockAccount(address, "password")

Note that we do NOT recommend using the password argument here, since
the console history is logged, so you may compromise your account. You
have been warned.

Checking account balances
~~~~~~~~~~~~~~~~~~~~~~~~~

To check your the etherbase account balance:

::

    > web3.fromWei(eth.getBalance(eth.coinbase), "ether")
    6.5

Print all balances with a JavaScript function:

::

    function checkAllBalances() {
    var i =0;
    eth.accounts.forEach( function(e){
        console.log("  eth.accounts["+i+"]: " +  e + " \tbalance: " + web3.fromWei(eth.getBalance(e), "ether") + " ether");
    i++;
    })
    };

That can then be executed with:

::

    > checkAllBalances();
      eth.accounts[0]: 0xd1ade25ccd3d550a7eb532ac759cac7be09c2719   balance: 63.11848 ether
      eth.accounts[1]: 0xda65665fc30803cb1fb7e6d86691e20b1826dee0   balance: 0 ether
      eth.accounts[2]: 0xe470b1a7d2c9c5c6f03bbaa8fa20db6d404a0c32   balance: 1 ether
      eth.accounts[3]: 0xf4dd5c3794f1fd0cdc0327a83aa472609c806e99   balance: 6 ether

Since this function will disappear after restarting geth, it can be
helpful to store commonly used functions to be recalled later. The
`loadScript <https://github.com/ethereum/go-ethereum/wiki/JavaScript-Console#loadscript>`__
function makes this very easy.

First, save the ``checkAllBalances()`` function definition to a file on
your computer. For example, ``/Users/username/gethload.js``. Then load
the file from the interactive console:

::

    > loadScript("/Users/username/gethload.js")
    true

The file will modify your JavaScript environment as if you has typed the
commands manually. Feel free to experiment!

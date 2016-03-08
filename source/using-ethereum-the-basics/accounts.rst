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
**WARNING:** Remember your passwords and backup your keyfiles.

For anyone to send transactions from an account, including sending ether, they must have BOTH the keyfile and the password. Be absolutely sure to have a copy of your keyfile AND remember the password for that keyfile, and store them both as securely as possible. There are no escape routes here; lose the keyfile or forget your password and all your ether is gone. It is NOT possible to access your account without a password and there is no *forgot my password* option here. Do not forget it.

Using ``geth account new``
--------------------------------------------------------------------------------
Once you have the geth client installed, creating an account is merely a case of executing the ``geth account new`` command in a terminal.

Note that you do not have to run the geth client or sync up with the blockchain to use the ``geth account`` command.

.. code-block:: Bash

  $ geth account new
    
    Your new account is locked with a password. Please give a password. Do not forget this password.
    Passphrase:
    Repeat Passphrase:
    Address: {168bc315a2ee09042d83d7c5811b533620531f67}

For non-interactive use you supply a plaintext password file as argument to the ``--password`` flag. The data in the file consists of the raw characters of the password, followed by a single newline.
Note, this is meant to be used for testing only, it is a bad idea to save your password to file or expose it in any other way.

.. code-block:: Bash

  $ geth --password /path/to/password account new

To list all the accounts with keyfiles currently in your ``keystore`` folder use the ``list`` subcommand of the ``geth account`` command:

.. code-block:: Bash

  $ geth account list

  account #0: {a94f5374fce5edbc8e2a8697c15331677e6ebf0b}
  account #1: {c385233b188811c9f355d4caec14df86d6248235}
  account #2: {7f444580bfef4b9bc7e14eb7fb2a029336b07c9d}

Using geth console
--------------------------------------------------------------------------------
In order to create a new account using geth, we must first start geth in console mode: 

.. code-block:: Bash

  > geth console 2>> file_to_log_output
  instance: Geth/v1.4.0-unstable/linux/go1.5.1
  coinbase: coinbase: [object Object]
  at block: 865174 (Mon, 18 Jan 2016 02:58:53 GMT)
  datadir: /home/USERNAME/.ethereum

The console allows you to interact with your local node by issuing commands. For example, try the command to list your accounts:

.. code-block:: Javascript

  > eth.accounts

  {
  code: -32000,
  message: "no keys in store"
  }

This shows that you have no accounts. So let's create an account:

.. code-block:: Javascript

  > personal.newAccount()
  Passphrase: 
  Repeat passphrase: 
  "0xb2f69ddf70297958e582a0cc98bce43294f1007d"

Remember to use a strong and randomly generated password. We just created our first account. If we try to list our accounts again we can see our new account: 

.. code-block:: Javascript

  > eth.accounts
  ["0xb2f69ddf70297958e582a0cc98bce43294f1007d"]

Using EthKey
--------------------------------------------------------------------------------
ethkey is a CLI tool that allows you to interact with the Ethereum wallet. With it you can list, inspect, create, delete and modify keys and inspect, create and sign transactions.

We'll assume you have not yet run a client such as eth or anything in the Aleth series of clients. If you have, you should skip this section.
To create a wallet, run ethkey with the createwallet command:

.. code-block:: Bash

  > ethkey createwallet

Please enter a MASTER passphrase to protect your key store (make it strong!):
You'll be asked for a "master" passphrase. This protects your privacy and acts as a default password for any keys. You'll need to confirm it by entering the same text again.

We can list the keys within the wallet simply by using the list command:

.. code-block:: Bash

  > ethkey list
  
  No keys found.

We haven't yet created any keys, and it's telling us so! Let's create one.

One of the nice things about Ethereum is that creating a key is tantamount to creating an account. You don't need to tell anybody else you're doing it, you don't even need to be connected to the Internet. Of course your new account will not contain any Ether. But it'll be yours and you can be certain that without your key and your password, nobody else can ever access it.
To create a key, we use the new command. To use it we must pass a name - this is the name we'll give to this account in the wallet. Let's call it "test":

.. code-block:: Bash

  > ethkey new test

Enter a passphrase  with which to secure this account (or nothing to use the master passphrase):
It will prompt you to enter a passphrase to protect this key. If you just press enter, it'll use the default "master" passphrase. Typically this means you won't need to enter the passphrase for the key when you want to use the account (since it remembers the master passphrase). In general, you should try to use a different passphrase for each key since it prevents one compromised passphrase from giving access to other accounts. However, out of convenience you might decide that for low-security accounts to use the same passphrase.

Here, let's give it the incredibly imaginitive passphrase of 123.
Once you enter a passphrase, it'll ask you to confirm it by entering again. Enter 123 a second time.
Because you gave it its own passphrase, it'll also ask you to provide a hint for this password which will be displayed to you whenever it asks you to enter it. The hint is stored in the wallet and is itself protected by the master passphrase. Enter the truly awful hint of 321 backwards.

.. code-block:: Bash

  > ethkey new test
  
  Enter a passphrase with which to secure this account (or nothing to use the master passphrase): 
  Please confirm the passphrase by entering it again: 
  Enter a hint to help you remember this passphrase: 321 backwards
  Created key 055dde03-47ff-dded-8950-0fe39b1fa101
    Name: test
    Password hint: 321 backwards
    ICAP: XE472EVKU3CGMJF2YQ0J9RO1Y90BC0LDFZ
    Raw hex: 0092e965928626f8880629cec353d3fd7ca5974f

All normal (aka direct) ICAP addresses begin with XE so you should be able to recognise them easily. Notice also that the key has another identifier after Created key. This is known as the UUID. This is a unique identifer for the key that has absolutely nothing to do with the account itself. Knowing it does nothing to help an attacker discover who you are on the network. It also happens to be the filename for the key, which you can find in either ~/.web3/keys (Mac or Linux) or $HOME/AppData/Web3/keys (Windows).
Now let's make sure it worked properly by listing the keys in the wallet:

.. code-block:: Bash

  > ethkey list
  055dde03-47ff-dded-8950-0fe39b1fa101 0092e965… XE472EVKU3CGMJF2YQ0J9RO1Y90BC0LDFZ  test

It reports one key on each line (for a total of one key here). In this case our key is stored in a file 055dde... and has an ICAP address beginning XE472EVK.... Not especially easy things to remember so rather helpful that it has its proper name, test, too.

Using Mist
--------------------------------------------------------------------------------
Just link into Homestead website where the MIST wallet will be described?

Updating an account
================================================================================
You are able to upgrade your keyfile to the latest keyfile format and/or upgrade your keyfile password. 

Using geth
--------------------------------------------------------------------------------
You can update an existing account on the command line with the ``update`` subcommand with the account address or index as parameter.

.. code-block:: Bash

  geth account update b0047c606f3af7392e073ed13253f8f4710b08b6

or

.. code-block:: Bash

  geth account update 2

For example:

.. code-block:: Bash

  $ geth account update a94f5374fce5edbc8e2a8697c15331677e6ebf0b

  Unlocking account a94f5374fce5edbc8e2a8697c15331677e6ebf0b | Attempt 1/3
  Passphrase:
  0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b
  account 'a94f5374fce5edbc8e2a8697c15331677e6ebf0b' unlocked.
  Please give a new password. Do not forget this password.
  Passphrase:
  Repeat Passphrase:
  0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b

The account is saved in the newest version in encrypted format, you are prompted for a passphrase to unlock the account and another to save the updated file.This same command can be used to migrate an account of a deprecated format to the newest format or change the password for an account.

For non-interactive use the passphrase can be specified with the ``--password`` flag:

.. code-block:: Bash

  geth --password <passwordfile> account new

Since only one password can be given, only format update can be performed, changing your password is only possible interactively.

**Note:** account update has the side effect that the order of your accounts changes.
After a successful update, all previous formats/versions of that same key will be removed!

.. _`Backup and restore of accounts`:

Backup and restore accounts
================================================================================

Manual backup/restore
--------------------------------------------------------------------------------
You must have an account’s keyfile to be able to send any transaction from that account. Keyfiles are found in the keystore subdirectory of your Ethereum node’s data directory. The default data directory locations are platform specific:

- Windows: ``C:\Users\username\%appdata%\Roaming\Ethereum\keystore``
- Linux: ``~/.ethereum/keystore``
- Mac: ``~/Library/Ethereum/keystore``

To backup your keyfiles (accounts), copy either the individual keyfiles within the ``keystore`` subdirectory or copy the entire ``keystore`` folder.

To restore your keyfiles (accounts), copy the keyfiles back into the ``keystore`` subdirectory, where they were originally.

Importing an unencrypted private key
--------------------------------------------------------------------------------

.. code-block:: Bash

  geth account import /path/to/<keyfile>

This command imports an unencrypted private key from the plain text file ``<keyfile>`` and creates a new account and prints the address.
The keyfile is assumed to contain an unencrypted private key as canonical EC raw bytes encoded into hex.
The account is saved in encrypted format, you are prompted for a passphrase. You must remember this passphrase to unlock your account in the future.

An example where the data directory is specified. If the ``--datadir`` flag is not used, the new account will be created in the default data directory.

.. code-block:: Bash

  $ geth --datadir /someOtherEthDataDir  account import ./key.prv
  The new account will be encrypted with a passphrase.
  Please enter a passphrase now.
  Passphrase:
  Repeat Passphrase:
  Address: {7f444580bfef4b9bc7e14eb7fb2a029336b07c9d}

For non-interactive use the passphrase can be specified with the ``--password`` flag:

.. code-block:: Bash
  
  geth --password <passwordfile> account import <keyfile>


**Note:** Since you can directly copy your encrypted accounts to another ethereum instance, this import/export mechanism is not needed when you transfer an account between nodes.

**Warning:** When you copy keys into an existing node's ``keystore``, the order of accounts you are used to may change. Therefore you make sure you either do not rely on the account order or double-check and update the indexes used in your scripts.

**Warning:** If you use the ``--password`` flag with a password file, make sure the file is not readable or even listable for anyone but you.

For example, you can achieve this in Mac/Linux systems with:

.. code-block:: Bash
  
  touch /path/to/password
  chmod 700 /path/to/password
  cat > /path/to/password
  >I type my pass


Online Wallets, Paper Wallets, and Cold Storage
================================================================================

TODO
  This is here just a dumping ground of links and notes
  Please move this over in a listing form to ecosystem

  Keep examples here, maybe explain paranoid practices, list dangers

* Mist Wallet
    * https://github.com/ethereum/mist/releases
    * https://blog.ethereum.org/2015/09/16/ethereum-wallet-developer-preview/
	* How to easily set up the Ethereum Mist wallet! *Tutorial* – Tommy Economics – https://www.youtube.com/watch?v=Z6lE0Ctaeqs
* Kryptokit Jaxx
    * http://jaxx.io/
    * http://favs.pw/first-ethereum-mobile-app-released/#.VsHn_PGPL5c
* Etherwall
    * website: http://www.etherwall.com/
    * source: https://github.com/almindor/etherwall
* MyEtherWallet
    * https://www.myetherwallet.com/
    * source https://github.com/kvhnuke/etherwallet/
    * http://sebfor.com/myetherwallet-chrome-extension-release/
* cold storage
    * https://www.reddit.com/r/ethereum/comments/45uvmy/offline_cold_storage_question/offline_cold_storage_question
* hardware wallet
    * https://www.reddit.com/r/ethereum/comments/45siaq/hardware_wallet/
    * https://www.reddit.com/r/ethereum/comments/4521o4/crowdfunding_ethereum_hardware_cold_storage_wallet/
* brain wallet
	* brain wallets are not safe, do not use them. https://www.reddit.com/r/ethereum/comments/45y8m7/brain_wallets_are_now_generally_shunned_by/
	* Extreme caution with brain wallets. Read the recent controversy: https://reddit.com/r/ethereum/comments/43fhb5/brainwallets vs http://blog.ether.camp/post/138376049438/why-brain-wallet-is-the-best
* Misc
	* http://ethereum.stackexchange.com/questions/1239/what-is-the-recommended-way-to-safely-store-ether
	* http://www.fastcompany.com/3056651/researchers-find-a-crack-that-drains-supposedly-secure-bitcoin-wallets
	* http://sebfor.com/how-to-buy-and-store-ether/
	* https://github.com/ethereum/pyethsaletool/blob/master/README.md
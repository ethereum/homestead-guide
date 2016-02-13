********************************************************************************
Creating An Account
********************************************************************************
In order to create a new account using geth. We must first start the geth in console mode. 

.. code-block:: Bash

  > geth console 2>> file_to_log_output
  instance: Geth/v1.4.0-unstable/linux/go1.5.1
  coinbase: coinbase: [object Object]
  at block: 865174 (Mon, 18 Jan 2016 02:58:53 GMT)
  datadir: /home/USERNAME/.ethereum

Using the Console
================================================================================
The console allows you to interact with your local node by issueing commands. For example try the command to list your accounts


.. code-block:: Javascript

  > eth.accounts

  {
  code: -32000,
  message: "no keys in store"
  }

This shows that you have no accounts. So lets create an account.

.. code-block:: Javascript

  > personal.newAccount()
  Passphrase: 
  Repeat passphrase: 
  "0xb2f69ddf70297958e582a0cc98bce43294f1007d"

Remember to use a strong and randomly generated password. We just created our first account. If we try to list our accounts again we can see our new account. 

.. code-block:: Javascript

  > eth.accounts
  ["0xb2f69ddf70297958e582a0cc98bce43294f1007d"]

Using EthKey
================================================================================

Using Mist
================================================================================

Using RPC
================================================================================

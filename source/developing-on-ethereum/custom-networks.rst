.. _custom-networks:

********************************************************************************
Custom Networks
********************************************************************************

A network is defined by the genesis block and several infrastructure related options like the network id.

Networks created using a different genesis and config than the live network will be completely separated from the live network.
 
Using ++eth (C++ client)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is possible to connect to or create a new network by using the --genesis and --config.

.. code:: Console

  > eth --private "customChain" --config config.json --genesis genesis.json

It is possible to use both --config and --genesis. 

In that case, the genesis block description provided by --config will be overwritten by the --genesis option.


.. code:: Console

  --private //defines the name of the custom chain (optional).

.. code:: Console
  
  --config <filename>
 
.. note:: <filename> contains a JSON description of the network:
	
	- sealEngine (engine use to mine block)

		"Ethash" is the Ethereum proof of work engine (used by the live network).

		"NoProof" no proof of work is needed to mine a block.

	- params (general network information like minGasLimit, minimumDifficulty, blockReward, networkID)

	- genesis (genesis block description)

	- accounts (setup an original state that contains accounts/contracts)

Here is a Config sample (used by the Olympic network):

.. code:: JavaScript

  {
	"sealEngine": "Ethash",
	"params": {
		"accountStartNonce": "0x00",
		"frontierCompatibilityModeLimit": "0xffffffff",
		"maximumExtraDataSize": "0x0400",
		"tieBreakingGas": false,
		"minGasLimit": "125000",
		"gasLimitBoundDivisor": "0x0400",
		"minimumDifficulty": "0x020000",
		"difficultyBoundDivisor": "0x0800",
		"durationLimit": "0x08",
		"blockReward": "0x14D1120D7B160000",
		"registrar": "5e70c0bbcd5636e0f9f9316e9f8633feb64d4050",
		"networkID" : "0x0"
	},
	"genesis": {
		"nonce": "0x000000000000002a",
		"difficulty": "0x20000",
		"mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
		"author": "0x0000000000000000000000000000000000000000",
		"timestamp": "0x00",
		"parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
		"extraData": "0x",
		"gasLimit": "0x2fefd8"
	},
	"accounts": {
		"0000000000000000000000000000000000000001": { "wei": "1", "precompiled": { "name": "ecrecover", "linear": { "base": 3000, "word": 0 } } },
		"0000000000000000000000000000000000000002": { "wei": "1", "precompiled": { "name": "sha256", "linear": { "base": 60, "word": 12 } } },
		"0000000000000000000000000000000000000003": { "wei": "1", "precompiled": { "name": "ripemd160", "linear": { "base": 600, "word": 120 } } },
		"0000000000000000000000000000000000000004": { "wei": "1", "precompiled": { "name": "identity", "linear": { "base": 15, "word": 3 } } },
		"dbdbdb2cbd23b783741e8d7fcf51e459b497e4a6": { "wei": "1606938044258990275541962092341162602522202993782792835301376" },
		"e6716f9544a56c530d868e4bfbacb172315bdead": { "wei": "1606938044258990275541962092341162602522202993782792835301376" },
		"b9c015918bdaba24b4ff057a92a3873d6eb201be": { "wei": "1606938044258990275541962092341162602522202993782792835301376" },
		"1a26338f0d905e295fccb71fa9ea849ffa12aaf4": { "wei": "1606938044258990275541962092341162602522202993782792835301376" },
		"2ef47100e0787b915105fd5e3f4ff6752079d5cb": { "wei": "1606938044258990275541962092341162602522202993782792835301376" },
		"cd2a3d9f938e13cd947ec05abc7fe734df8dd826": { "wei": "1606938044258990275541962092341162602522202993782792835301376" },
		"6c386a4b26f73c802f34673f7248bb118f97424a": { "wei": "1606938044258990275541962092341162602522202993782792835301376" },
		"e4157b34ea9615cfbde6b4fda419828124b70c78": { "wei": "1606938044258990275541962092341162602522202993782792835301376" }
	}
  }


.. code:: Console

  --genesis <filename> (optional if the config option is provided and contains the genesis description).

.. note:: <filename> contains a JSON description of the genesis block:

The content is the same as the genesis field provided by the 'config' parameter:

.. code:: JavaScript
  
  {
		"nonce": "0x000000000000002a",
		"difficulty": "0x20000",
		"mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
		"author": "0x0000000000000000000000000000000000000000",
		"timestamp": "0x00",
		"parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
		"extraData": "0x",
		"gasLimit": "0x2fefd8"
  } 


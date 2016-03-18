Command line options
====================

::

    NAME:
       geth - the go-ethereum command line interface

    USAGE:
       geth [options] command [command options] [arguments...]

    VERSION:
       1.3.1

    COMMANDS:
       recover      Attempts to recover a corrupted database by setting a new block by number or hash
       blocktest    loads a block test file
       import       import a blockchain file
       export       export blockchain into file
       upgradedb    upgrade chainblock database
       removedb     Remove blockchain and state databases
       dump         dump a specific block from storage
       monitor      Geth Monitor: node metrics monitoring and visualization
       makedag      generate ethash dag (for testing)
       gpuinfo      gpuinfo
       gpubench     benchmark GPU
       version      print Ethereum version numbers
       wallet       Ethereum presale wallet
       account      manage accounts
       console      Geth Console: interactive JavaScript environment
       attach       Geth Console: interactive JavaScript environment (connect to node)
       js           executes the given JavaScript files in the Geth JavaScript VM
       help, h      Shows a list of commands or help for one command

    ETHEREUM OPTIONS:
      --datadir "/home/youruser/.ethereum"  Data directory for the databases and keystore
      --networkid "1"                       Network identifier (integer, 0=Olympic, 1=Frontier, 2=Morden)
      --olympic                             Olympic network: pre-configured pre-release test network
      --testnet                             Morden network: pre-configured test network with modified starting nonces (replay protection)
      --dev                                 Developer mode: pre-configured private network with several debugging flags
      --genesis                             Insert/overwrite the genesis block (JSON format)
      --identity                            Custom node name
      --fast                                Enables fast syncing through state downloads
      --cache "0"                           Megabytes of memory allocated to internal caching (min 16MB / database forced)
      --blockchainversion "3"               Blockchain version (integer)

    ACCOUNT OPTIONS:
      --unlock      Unlock an account (may be creation index) until this program exits (prompts for password)
      --password    Password file to use with options/subcommands needing a pass phrase

    API AND CONSOLE OPTIONS:
      --rpc                                                                 Enable the HTTP-RPC server
      --rpcaddr "127.0.0.1"                                                 HTTP-RPC server listening interface
      --rpcport "8545"                                                      HTTP-RPC server listening port
      --rpcapi "db,eth,net,web3"                                            API's offered over the HTTP-RPC interface
      --ipcdisable                                                          Disable the IPC-RPC server
      --ipcapi "admin,db,eth,debug,miner,net,shh,txpool,personal,web3"      API's offered over the IPC-RPC interface
      --ipcpath "/home/youruser/.ethereum/geth.ipc"                         Filename for IPC socket/pipe
      --rpccorsdomain                                                       Domains from which to accept cross origin requests (browser enforced)
      --jspath "."                                                          JavaSript root path for `loadScript` and document root for `admin.httpGet`
      --exec                                                                Execute JavaScript statement (only in combination with console/attach)

    NETWORKING OPTIONS:
      --bootnodes           Space-separated enode URLs for P2P discovery bootstrap
      --port "30303"        Network listening port
      --maxpeers "25"       Maximum number of network peers (network disabled if set to 0)
      --maxpendpeers "0"    Maximum number of pending connection attempts (defaults used if set to 0)
      --nat "any"           NAT port mapping mechanism (any|none|upnp|pmp|extip:<IP>)
      --nodiscover          Disables the peer discovery mechanism (manual peer addition)
      --nodekey             P2P node key file
      --nodekeyhex          P2P node key as hex (for testing)

    MINER OPTIONS:
      --mine                        Enable mining
      --minerthreads "8"            Number of CPU threads to use for mining
      --minergpus                   List of GPUs to use for mining (e.g. '0,1' will use the first two GPUs found)
      --autodag                     Enable automatic DAG pregeneration
      --etherbase "0"               Public address for block mining rewards (default = first account created)
      --gasprice "50000000000"      Minimal gas price to accept for mining a transactions
      --extradata                   Block extra data set by the miner (default = client version)

    GAS PRICE ORACLE OPTIONS:
      --gpomin "50000000000"        Minimum suggested gas price
      --gpomax "500000000000"       Maximum suggested gas price
      --gpofull "80"                Full block threshold for gas price calculation (%)
      --gpobasedown "10"            Suggested gas price base step down ratio (1/1000)
      --gpobaseup "100"             Suggested gas price base step up ratio (1/1000)
      --gpobasecf "110"             Suggested gas price base correction factor (%)

    VIRTUAL MACHINE OPTIONS:
      --vmdebug             Virtual Machine debug output
      --jitvm               Enable the JIT VM
      --forcejit            Force the JIT VM to take precedence
      --jitcache "64"       Amount of cached JIT VM programs

    LOGGING AND DEBUGGING OPTIONS:
      --verbosity "3"       Logging verbosity: 0-6 (0=silent, 1=error, 2=warn, 3=info, 4=core, 5=debug, 6=debug detail)
      --vmodule ""          Per-module verbosity: comma-separated list of <module>=<level>, where <module> is file literal or a glog pattern
      --backtrace ":0"      Request a stack trace at a specific logging statement (e.g. "block.go:271")
      --logfile             Log output file within the data dir (default = no log file generated)
      --pprof               Enable the profiling server on localhost
      --pprofport "6060"    Profile server listening port
      --metrics             Enable metrics collection and reporting

    EXPERIMENTAL OPTIONS:
      --shh         Enable Whisper
      --natspec     Enable NatSpec confirmation notice

    MISCELLANEOUS OPTIONS:
      --solc "solc" Solidity compiler command to be used
      --help, -h    show help

Note that the default for datadir is platform-specific. See `backup &
restore <https://github.com/ethereum/go-ethereum/wiki/Backup-&-restore>`__
for more information.

Examples
--------

Accounts
~~~~~~~~

See `Account
management <https://github.com/ethereum/go-ethereum/wiki/Managing-your-accounts>`__

Import ether presale wallet into your node (prompts for password):

::

    geth wallet import /path/to/my/etherwallet.json

Import an EC privatekey into an ethereum account (prompts for password):

::

    geth account import /path/to/key.prv

Geth JavaScript Runtime Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Geth javascript
console <https://github.com/ethereum/go-ethereum/wiki/JavaScript-Console>`__

Bring up the geth javascript console:

::

    geth --verbosity 5 --jspath /mydapp/js console 2>> /path/to/logfile

Execute ``test.js`` javascript using js API and log Debug-level messages
to ``/path/to/logfile``:

::

    geth --verbosity 6 js test.js  2>> /path/to/logfile

Import/export chains and dump blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Import a blockchain from file:

::

    geth import blockchain.bin

Upgrade chainblock database
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the consensus algorithm is changed blocks in the blockchain must be
reimported with the new algorithm. Geth will inform the user with
instructions when and how to do this when it's necessary.

::

    geth upgradedb

Mining and networking
~~~~~~~~~~~~~~~~~~~~~

Start two mining nodes using different data directories listening on
ports 30303 and 30304, respectively:

::

    geth --mine --minerthreads 4 --datadir /usr/local/share/ethereum/30303 --port 30303
    geth --mine --minerthreads 4 --datadir /usr/local/share/ethereum/30304 --port 30304

Start an rpc client on port 8000:

::

    geth --rpc=true --rpcport 8000 --rpccorsdomain '"*"'

Launch the client without network:

::

    geth --maxpeers 0 --nodiscover --networdid 3301 js justwannarunthis.js

Resetting the blockchain
^^^^^^^^^^^^^^^^^^^^^^^^

In the datadir, delete the blockchain directory. For an example above:

::

    rm -rf /usr/local/share/ethereum/30303/blockchain

Sample usage in testing environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The lines below are meant only for test network and safe environments
for non-interactive scripted use.

::

    geth --datadir /tmp/eth/42 --password <(echo -n notsosecret) account new 2>> /tmp/eth/42.log
    geth --datadir /tmp/eth/42 --port 30342  js <(echo 'console.log(admin.nodeInfo().NodeUrl)') > enode 2>> /tmp/eth/42.log
    geth --datadir /tmp/eth/42 --port 30342 --password <(echo -n notsosecret) --unlock primary --minerthreads 4 --mine 2>> /tmp/eth/42.log

Attach
~~~~~~

Attach a console to a running geth instance. By default this happens
over IPC over the default IPC endpoint but when necessary a custom
endpoint could be specified:

::

    geth attach ipc:/some/path
    geth attach rpc:http://host:8545

Alternative ways to set flags
-----------------------------

**WARNING:** This is not available for the latest frontier.

The same flags can be set via config file (by default
``<datadir>/conf.ini``) as well as environment variables.

**Precedence**: default < config file < environment variables < command
line

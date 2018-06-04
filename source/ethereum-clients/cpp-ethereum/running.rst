.. _Running cpp-ethereum:

################################################################################
Running
################################################################################

Run ``eth --help`` to see the various command-line arguments. Running eth without any arguments will synchronise your node to the public blockchain.  It is also possible to create or synchronise to another blockchain (see :ref:`custom blockchain using eth <custom-networks-eth>`). 


**Running eth**
::

   Usage eth [OPTIONS]
   Options:

   Wallet usage:
       account list  List all keys available in wallet.
       account new	Create a new key and add it to the wallet.
       account update [<uuid>|<address> , ... ]  Decrypt and re-encrypt given keys.
       account import [<uuid>|<file>|<secret-hex>]	Import keys from given source and place in wallet.
       wallet import <file>	Import a presale wallet.
   Client mode (default):
     --mainnet                               Use the main network protocol.
     --ropsten                               Use the Ropsten testnet.
     --private <name>                        Use a private chain.
     --test                                  Testing mode: Disable PoW and provide test rpc interface.
     --config <file>                         Configure specialised blockchain using given JSON information.

     --genesis <file>                        Set genesis JSON file.
     -o [ --mode ] <full/peer>               Start a full node or a peer node (default: full).

     --ipc                                   Enable IPC server (default: on).
     --ipcpath <path>                        Set .ipc socket path (default: data directory)
     --no-ipc                                Disable IPC server.
     --admin <password>                      Specify admin session key for JSON-RPC (default: auto-generated and printed at start-up).
     -K [ --kill ]                           Kill the blockchain first.
     -R [ --rebuild ]                        Rebuild the blockchain from the existing database.
     --rescue                                Attempt to rescue a corrupt database.

     --import-presale <file>                 Import a pre-sale key; you'll need to specify the password to this key.
     -s [ --import-secret ] <secret>         Import a secret key into the key store.
     -S [ --import-session-secret ] <secret> Import a secret session into the key store.
     --master <password>                     Give the master password for the key store. Use --master "" to show a prompt.
     --password <password>                   Give a password for a private key.

   Client transacting:
     --ask <wei>            Set the minimum ask gas price under which no transaction will be mined
                            (default 20000000000).
     --bid <wei>            Set the bid gas price to pay for transactions
                            (default 20000000000).
     --unsafe-transactions  Allow all transactions to proceed without verification. EXTREMELY UNSAFE.

   Client mining:
     -a [ --address ] <addr>         Set the author (mining payout) address to given address (default: auto).
     -m [ --mining ] <on/off/number> Enable mining, optionally for a specified number of blocks (default: off).
     --extra-data arg                Set extra data for the sealed blocks.

   Client networking:
     -b [ --bootstrap ]              Connect to the default Ethereum peer servers (default unless --no-discovery used).
     --no-bootstrap                  Do not connect to the default Ethereum peer servers (default only when --no-discovery is used).
     -x [ --peers ] <number>         Attempt to connect to a given number of peers (default: 11).
     --peer-stretch <number>         Give the accepted connection multiplier (default: 7).
     --public-ip <ip>                Force advertised public IP to the given IP (default: auto).
     --listen-ip <ip>(:<port>)       Listen on the given IP for incoming connections (default: 0.0.0.0).
     --listen <port>                 Listen on the given port for incoming connections (default: 30303).
     -r [ --remote ] <host>(:<port>) Connect to the given remote host (default: none).
     --port <port>                   Connect to the given remote port (default: 30303).
     --network-id <n>                Only connect to other hosts with this network id.
     --peerset <list>                Space delimited list of peers; element format: type:publickey@ipAddress[:port].
                                             Types:
                                             default     Attempt connection when no other peers are available and pinning is disabled.
                                             required    Keep connected at all times.

     --no-discovery                  Disable node discovery, implies --no-bootstrap.
     --pin                           Only accept or connect to trusted peers.
   Work farming mode:
       --no-precompute  Don't precompute the next epoch's DAG.
   Ethash verify mode:
       -w,--check-pow <headerHash> <seedHash> <difficulty> <nonce>  Check PoW credentials for validity.

   Benchmarking mode:
       -M,--benchmark  Benchmark for mining and exit; use with --cpu and --opencl.
       --benchmark-warmup <seconds>  Set the duration of warmup for the benchmark tests (default: 3).
       --benchmark-trial <seconds>  Set the duration for each trial for the benchmark tests (default: 3).
       --benchmark-trials <n>  Set the number of trials for the benchmark tests (default: 5).
   DAG creation mode:
       -D,--create-dag <number>  Create the DAG in preparation for mining on given block and exit.
   Mining configuration:
       -C,--cpu  When mining, use the CPU.
       -t, --mining-threads <n> Limit number of CPU/GPU miners to n (default: use everything available on selected platform)
       --current-block Let the miner know the current block number at configuration time. Will help determine DAG size and required GPU memory.
       --disable-submit-hashrate  When mining, don't submit hashrate to node.
   Import/export modes:
     -I [ --import ] <file>      Import blocks from file.
     -E [ --export ] <file>      Export blocks to file.
     --from <n>                  Export only from block n; n may be a decimal, a '0x' prefixed hash, or 'latest'.
     --to <n>                    Export only to block n (inclusive); n may be a decimal, a '0x' prefixed hash, or 'latest'.
     --only <n>                  Equivalent to --export-from n --export-to n.
     --format <binary/hex/human> Set export format.
     --dont-check                Prevent checking some block aspects. Faster importing, but to apply only when the data is known to be valid.
     --download-snapshot <path>  Download Parity Warp Sync snapshot data to the specified path.
     --import-snapshot <path>    Import blockchain and state data from the Parity Warp Sync snapshot.

   General Options:
     -d [ --db-path ] <path>     Load database from path
                                 (default: C:\Users\nilse\AppData\Roaming\Ethereum).

     -v [ --verbosity ] <0 - 15> Set the log verbosity from 0 to 15 (default: 1).
     -V [ --version ]            Show the version and exit.
     -h [ --help ]               Show this help message and exit.
                              

Interacting with your node can be done using either geth or the ethereum console:

**Using geth**

.. code:: console

   > geth attach //attach geth to a running eth node.

**Using the ethereum console**

The ethereum console is a node.js application which connect to a running eth/geth node and provide access to the web3 object.

.. note:: https://github.com/ethereum/ethereum-console

It can be installed using npm:

.. note:: | > npm install -g ethereum-console
            | > ethconsole

.. note:: | **Usage:**
        | ethconsole [javascript file] [ipc socket]
        | Connects to an ethereum node via ipc in order to control it remotely
        | through global variable web3 (web3.admin is also present).
        | If no arguments are given, connects to the default ipc socket
        | and drops into interactive mode.
        | Arguments:
        | <ipc socket path>  connect to the given ipc socket (use ipc://<path> if it does not end with .ipc)
        | <javascript file>    execute the given javascript file that has to end in .js non-interactively.
        | The script has to call process.exit() in order to terminate the console.

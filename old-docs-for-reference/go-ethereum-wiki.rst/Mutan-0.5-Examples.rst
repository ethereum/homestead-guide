Register with NameReg
---------------------

.. code:: go

    #define CONFADDR 0x661005d2720d855f1d9976f88bb10c1a3398c77f

    var a = 0
    var nameRegAddr = 0

    // Get NameReg's address
    call(CONFADDR, 0, 1000, a, nameRegAddr)

    var[2] nameRegArgs
    nameRegArgs[0] = "register"
    nameRegArgs[1] = "MyName"

    // Register with NameReg
    call(nameRegAddr, 0, 1000, nameRegArgs, nil)

DNS
---

The DNS contract is currently in operation on the test net. Simply send
a transaction to "DnsReg" with "register", "your domain name" and 4
bytes representing the IP.

::

    "register"
    "your domain name"
    0x7f000001

.. code:: go

    #define CONFADDR 0x661005d2720d855f1d9976f88bb10c1a3398c77f

    var a = 0
    var nameRegAddr = 0

    call(CONFADDR, 0, 1000, a, nameRegAddr)

    var[2] nameRegArgs
    nameRegArgs[0] = "register"
    nameRegArgs[1] = "DnsReg"

    call(nameRegAddr, 0, 1000, nameRegArgs, nil)

    contract.storage["owner"] = tx.sender()

    return compile {
        if message.data[0] == "register" && contract.storage[message.data[1]] == 0 {
            // Deregister old
            if contract.storage[tx.sender()] != 0 {
                contract.storage[contract.storage[tx.sender()]] = 0
            }
            
            // Ex. jeff.eth => "192.168.0.1"
            // 0xac000001
            contract.storage[message.data[1]] = message.data[2]
            contract.storage[tx.sender()] = message.data[1]
        } else if message.data[0] == "deregister" {
            if contract.storage[tx.sender()] == message.data[1] {
                contract.storage[tx.sender()] = 0
                contract.storage[message.data[1]] = 0
            }
        } else if message.data[0] == "kill" {
            if contract.storage["owner"] == tx.sender() {
                suicide(tx.sender())
            }
        }
    }

Saving w/ lock
--------------

.. code:: go

    #define CONFADDR 0x661005d2720d855f1d9976f88bb10c1a3398c77f

    var a = 0
    var nameRegAddr = 0

    call(CONFADDR, 0, 1000, a, nameRegAddr)

    var[2] nameRegArgs
    nameRegArgs[0] = "register"
    nameRegArgs[1] = "TimeLock"

    call(nameRegAddr, 0, 1000, nameRegArgs, nil)

    contract.storage["owner"] = tx.sender()
    contract.storage["period"] = 20
    contract.storage["initiated"] = block.time()

    return compile {
        if message.data[0] == "lock" {
            if tx.sender() == contract.storage["owner"] && contract.storage["recipient"] == 0 {
                contract.storage["recipient"] = message.data[1]
            }
        } else message.data[0] == "withdraw" {
            if block.time() > contract.storage["period"] + contract.storage["initiated"] {
                suicide(contract.storage["recipient"])
            }
        }
    }

Currency
--------

.. code:: go

    contract.storage[tx.sender()] = 10**12

    return compile {
        var to = message.data[0]
        var from = tx.sender()
        var value = message.data[1]

        if contract.storage[from] > value {
            contract.storage[from] = contract.storage[from] - value
            contract.storage[to] = contract.storage[to] + value
        }
    }

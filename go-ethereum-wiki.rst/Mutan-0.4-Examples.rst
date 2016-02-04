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
        if this.data[0] == "register" {
            if contract.storage[this.data[1]] == 0 {
                // Deregister old
                if contract.storage[tx.sender()] != 0 {
                    contract.storage[contract.storage[tx.sender()]] = 0
                }
                
                // Ex. jeff.eth => "192.168.0.1"
                // 0xac000001
                contract.storage[this.data[1]] = this.data[2]
                contract.storage[tx.sender()] = this.data[1]
            }
            stop()
        }
        
        if this.data[0] == "deregister" {
            if contract.storage[tx.sender()] == this.data[1] {
                contract.storage[tx.sender()] = 0
                contract.storage[this.data[1]] = 0
            }
        }
        
        if this.data[0] == "kill" {
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
        if this.data[0] == "lock" {
            if tx.sender() == contract.storage["owner"] {
                if contract.storage["recipient"] == 0 {
                    contract.storage["recipient"] = this.data[1]
                }
            }
            
            stop()
        }
            
        if this.data[0] == "withdraw" {
            if block.time() > contract.storage["period"] + contract.storage["initiated"] {
                suicide(contract.storage["recipient"])
            }
        }
    }

Currency
--------

.. code:: go

    contract.storage[tx.sender()] = 10**20

    return compile {
        var to = this.data[0]
        var from = tx.sender()
        var value = this.data[1]

        if contract.storage[from] > value {
            contract.storage[from] = contract.storage[from] - value
            contract.storage[to] = contract.storage[to] + value
        }
    }

Life Insurance
--------------

\`\`\`go #define CLAIMER 0xd766c288f24b91ae9781fe2b155d3260b8674c62
this.store[1000] = tx.origin()

func heartbeat() var { if contract.storage[1000] == tx.origin() {
contract.storage[1002] = block.time() return true } else { if
block.time() > contract.storage[1002] - 2592000 { return false } else {
return true } } }

func claim() var { if tx.origin() == CLAIMER { h := heartbeat() if h ==
false { transact(CLAIMER, balance(contract.address()), nil) return true
} else { return false } } }

func withdraw(var amount, var address) var { if contract.storage[1000]
== tx.origin() { h := heartbeat() if h == true { return
transact(address, amount, nil) } else { return false } } }

func run() { if contract.storage[1000] == tx.origin() { if this.data[0]
== "heartbeat" { h := heartbeat() return h } else { address :=
this.data[1] amount := this.data[2] return withdraw(address, amount) } }

::

    if tx.origin() == CLAIMER {
        if this.data[0] == "claim" {
            c := claim()
            return c
        } else {
            return false
        }
    }

} run()

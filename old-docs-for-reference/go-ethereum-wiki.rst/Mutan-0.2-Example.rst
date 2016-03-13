Currency
--------

.. code:: go

    this.store[this.origin()] = 10**20

    exit compile {
        var to = this.data[0]
        var from = this.origin()
        var value = this.data[1]

        if this.store[from] > value {
            this.store[from] = this.store[from] - value
            this.store[to] = this.store[to] + value
        }
    }

Life Insurance
--------------

\`\`\`go #define CLAIMER 0xd766c288f24b91ae9781fe2b155d3260b8674c62
this.store[1000] = this.origin()

func heartbeat() var { if this.store[1000] == this.origin() {
this.store[1002] = this.time() return true } else { if this.time() >
this.store[1002] - 2592000 { return false } else { return true } } }

func claim() var { if this.origin() == CLAIMER { h := heartbeat() if h
== false { transact(CLAIMER, this.balance(), nil) return true } else {
return false } } }

func withdraw(var amount, var address) var { if this.store[1000] ==
this.origin() { h := heartbeat() if h == true { return transact(address,
amount, nil) } else { return false } } }

func run() { if this.store[1000] == this.origin() { if this.data[0] ==
"heartbeat" { h := heartbeat() return h } else { address := this.data[1]
amount := this.data[2] return withdraw(address, amount) } }

::

    if this.origin() == CLAIMER {
        if this.data[0] == "claim" {
            c := claim()
            return c
        } else {
            return false
        }
    }

} run()

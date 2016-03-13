.. code:: go

    package main

    import "fmt"

    type Type byte

    const (
        AddressTy Type = iota
        Int32Ty
        Int64Ty
        Int256Ty
        // ....
    )

    func main() {
        // ABI.
        abi := ABI{
            Methods: []Method{
                Method{
                    Name:  "balance",
                    Const: true,
                },

                Method{
                    Name:  "send",
                    Const: false,
                    Arguments: []Argument{
                        Argument{
                            Name: "to",
                            Type: AddressTy,
                        },
                        Argument{
                            Name: "amount",
                            Type: Int256Ty,
                        },
                    },
                },
            },
        }
        // The above should be returned by = ParseABI(json)

        account := state.GetAccount(address)
        account.SetABI(abi)

        // Hot wallet (to supply transactor)
        hot := state.GetAccount(hotAddress)
        // "idea" to specify the transactor
        state.SetTransactor(hot)
        // OR specify it through call
        account.Call(hot /* .... see params below */)

        // This will do a local call (const = true)
        balance, err := account.Call("balance")
        if err != nil {
            exit(err)
        }
        fmt.Println("balance =", balance)

        // This will do an actual transaction (const = false)
        ret, err := account.Call("send", Address([]byte("my_address")), Int256("111111111111111111"))
        if err != nil {
            exit(err)
        }
        fmt.Println("ret =", ret)

        // "low" level transaction method w/ private key
        to := state.GetAccount(toAddress)
        tx, err := state.Transact(hot, to, Int256("123"), Int256("123"), Int256("123"), []byte("data"))
        if err != nil {
            exit(err)
        }
        fmt.Println("tx =", tx)

        // This should return an error (no private key)
        tx, err = state.Transact(to, hot, Int256("123"), Int256("123"), Int256("123"), []byte("data"))
        if err != nil {
            exit(err)
        }
        fmt.Println("tx =", tx)
    }

    // JSON
    /*
    [
        { "name" : "balance", "const" : true },
        { "name" : "send", "const" : false, "input" : [ { "name" : "to", "type" : "int256" } ] },
    ]
    */

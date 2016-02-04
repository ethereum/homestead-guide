Compiler & Language definition for the Ethereum project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mutan is a C-Like language for the Ethereum project. Mutan supports a
full, dynamic higher level language that compiles to native Ethereum
Assembler. `Repo <https://github.com/obscuren/mutan>`__ will be moved.

An online editor and compiler can be found
`here <http://mutan.jeffew.com>`__

Installation
~~~~~~~~~~~~

::

    go get -u github.com/obscuren/mutan/mutan

Notation
~~~~~~~~

The syntax is specified using Extended Backus-Naur Form (EBNF):

::

    digit excluding zero = "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
    digit                = "0" | digit excluding zero ;

Keywords
~~~~~~~~

The following keywords are reserved and may not be used as identifiers

::

    block         if         true       exit        sizeof     import
    contract      else       false      return      byte       asm
    tx            for        var        stop        call
    this          return     nil        import      create

Operators and delimiters
~~~~~~~~~~~~~~~~~~~~~~~~

Mutan contains the following operators and delimiters

::

    +       **       =       |       (     )
    -       ^        ==      &       {     }
    *       >=       ++      ;       <<    >>
    /       <=       --      !       :=

Numeric types
-------------

Numeric types in Mutan can only be represented by integer values and are
architecture-independent. They are all represented in big endian byte
order. Numbers may be specified in decimal and hexadecimal format.

.. code:: go

    10      0xabc     0xABC

Pointer types
-------------

A pointer type denotes the set of all pointer to variadics. The default
value of an uninitialised pointer is *nil*.

::

    Pointer = "*" Var .

.. code:: go

    var *a

Address operations
------------------

Address operations are performed with the ampersand "&". The operand
must be *addressable* (i.e, a variable).

::

    var a = 10
    var *b = &a

The pointer indirection ``*x`` denotes the value pointed by ``x``.

::

    var old = *b
    *b = 1

Arrays
------

Arrays are of theoretical unlimited length

::

    ArrayType   = Var "[" Number "]" .

The following is a valid array:

.. code:: go

    var[10] a

Declarations
------------

A declaration binds an identifier to a type. Every identifier must be
declared. No identifier may be declared twice and all variables are
scoped to the current executing frame (function).

::

    Declaration = TypeDecl .

A declaration can be done in several ways. First and foremost every
identifier must be declared as a variant. Variants can be created in two
ways, either with the ``var`` keyword or by using the ``:=`` assignment
operator.

.. code:: go

    var a = "a"
    c := "c"

Statements
----------

::

    Statement = Declaration | Block | IfStmt | ForStmt | Expression | Compile

Expression
----------

::

    Expression = Ptr | Number | Hex | String | Identifier .
    Ptr        = Identifier | "nil" .
    Number     = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" .
    Hex        = "0x" "a" | "b" | "c" | "d" | "e" | "f" | Number .
    String     = """ * """
    Identifier = * .

Blocks
------

Blocks contain, but not necessarily, contain lists of Statements within
matching brackets.

::

    Block         = "{" StatementList "}" .
    StatementList = { Statement ";" } .

If statements
-------------

If statements specify the conditional execution of two branches
according to the value of an expression. If the expression evaluated to
true, the "if" branch is executed, else, if present, the else branch is
executed.

::

    IfStmt = "if" [ SimpleStmt ";" ] Expression Block [ "else" Block ] .

.. code:: go

    if x < 10 {
       x = maximum
    }

The expression may be preceded by a simple statement which executes
before the boolean expression

.. code:: go

    if x := value(); x < 10 {
        x = maximum
    } else {
        y = 10
    }

For statement
-------------

A "for" statements specifies repeated execution of a block, the
iteration is controlled by a conditional block.

::

    ForStmt  = "for" [ InitStmt ] ";" [ Condition ] ";" [ PostStmt ] .
    InitStmt = SimpleStmt .
    PostStmt = SimpleStmt .

A "for" in it's simplest form is a C-Like "while" statement (therefor
Mutan doesn't have a "while")

.. code:: go

    for a < b {
        a = a * 2
    }

A "for" statement in it's purest form is controlled my a initialiser,
condition and a post statement which will be executed at the end of the
Block

.. code:: go

    for var a = 0; a < b; a++ {
        b = b - 1
    }

::

    for cond { T() }         is the same as    for ; cond ; { T() }
    for cond; post { T() }   is the same as    for ; cond; post { T() }

String literal
--------------

String literals are supported by enclosing a line of text with matching
quotes ``"string"``. Strings can be assigned to variables and stored in
memory. Strings have a limitation in size. Strings can be no longer than
**32 bytes**. Attempting to create a string larger than 32 bytes will
result in a compile error. This is due to the limitation of the size
that is allowed to be stored in each storage location.

.. code:: go

    str := "hello world"
    contract.storage[0] = "hello world"

Function Declarations
---------------------

A function declarations binds an identifier, *the function name*, to a
function.

::

    FunctionDecl  = "func" FunctionName Signature .
    Signature     = Parameters [ Result ] .
    Parameters    = "(" [ ParameterList [ "," ] ] ")" .
    ParameterList = ParemeterDecl { "," ParameterDecl } .
    ParameterDecl = [ Var Identifier ] .

If the function's signature declares a result parameter, the function
body's statement list must end with a return statement (**TODO**).

.. code:: go

    func fib(var n) var {
        if n == 0 {
            return 0
        } else {
            if n == 1 {
                return 1
            }
        }

        return fib(n-1) + fib(n-2)
    }

Compile
-------

You can invoke the compiler from within mutan allowing you compile code
inline. At this time of writing compile can only be used in combination
with an ``exit`` statement. Compile will compile the given code,
enclosed by brackets.

.. code:: go

    a := "hello"

    exit compile {
         a := 20
         if a == 20 {
         }
    }

Mutan code that is inline compiled does not share any memory outside of
its own scope, and thus can not use any variables outside the enclosed
brackets.

.. code:: go

    var a = "hello"
    return compile {
        b := a // Undefined reference error
    }

Build in functions
------------------

Mutan comes with a couple build in functions for stopping, creating and
transacting between multiple objects and context functions.

exit() / stop()
'''''''''''''''

::

    "exit(); stop()"

Stops the execution of the current call

byte(word, nth)
'''''''''''''''

Returns the nth byte in the given word

call(addr, value, gas, in, out)
'''''''''''''''''''''''''''''''

::

    Success = "call(" Expression, Expression, Expression, Ptr, Ptr ")"

Calls contract specified by the address and executes. Arguments can be
passed to the ``in`` argument and the return value can be specified by
the ``out`` parameters. Return a ``1`` or ``0`` depending whether this
call was success or not.

transact(addr, gas, value, data)
''''''''''''''''''''''''''''''''

::

    Success = "transact(" Expression, Expression, Expression, Ptr ")"

Handles a transaction between two objects.

create(value, script)
'''''''''''''''''''''

::

    Address = "create(" Expression, Expression ")"

Creates a new contract given by ``script`` and returns the ``Address``
of the transaction.

Transaction methods
^^^^^^^^^^^^^^^^^^^

::

    TxMethod    = "tx" "." MethodName [ "(" [ Expression ] ")" ] .
    MethodName  = "origin" | "gasPrice" | "value" .

    origin      Returns the initiator of the first call (sender of the transaction)
    gasPrice    Returns the gas price set for the transaction
    value       Returns the value of the transaction

Contract methods
^^^^^^^^^^^^^^^^

::

    ContractMethod   = "contract" "." MethodName "(" [ Expression ] ")" .
    MethodName       = "storage" | "address" .

    storage          Returns the contract's storage given by the key
    address          Returns the direct address of this execution

Call methods
^^^^^^^^^^^^

::

    CallMethod   = "this" "." MethodName "(" [ Expression ] ")" .
    MethodName   = "data" | "gas" .

    data             Returns the x'th value of the attached data of this call
    gas              Returns the current call's attached amount of gas

Block methods
^^^^^^^^^^^^^

::

    BlockMethod   = "block" "." MethodName "(" [ Expression ] ")" .
    MethodName    = "difficulty" | "prevHash" | "time" | "number" | "coinbase" .

    difficulty    Returns the current difficulty
    prevHash      Returns the previous block's hash
    time          Returns the current block's timestamp
    number        Returns the current block's number
    coinbase      Returns the current block's coinbase

import
------

Importing sourcefiles can be done through the ``import`` keyword

::

    Import = "import" StringLiteral

.. code:: go

    import "std.mu"

Assembler
---------

Inline assembler is allowed through the ``asm`` keyword

::

    InlineAssembler = "asm" "{" Code "}" .
    Code            = "abcdefghijklmnopqrstuwvxyz" | "1234567890" .

For a full list of ``asm`` opcodes see the
`Assembler <https://github.com/ethereum/go-ethereum/wiki/Assembler>`__
page.

Pre processor
-------------

Mutan has a very basic pre processor that takes any ``#define`` and
replaces that throughout the source code

::

    Output = "#define" Word [ Expression ] .

Basic syntax
------------

.. code:: go

    #define ADDR 0xe6716f9544a56c530d868e4bfbacb172315bdead

    import "std.mu"

    func pow(var x, var y) {
        return x ** y
    }

    p := pow(10, 2)

    var a = 20
    var b = 10

    var str = "hello"
    otherStr := "world"

    if a < b {
        exit()
    } else {
        // :-)
        if !a {
            if contract.data[0] ** 10 >= 10 {
                contract.data[0] = 1000;
            }
        }
    }

    contract.storage[a] = 10000
    contract.storage[b] = tx.origin()

    for i := 0; i < 10; i++ {
        var[10] out
        call(0xaabbccddeeff112233445566, 0, 10000, i, out)
    }

    // tx without input data
    transact(0xa78f6abe, 10000, nil)
    // no args and return values
    call(0xab, 0, 10000, nil, nil)
    // create contract
    big ret = create(value, compile {
        var bt      = block.time()
        var dataLen = tx.data
        var price   = tx.gasPrice()
    })

    var left = 8 << 2
    left = left >> 2

    var[2] array
    array[0] = 42
    array[1] = 0
    var re = sha3(array, sizeof(array))

    asm {
        push1 10
        push1 0
        mstore
    }

    return compile {
        contract.storage[0] = "hello"
    }


Compiler & Language definition for the Ethereum project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mutan is a C-Like language for the Ethereum project. Mutan supports a
full, statically typed higher level language that compiles to native
Ethereum Assembler. `Repo <https://github.com/obscuren/mutan>`__ will be
moved.

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

    this if else return exit for asm nil transact create call sizeof true false

Operators and delimiters
------------------------

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
order. Signed integers aren't supported (yet?)

::

    int8        the set of all _unsigned_ integers (0 to 255)
    int16       the set of all _unsigned_ integers (0 to 65535)
    int32       the set of all _unsigned_ integers (0 to 4294967295)
    int64       the set of all _unsigned_ integers (0 to 18446744073709551615)
    int256      the set of all _unsigned_ integers (0 to 1.1579209e+77)
    addr        special type for storing addresses with a size of 20 bytes
    big         type int256
    int         type int32
    byte, bool  type int8

Numbers may be specified in decimal and hexadecimal format.

Arrays
------

Arrays are of theoretical unlimited length

::

    ArrayType   = ElementType "[" Number "]" .
    ElementType = Type .

The following are all valid arrays:

::

    int16[10] a
    int32[10] b
    big[10]   c

Declarations
------------

A declaration binds an identifier to a type. Every identifier must be
declared. No identifier may be declared twice. All declarations are
global.

::

    Declaration = TypeDecl .

A declaration can be done in several ways. First and foremost every
identifier must be declared either with a type or a variant. Variants
can be created in two separate ways, either with the ``var`` keyword or
by using the ``:=`` assignment operator.

.. code:: go

    var a = "a"
    string b = "b"
    c := "c"

If a variable has been declared as a variant and assigned, it's no
longer possible to re-assign it with a different type.

.. code:: go

    a := 10
    a = "hello" // Error

::

    Types:
        var bool int int8 int16 int32 int64 int256 big string

Statements
----------

::

    Statement = Declaration | Block | IfStmt | ForStmt | Expression | Lambda

Expression
----------

::

    Expression = Ptr | Number | Hex | String | Identifier .
    Ptr = Identifier | "nil" .
    Number = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" .
    Hex = "0x" "a" | "b" | "c" | "d" | "e" | Number .
    String = """ * """
    Identifier = * .

Blocks
------

Blocks contain, but not necessarily, contain lists of Statements within
matching brackets.

::

    Block = "{" StatementList "}" .
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

    if int8 x = this.Value(); x < 10 {
        x = maximum
    } else {
        y = 10
    }

For statement
-------------

A "for" statements specifies repeated execution of a block, the
iteration is controlled by a conditional block.

::

    ForStmt = "for" [ InitStmt ] ";" [ Condition ] ";" [ PostStmt ] .
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

    for int8 a = 0; a < b; a++ {
        b = b - 1
    }

::

    for cond { T() }         is the same as    for ; cond ; { T() }
    for cond; post { T() }   is the same as    for ; cond; post { T() }

String literal
--------------

String literals are supported by enclosing a line of text with matching
quotes ``"string"``. Strings can be assigned to variables and stored in
memory. Storing strings in memory only allows storing up to **32
bytes**. This is due to the limitation of the size that is allowed to be
stored in each storage location. If a string with a size larger than 32
bytes is assigned to a storage address it will throw an error.

.. code:: go

    str := "hello world"
    this.store[0] = "hello world"

Lambda
------

A lambda in mutan is a semi lambda and, at the time of writing, can only
be used in a return statement. A lambda will compile the given code,
enclosed by brackets ``{ // code }``. Lambdas are allowed to be of
arbitrary size and take up as much memory as needed.

.. code:: go

    a := "hello"

    return lambda {
         a := 20
         if a == 20 {
         }
    }

Lambdas have their own scope and do not share any memory outside of
their own scope, neither can they use any memory outside of their scope.
Lambdas should be viewed as separate instances of code.

.. code:: go

    var a = "hello"
    return lambda {
        b := a // Undefined references error
    }

Build in functions
------------------

Mutan comes with a couple build in functions for stopping, creating and
transacting between multiple objects and context functions.

exit()
''''''

::

    "exit()"

Stops the execution of the current call

call(addr, value, gas, in, out)
'''''''''''''''''''''''''''''''

::

    Success = "call(" Expression, Expression, Expression, Ptr, Ptr ")"

Calls contract specified by the address and executes. Arguments can be
passed to the ``in`` argument and the return value can be specified by
the ``out`` parameters. Return a ``1`` or ``0`` depending whether this
call was success or not.

transact(addr, value, data)
'''''''''''''''''''''''''''

::

    Success = "transact(" Expression, Expression, Ptr ")"

Handles a transaction between two objects.

create(value, script)
'''''''''''''''''''''

::

    Address = "create(" Expression, Expression ")"

Creates a new contract given by ``script`` and returns the ``Address``
of the transaction.

Context functions
~~~~~~~~~~~~~~~~~

The following functions relate to the current executing context (i.e.
the closure). These build-in functions are prefixed with ``this.``.

::

    Method     = "this" Dot MethodName "(" [ Expression ] ")" .
    Dot        = "." .
    MethodName = "dataLoad" | "dataSize" | "origin" | "caller" | "gasPrice" | "value" |
                 "diff" | "prevHash" | "time" | "gasPrice" | "number" | "coinbase" | "gas" .

::

    data          Returns the x'th value of the attached data of this call
    dataSize      Returns the size of the data attached to this call
    origin        Returns the origin address of this execution
    caller        Returns the current caller of the closure
    gasPrice      Returns the gas price attached to this call
    value         Returns the value attached to this call
    balance       Returns the value of the current call
    diff          Returns the current difficulty
    prevHash      Returns the previous block's hash
    time          Returns the current block's timestamp
    gasPrice      Returns the attached call's gas price
    number        Returns the current block's number
    coinbase      Returns the current block's coinbase
    gas           Returns the current call's attached amount of gas

Assembler
---------

Inline assembler is allowed through the ``asm`` keyword

::

    InlineAssembler = "asm" "(" Code ")" .
    Code            = "abcdefghijklmnopqrstuwvxyz" | "1234567890" .

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

    int32 a = 20
    int32 b = 10

    var str = "hello"
    otherStr := "world"

    if a < b {
        exit()
    } else {
        // :-)
        if !a {
            if this.data[0] ** 10 >= 10 {
                this.data[0] = 1000;
            }
        }
    }

    this.store[a] = 10000
    this.store[b] = this.origin()

    for int8 i = 0; i < 10; i++ {
        int32[10] out
        call(0xaabbccddeeff112233445566, 0, 10000, i, out)
    }

    // tx without input data
    transact(0xa78f6abe, 10000, nil)
    // no args and return values
    call(0xab, 0, 10000, nil, nil)
    // create contract
    big ret = create(value, 0xaabbccddeeff0099887766552211)

    int8 left = 8 << 2
    left = left >> 2

    asm (
        PUSH 10
        PUSH 0
        MSTORE
    )

    return lambda {
        this.store[0] = "hello"
    }


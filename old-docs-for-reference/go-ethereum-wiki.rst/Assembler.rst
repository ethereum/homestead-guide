This is the assembler code emitted by the Mutan compiler and which can
be used directly in the ``asm`` expression followed by the asm opcodes.

Comments can be made using ";"

.. code:: d

    asm {
        push1 10    ; Push 10 to stack
        push1 20    ; Push 20 to stack
        add         ; Add 10 and 20 together
    }

Arithmetic operations
^^^^^^^^^^^^^^^^^^^^^

::

    stop
    add
    mul
    sub
    div
    sdiv
    mod
    smod
    exp
    neg
    lt
    gt
    eq
    not

Bit operations
^^^^^^^^^^^^^^

::

    and
    or
    xor
    byte

Crypto operations
^^^^^^^^^^^^^^^^^

::

    sha3

Context operations
^^^^^^^^^^^^^^^^^^

::

    address
    balance
    origin
    caller
    callvalue
    calldataload
    calldatasize
    gasprice

Block operations
^^^^^^^^^^^^^^^^

::

    prevhash
    coinbase
    timestamp
    number
    difficulty
    gaslimit

Storage and execution operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    pop
    dup
    swap
    mload
    mstore
    mstore8
    sload
    sstore
    jump
    jumpi
    pc
    msize

Call / Create operations
^^^^^^^^^^^^^^^^^^^^^^^^

::

    create
    call
    return
    suicide

Push operations
^^^^^^^^^^^^^^^

::

    push1
    push2
    push3
    push4
    push5
    push6
    push7
    push8
    push9
    push10
    push11
    push12
    push13
    push14
    push15
    push16
    push17
    push18
    push19
    push20
    push21
    push22
    push23
    push24
    push25
    push26
    push27
    push28
    push29
    push30
    push31
    push32

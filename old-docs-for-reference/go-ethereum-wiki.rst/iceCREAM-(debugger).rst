**UPDATE** IceCream has been removed as of 0.9.0 in favour of more
advanced other tools.

Go Ethereum comes with a handy EVM debugger called iceCREAM (after the
famous 'SoftICE' kernel debugger). This article will give you a basic
understanding of debugging EVM code and operating the iceCREAM debugger.

.. figure:: https://photos-5.dropbox.com/t/0/AACUFqkxJZxCr0S_K-65D8lBwFcD9g2fXj0EM6VK8cosTA/12/4270001/png/1024x768/3/1404478800/0/2/Screenshot%202014-07-04%2013.46.16.png/b0UNfgLTmovpciCPHQwXjDKVM2NEUGG4bUuKDhC3jSk
   :alt: 

The interface of the debugger is pretty straight forward and can be
accessed from within
`Ethereal <http://github.com/ethereum/go-ethereum/>`__ menu (⌘-D)

-  In the centre of the window you'll find the main editor which support
   `mutan <http://github.com/obscuren/mutan>`__ and `serpent <>`__.
-  On the left side you'll find the disassembled instruction sequence.
-  Right top corner are pre-made snippets
-  Right side you'll find the simulated data field, endowment, amount of
   gas & gas price.
-  Temp is the VM stack
-  Memory is the current in-use memory. Each item is one word (32 bytes)
-  Storage inspector
-  Debugger CLI
-  Debugger log

The debugger supports ``break`` points on an instruction level (so don't
try to use line numbers). Adding a breakpoint through the debugger CLI
(⌘-L) can be done with ``break <instr number>``. When the EVM encounters
a breakpoint it will halt the execution and displays the current state
of the VM such as the current memory, storage and stack, and allows you
to step through the following instructions using the ``next`` button
(⌘-N).

The debugger supports the following shortcut keys: - ⌘-L Debugger CLI -
⌘-R Debug run - ⌘-N Next sequence (during break) - ⌘-G Continue (during
break) - ⌘-1 Focus editor - ⌘-2 Focus data

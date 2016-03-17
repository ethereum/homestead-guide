Getting Geth
============

The Frontier tool is called Geth (the old english third person singular
conjugation of "to go". Quite appropriate given geth is written in
`Go <https://golang.org/>`__. Geth is a multipurpose command line tool
that runs a full Ethereum node implemented in Go. It offers three
interfaces: the `command line subcommands and
options <./Command-Line-Options>`__, a Json-rpc server and an
interactive console.

In order to install Geth, open a command line or terminal tool (if you
are unsure how to do this, consider waiting for a more user friendly
release) and paste the command below:

::

    bash <(curl https://install-geth.ethereum.org)

This script will detect your OS and will attempt to install the Ethereum
CLI. For more options including package managers, check the OS-specific
subsections.

First run
---------

For the purposes of this guide, we will focus on the interactive
console, a JavaScript environment. The history of the console is
persisted between sessions, providing for a powerful and flexible way of
using the client. You can navigate your command history by using the up
and down arrow keys, like a standard command line. To get started Type
the code below on your terminal

::

    geth console

Once geth is fully started, you should see a ``>`` prompt, letting you
know the console is ready. To exit, type ``exit`` at the prompt and hit
``[enter]``.

Using stderr
~~~~~~~~~~~~

Output from the console can be logged or redirected:

``geth console 2>>geth.log``

Using standard tools, the log can be monitored in a separate window:

``tail -f geth.log``

Alternatively, you can also run one terminal with the interactive
console and a second one with the logging output directly.

1. Open two terminals
2. In the **second** terminal type ``tty``. The output will be something
   like ``/dev/pts/13``
3. In your main terminal, type: ``geth console 2>> /dev/pts/13``

This will allow you to monitor your node without cluttering the
interactive console.

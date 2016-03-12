################################################################################
Ethereum Clients
################################################################################

A key design decision for Ethereum was to separate the definition of the
protocol (the "Yellow Paper") from the implementation(s) of that protocol
(geth, eth, etc).

From the earlier days of the project there have been multiple interoperable
client implementations across a range of different operating systems.

As we enter the Homestead phase, the Go client is very, very dominant, but
it hasn't always been that way, and won't necessarily be that way in the
future.

In the early days of the project the C++ client was more popular.
BlockApps were able to create the Haskell client in stealth mode and to
"uncloak" at DEVCON1 as part of the Azure partnership.  Ethcore have
brought a Rust client to life in the last few months.  Every client
has its own strengths.

That client diversity is a huge win for the eco-system as a whole.
It lets us verify that the protocol is unambiguous.  It keeps the door
open for new innovation.  It keeps us all honest.

However, it can be very confusing for end-users, because there is no
universal "Ethereum Installer" for them to use.

.. toctree::
   :maxdepth: 2

   cpp-ethereum/index.rst
   go-ethereum/go-ethereum.rst
   pyethapp/pyethapp.rst
   ethereumjs-lib/ethereumjs-lib.rst
   ethereumj/ethereumj.rst
   ethereumh/ethereumh.rst
   ethereum-ruby/ethereum-ruby.rst
   parity/parity.rst

--------------

**Q.** I noticed my peercount slowly decrease, and now it is at 0.
Restarting doesn't get any peers.

**A.** Check and sync your clock with ntp.
`Example <http://askubuntu.com/questions/254826/how-to-force-a-clock-update-using-ntp>`__
``sudo ntpdate -s time.nist.gov``

--------------

**Q.** I would like to run multiple geth instances but got the error
"Fatal: blockchain db err: resource temporarily unavailable".

**A.** Geth uses a datadir to store the blockchain, accounts and some
additional information. This directory cannot be shared between running
instances. If you would like to run multiple instances follow
`these <https://github.com/ethereum/go-ethereum/wiki/Setting-up-private-network-or-local-cluster>`__
instructions.

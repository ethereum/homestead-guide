Building Mist (GUI)
~~~~~~~~~~~~~~~~~~~

**Note: Mist is currently a work in progress and might not always
work.**

Clone the repository to a directory of your choosing:

.. code:: shell

    git clone https://github.com/ethereum/go-ethereum

Building ``mist`` requires some external libraries to be installed:

-  `GMP <https://gmplib.org>`__
-  `Qt 5 <https://www.qt.io>`__
-  `Qt 5 WebEngine <http://wiki.qt.io/QtWebEngine>`__
-  `Go <https://golang.org>`__

Install these first:

.. code:: shell

    brew install gmp go qt5
    brew link -f qt5 # This is required, sorry.

Finally, build the ``mist`` program using the following commands:

.. code:: shell

    cd go-ethereum
    make mist

Mist does not automatically look in the right location for its GUI
assets. You can set the asset path on the command line.

.. code:: shell

    build/bin/mist --asset_path cmd/mist/assets

Or launch it from its source directory instead:

.. code:: shell

    cd cmd/mist
    ../../build/bin/mist

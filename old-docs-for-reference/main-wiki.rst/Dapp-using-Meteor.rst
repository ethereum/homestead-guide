This tutorial will show you how to setup a Meteor app to be used as a
dapp and probably answer a few questions on why Meteor should be used.

1. `Create your dapp <#create-your-%C3%90app>`__
2. `Start your dapp <#start-your-%C3%90app>`__
3. `Connect your dapp <#connect-your-%C3%90app>`__
4. `Run your dapp <#run-your-%C3%90app>`__
5. `Add dapp styles <#add-%C3%90app-styles>`__
6. `Using Ethereum:elements <#using-ethereumelements>`__
7. `Dapp code structure <#%C3%90app-code-structure>`__
8. `Bundle your dapp <#bundle-your-%C3%90app>`__

FAQ
---

Isn't Meteor a full stack framework, how does that fit into dapp development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

True, Meteor is a full stack framework and its main improvement is
realtime web applications, but Meteor is also the first framework (i
know of), which fully embraced *s*\ ingle *p*\ age *a*\ pp (SPA)
development and provided all necessary tools.

5 reasons why Meteor is a perfect fit:

1. Its purely written in JS and has all the tools a SPA needs
   (Templating engine, Model, on-the-fly compiling, bundling)
2. You get a development environment, which has live reload, CSS
   injection and support for many pre-compilers (LESS, Coffeescript,
   etc) out of the box
3. You can get all frontend code as single ``index.html`` with one
   ``js`` and ``css`` file plus your assets, using
   `meteor-build-client <https://github.com/frozeman/meteor-build-client>`__.
   You can then host it everywhere or simple run the ``index.html``
   itself or distribute it later on *swarm*.
4. It embraces full reactivity, which make building consistent interface
   much easier (similar to angualr.js ``$scope`` or binding)
5. It has a great model called Minimongo, which gives you a mongoDB like
   interface for a reactive in-memory database, which can also be
   `auto-persistet to
   localstorage <https://atmospherejs.com/frozeman/persistent-minimongo>`__
   or
   `indexedDB <https://atmospherejs.com/frozeman/persistent-minimongo2>`__

Do I need to host my dapp on a server?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, using
`meteor-build-client <https://github.com/frozeman/meteor-build-client>`__
you can get all the static assets of you dapp to run without any server,
though if you use a router like
`iron- <https://atmospherejs.com/iron/router>`__ or
`flow-router <https://atmospherejs.com/meteorhacks/flow-router>`__, you
need to use hash (``index.html#!/mypath``) routes instead of clean HTML5
pushstate routes.

--------------

Create your dapp
----------------

Install Meteor if don't have already:

.. code:: bash

    $ curl https://install.meteor.com/ | sh

Then create an app:

.. code:: bash

    $ meteor create myDapp
    $ cd myDapp

Next add the web3 package:

.. code:: bash

    $ meteor add ethereum:web3

I recommend also to add the following packages:

-  `ethereum:dapp-styles <https://atmospherejs.com/ethereum/dapp-styles>`__
   - The LESS/CSS framework which gives your dapp a nice Mist-consistent
   look.
-  `ethereum:tools <https://atmospherejs.com/ethereum/tools>`__ - This
   package gives you the ``EthTools`` object with a set of formatting an
   conversion functions and template helpers for ether.
-  `ethereum:elements <https://atmospherejs.com/ethereum/elements>`__ -
   A set of interface elements specifically made for Ethereum, see this
   `Demo <http://ethereum-elements.meteor.com>`__ for more.
-  `ethereum:accounts <https://atmospherejs.com/ethereum/accounts>`__ -
   Gives you the reactive ``EthAccounts`` collection with all current
   available Ethereum accounts, where balances will be automatically
   updated.
-  `ethereum:blocks <https://atmospherejs.com/ethereum/blocks>`__ -
   Gives you the reactive ``EthBlocks`` collection with the latest 50
   blocks. To get the lastest block use ``EthBlocks.latest`` (It will
   also have the latest default gasPrice)
-  `frozeman:template-var <https://atmospherejs.com/frozeman/template-var>`__
   - Gives you the ``TemplateVar`` object, that allows you to set
   reactive variables, which are template instance specific. See the
   `readme <https://atmospherejs.com/frozeman/template-var>`__ for more.
-  `frozeman:persistent-minimongo2 <https://atmospherejs.com/frozeman/persistent-minimongo2>`__
   - Allows you to auto persist your minimongo collection in local
   storage

Start your dapp
---------------

A short excursion into Meteors folder structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Meteor doesn't force you to have a specific folder structure, though some
folders have specific meaning and will be treated differently when
bundling/running your application.

Folders with specific treatment - ``client`` - files in a folder called
``client`` will only be loaded by the client part of your app and as we
are building a dapp, thats where most of our files go. - ``lib`` - files
in folders called ``lib`` will load before other files in the same
folder. This is an ideal place your init files, libraries, or Ethereum
specific files. - ``public`` - a folder called ``public`` contains assets
meteor will make available on the root of your webserver (or later
bundled dapp) - There are a few more specific folders like ``server``,
``tests``, ``packages``, etc. If you want to get to know them take a
look at the `Meteor
docs <http://docs.meteor.com/#/full/structuringyourapp>`__

So to build a dapp we ideally create the following folder structure in
our ``myDapp`` folder:

::

    - myDapp
       - client
          - lib
          - myDapp.html
          - myDapp.js
          - myDapp.css
       - public

**Note** The community provides also Meteor dapp Boilerplates like this
on from Nick Dodson:
https://github.com/SilentCicero/meteor-dapp-boilerplate

Connect your dapp
~~~~~~~~~~~~~~~~~

To connect our dapp we need to start ``geth`` with the right CORS
headers in another terminal:

.. code:: bash

    $ geth --rpc --rpccorsdomain "http://localhost:3000"

We also need to set the provider. Ideally we create a file in our lib
folder called ``init.js`` and add the following line:

.. code:: js

    if(typeof web3 === 'undefined')
        web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'));

Run your dapp
~~~~~~~~~~~~~

Now we can run our dapp by simply running:

.. code:: bash

    $ meteor

If we go to ``http://localhost:3000``, we should see a website appear
and if we open the browser console we can use the web3 object to query
the geth node:

.. code:: js

    > web3.eth.accounts
    ['0xfff2b43a7433ddf50bb82227ed519cd6b142d382']

Add dapp styles
---------------

If you want your dapp to nicely fit later into Mist and have follow the
official look use the `dapp-styles css css/less
framework <https://atmospherejs.com/ethereum/dapp-styles>`__.

*Note that they are under heavy development and the class names and
elements may change.*

To add it simple add the following packages to your dapp:

.. code:: bash

    $ meteor add less
    $ meteor add ethereum:dapp-styles

Now rename you ``myDapp.css`` to ``myDapp.less`` and add the following
line inside:

.. code:: css

    // libs
    @import '{ethereum:dapp-styles}/dapp-styles.less';

Now you can use all ``dapp-styles`` classes and also overwrite all variables
of the framework. You can find them `in the
repo <https://github.com/ethereum/dapp-styles/blob/master/constants.import.less>`__.
Overwrite them by copying them to your ``myDapp.less`` file and set
different values.

Using Ethereum packages
-----------------------

To make your live as a dapp developer easier we provide some packages
that help you build dapps faster.

If you add the recommended packages above you should have the
`ethereum:tools <https://atmospherejs.com/ethereum/tools>`__,
`accounts <https://atmospherejs.com/ethereum/accounts>`__ and
`ethereum:blocks <https://atmospherejs.com/ethereum/blocks>`__ packages
available.

These 3 packages give you the ``EthTools``, ``EthAccounts`` and
``Ethblocks`` objects, which give you formatter functions, a collection
with the accounts from ``web3.eth.accounts`` (with auto updated balance)
and a collection of the last 50 blocks.

Most of these functions are reactive so they should make building
interfaces a breeze.

Example usage
~~~~~~~~~~~~~

If you look into you ``myDapp.html`` you will find the ``hello``
template. Just add a helper called ``{{currentBlock}}`` some where
between the ``<template name="hello">..</template>`` tags.

Now open the ``myDapp.js`` and add after the ``counter: function..`` the
``currentBlock`` helper:

.. code:: js

    Template.elements.helpers({
        counter: function () {
          ...
        },
        currentBlock: function(){
            return EthBlocks.latest.number;
        }
      });

Then initialize EthBlocks by adding ``EthBlocks.init();`` after
``Session.setDefault('counter', 0);``

If you now check your dapp in the browser you should see the latest
block number, which will increase once you mine.

*For more examples please checkout the packages readmes and the
`demo <http://ethereum-elements.meteor.com>`__
(`source <https://github.com/frozeman/meteor-ethereum-elements-demo>`__)
for more.*

Dapp code structure
-------------------

*This tutorial won't go into building apps with Meteor. For this please
refer to the `Meteor's
tutorials <https://www.meteor.com/tutorials/blaze/creating-an-app>`__,
`A list of good resources <https://www.meteor.com/tools/resources>`__,
`EventMinded <https://www.eventedmind.com>`__ (payed tutorials) or books
like `Building Single-page Web Apps with
Meteor <https://www.packtpub.com/web-development/building-single-page-web-apps-meteor>`__
or `Discover Meteor <http://discovermeteor.com>`__.*

TODO Short: - put Ethereum related stuff into
``client/lib/ethereum/somefile.js`` - use
``myCollection.observe({added: func, changed: func, removed: func})`` to
communicate to Ethereum, keep Ethereum logic out of your app as much as
possible. This way you just write and read from your reactive
collections and the observe functions will handle the rest (e.g.
sendTransactions) - Filters etc will add logs etc to your collections.
So you keep all the callback mess out of your app logic.

For an example see the
`Ethereum-Wallet <https://github.com/ethereum/meteor-dapp-wallet>`__.

Bundle your dapp
----------------

To bundle your dapp into a local standalone file use
`meteor-build-client <https://github.com/frozeman/meteor-build-client>`__:

.. code:: bash

    $ npm install -g meteor-build-client
    $ cd myDapp
    $ meteor-build-client ../build --path ""

This will put your dapps static files into the build folder, above your
``myDapp`` folder.

The last option ``--path`` will make the linking of all files relative,
allowing you to start the app by simply clicking the
``build/index.html``.

Be aware that when running your app on the ``file://`` protocol, you
won't be able to use client side routing, due to web security. Later in
mist you will be able to use client side routing, as dapps are severed
over the ``eth://`` protocol.

In the future you will be able to simply upload your dapp on swarm.

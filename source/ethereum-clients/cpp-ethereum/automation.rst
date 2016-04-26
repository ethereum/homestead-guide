.. _cpp-ethereum-automation:

################################################################################
Automation setup for cpp-ethereum
################################################################################

At the time of writing all of the automation for cpp-ethereum is driven using
a Jenkins instance hosted at http://52.28.164.97.

There is a "pretty alias" to the setup at http://ethbuilds.com, but that is
owned by
`Bob Summerwill <http://bobsummerwill.com/about>`_ personally, not by the
:ref:`Ethereum Foundation <foundation>`, and might end up pointing to something else at a later date.

..  image:: ../../img/jenkins.png
    :height: 256px
    :width: 256px


It runs in parallel with the `Ethereum buildbot instance <https://builds.ethereum.org/>`_
which is used for Go and Python builds.

The fact that we have two different automation systems is not ideal, and is for
historical reasons.   It would make sense for us to consolidate all
:ref:`Ethereum Foundation <foundation>` projects into a single, consistent
automation setup, but that is a non-trivial amount of work.   We're talking about
that.  It will be much easier to assess that when we have completed the
`repo reorg <https://github.com/ethereum/webthree-umbrella/issues/251>`_
for the C++ codebase.

The current Jenkins setup is `missing a canonical continuous integration target <https://github.com/ethereum/webthree-umbrella/issues/247>`_,
which is a major weakness.  There is no single URL which you can visit to find
out whether the C++ builds are working or broken at HEAD.   There is not even
a URL which you can visit per repository, to find if the individual repositories
are working or broken.

We are also missing automation for `webthree-umbrella <http://github.com/ethereum/webthree-umbrella>`_ as a whole, to know
whether the set of repositories which we are publishing is working or broken.

What we **do have** is automation of our pull-requests.   Those are built against
the develop branches of the repositories which they depend on.   There is a
mechanism for specifying alternative branches for those dependencies, when testing
changes which span multiple repositories.   But `it is broken <https://github.com/ethereum/webthree-umbrella/issues/257>`_.

Here are the Jenkins projects for the PR automation.   These are triggered
automatically via Github webhooks whenever new PRs are created, or when the content
of the branches for existing PRs is updated:

* `alethzero-prs <http://52.28.164.97/job/alethzero-prs/>`_ - PR testing for alethzero
* `libethereum-prs <http://52.28.164.97/job/libethereum-prs/>`_ - PR testing for libethereum
* `libweb3core-prs <http://52.28.164.97/job/libweb3core-prs/>`_ - PR testing for libweb3core
* `mix-prs <http://52.28.164.97/job/mix-prs/>`_ - PR testing for mix
* `solidity-prs <http://52.28.164.97/job/solidity-prs/>`_ - PR testing for solidity
* `webthree-helpers-prs <http://52.28.164.97/job/webthree-helpers-prs/>`_ - PR testing for webthree-helpers
* `webthree-prs <http://52.28.164.97/job/webthree-prs/>`_ - PR testing for webthree

Here are the other Jenkins projects we have:

* `ethbinaries-develop <http://52.28.164.97/job/ethbinaries-develop/>`_ and `ethbinaries-release <http://52.28.164.97/job/ethbinaries-release/>`_ - Projects for generating Windows and OS X binaries for the develop and release branches of the webthree-umbrella.   The develop project is run nightly at midnight, UTC.   The release project is run manually.
* `ppa-build-develop <http://52.28.164.97/job/ppa-build-develop/>`_ and `ppa-build-release <http://52.28.164.97/job/ppa-build-release/>`_ - Projects for packaging source and build steps which are then pushing to `Launchpad <https://launchpad.net/~ethereum/+archive/ubuntu/ethereum>`_ where they will be built, and the binaries pushed to the world if they are successful.  The develop project is run nightly at midnight, UTC.   The release project is run manually.
* `solidity-emscripten <http://52.28.164.97/job/solidity-emscripten/>`_ - Solidity builds for the Emscripten architecture.  This is the build target, which calls the publish target detailed below.   It is run nightly at midnight, UTC.
* `update-umbrella <http://52.28.164.97/job/update-umbrella/>`_ - Utility project which can be run manually to update the submodules in the webthree-umbrella project.  It will soon be obsolete.   It is run manually, and also nightly.

The following projects are effectively "libraries" which are used to build the "user-facing"
projects above.

* `ethbinaries-build <http://52.28.164.97/job/ethbinaries-build/>`_ - Used in ethbinaries-develop and ethbinaries-release.
* `project-build <http://52.28.164.97/job/project-build/>`_ - Used in all the PR projects.
* `project-test <http://52.28.164.97/job/project-test/>`_ - Used in all the PR projects.
* `pullrequest_parser <http://52.28.164.97/job/pullrequest_parser/>`_ - Used in all the PR projects.
* `solidity-emscripten-publisher <http://52.28.164.97/job/solidity-emscripten-publisher/>`_ - Used in solidity-emscripten.

Bob does not know what these Jenkins targets are.   They may be obsolete.

* `code-coverage-run <http://52.28.164.97/job/code-coverage-run/>`_

We have been making a conscious effort to `move our automation scripts into Git from Jenkins <https://github.com/ethereum/webthree-umbrella/issues/439>`_
to reduce the "voodoo factor" in our automation.   It is still a work in progress, but here are
some key scripts which our automation uses:

* `homebrew/prepare_receipt.sh <https://github.com/ethereum/webthree-helpers/blob/develop/homebrew/prepare_receipt.sh>`_ - Build for Homebrew
* `scripts/build_emscripten.sh <https://github.com/ethereum/webthree-helpers/blob/develop/scripts/build_emscripten.sh>`_ - Build Emscripten binaries (for browser-solidity)
* `scripts/ethbinaries.sh <https://github.com/ethereum/webthree-helpers/blob/develop/scripts/ethbinaries.sh>`_ - Build Windows and OS X binaries
* `scripts/ethbuild.sh <https://github.com/ethereum/webthree-helpers/blob/develop/scripts/ethbuild.sh>`_ - Build code (all platforms)
* `scripts/ethtests.sh <https://github.com/ethereum/webthree-helpers/blob/develop/scripts/ethtests.sh>`_ - Run tests (all platforms)
* `scripts/ppabuild.sh <https://github.com/ethereum/webthree-helpers/blob/develop/scripts/ppabuild.sh>`_ - Build bundle for PPAs

But we still have some scripts which are orphaned within Jenkins:

* `Create ZIP of Eth in Windows powershell <http://52.28.164.97/configfiles/show?id=org.jenkinsci.plugins.managedscripts.PowerShellConfig1444842304838>`_ - Used to make win_eth.zip
* `github_issue_mover.py <http://52.28.164.97/configfiles/show?id=org.jenkinsci.plugins.managedscripts.ScriptConfig1443614334556>`_ - Script used to match move issues from cpp-ethereum to webthree-umbrella repo


Setting up a new Jenkins slave
-------------------------------------------------------------------------------

This is a nightmare process.   Here's how to add an OS X slave.   The process
for other platforms will vary, but we've not had to do it yet.

- Install appropriate operating system (Bob had to use his own Apple login)
- Install the latest xcode from the Mac Store
- Install Homebrew
    - say yes to xcode select license
    - brew update
    - brew upgrade
    - install pre-requisites (http://www.ethdocs.org/en/latest/ethereum-clients/cpp-ethereum/building-from-source/osx.html)
    - install Ruby
        - See https://github.com/rbenv/rbenv#homebrew-on-mac-os-x
        - brew install rbenv
        - rbenv init
        - rbenv install 1.9.3-p551
        - Add `eval "$(rbenv init -)"` to ~/.bash_profile:
    - Connect the slave using Java web-start (have to lower security settings)
    - Cut-and-paste PATH from the machine into the Configure field for the node in Jenkins:
        - Example:  /Users/administrator/.rbenv/shims:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

    
Known issues
-------------------------------------------------------------------------------

- Lack of canonical build
- Lack of webthree-umbrella builds
- No automated Windows tests
- Broken cross-repo PRs
- Hanging tests
- Incomplete test suits
- Do we run "ethereum/tests" at all?
- Do we run "ethereum/rpc-tests" at all?
- Windows box is running Windows 7 home edition.   No RDC access.
- Running Visual Studio 2013.
- Should be running Windows 10 with VS2015 targeting Windows7
- We still don't have working El Capitan binaries
- Nothing doing Homebrew/PPA updates per cycle
- No clean builds ever?

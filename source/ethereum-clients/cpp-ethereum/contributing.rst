################################################################################
Contributing
################################################################################

Help in whatever form is always more than welcome.

You can just start by :ref:`Building from source` and familiarizing yourself
with the :ref:`Architecture`.  If something strange happens, please report an
issue (see below).

Once you get to know the technology, you can try to answer questions from
other users (we do not always have time for that) either on
`cpp-ethereum gitter <https://gitter.im/ethereum/cpp-ethereum>`_,
`stackexchange <http://ethereum.stackexchange.com/>`_ or just comment on issues.

If you are a C++ developer, you can help by submitting pull requests (see below).

We try to keep a list of `good tasks to start with <https://github.com/ethereum/cpp-ethereum/labels/good%20first%20task>`_.
Please get in contact on gitter if you have any questions or suggestions.

The backlog is kept in github issues with an overview in our
`waffle board <https://waffle.io/ethereum/webthree-umbrella>`_.

The waffle board is also useful to keep track of pull requests pending reviews
(if you switch the filter on the top right to "pull requests only").


How to Report Issues
--------------------

Please report issues against the specific projects using GitHub Issues:

- `cpp-ethereum issues <https://github.com/ethereum/cpp-ethereum/issues>`_
- `cpp-dependencies issues <https://github.com/ethereum/cpp-dependencies/issues>`_
- `evmjit issues <https://github.com/ethereum/evmjit/issues>`_

Try to mention which version of the software you used and on which platform (Windows, MacOS, Linux, ...),
how you got into the situation (what did you do), what did you expect to happen
and what actually happened.

How to Submit Pull Requests / Workflow
--------------------------------------

Set up your workspace using the :ref:`Building from source` instructions.
To contribute you will need to fork/clone the repositories.

Please also respect the `Coding Standards <https://raw.githubusercontent.com/ethereum/cpp-ethereum/develop/CodingStandards.txt>`_.

If you encounter any problems, please ask on gitter.

Create pull requests against the `develop` branch of the repository you
made changes in. Try not to include any merges with the pull request and rebase
if necessary. If you can set labels on a pull request, set it to `please review`
and also ask for a review in `gitter <http://gitter.im/ethereum/cpp-ethereum-development>`_.

You can also do reviews on others' pull requests. In this case either comment
with "looks good" or set the label if you can. If at least one core developer
apart from the author is confident about the change, it can be merged.
If the reviewer thinks that corrections are necessary, they put he label `got issues`.
If the author addressed all comments, they again put `please review` or comment
appropriately.

Automation runs on `Appveyor <https://ci.appveyor.com/project/ethereum/cpp-ethereum>`_
and `TravisCI <https://travis-ci.org/ethereum/cpp-ethereum/branches>`_.

Thanks for helping and have fun!

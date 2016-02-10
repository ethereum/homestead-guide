*****************************
Homestead-Guide
*****************************
|Gitter|

.. |Gitter| image:: https://badges.gitter.im/ethereum/homestead-guide.svg
   :target: https://gitter.im/ethereum/homestead-guide?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge

The Ethereum Homestead Guide is the reference documentation accompanying the Homestead release of the Ethereum project.

`Hosted on ReadTheDocs`_

HOW YOU CAN HELP
================================================================================
**Homestead Documentation Initiative**

It doesn't matter if you are a beginner or an expert, there are many ways to help.

Write Content to the Guide
--------------------------------------------------------------------------------
Help transfer and update content from the Ethereum Wiki, Ethereum Frontier Guide, the Ethereum Stack Exchange, or any other reputable source to relevant pages of the Homestead guide. Alternatively, write your own content for the guide based on experience.

Make sure the documentation you are porting over is still accurate and follows our guidelines for the Homestead docs (https://ethereum-homestead.readthedocs.org/en/latest/about.html).

Review What Has Been Written
--------------------------------------------------------------------------------
Have a look at our guide (https://ethereum-homestead.readthedocs.org/en/latest/) and give us feedback by visiting our Gitter Chatroom (https://gitter.im/ethereum/homestead-guide) or submit a pull request or issue to this repo. Too EZ.

What's In It For Me?
--------------------------------------------------------------------------------
Your name will forever be immortalized, both in my heart and on the Contributors page in the guide.
As a side effect, you may also get those good feels that you get when you help improve documentation :-)

GETTING STARTED
======================

This project uses Sphinx (http://www.sphinx-doc.org/en/stable/index.html) to build html that is published to Read the Docs. To run this documentation on your computer, you should do the following:

Prerequisites
--------------------------------------------------------------------------------
* Python 2.6 or later
* git

Install Sphinx, etc
--------------------------------------------------------------------------------
For OSX/Linux users (based on instructions here: https://read-the-docs.readthedocs.org/en/latest/getting_started.html)

* From command line: ``sudo pip install sphinx``

For Windows users:

* http://www.sphinx-doc.org/en/stable/install.html#windows-install-python-and-sphinx

Get source code
--------------------------------------------------------------------------------
* git clone: https://github.com/ethereum/homestead-guide.git

Build and view html
--------------------------------------------------------------------------------
* In a terminal window, go to your homestead-guide directory.
* ``make html``
* ``cd build/html``
* ``open index.html`` (open in web browser)
* Tip: each time you run ``make html``, just reload your browser to view changes


RESOURCES
================================================================================

**Homestead**

* Homestead Guide online: https://ethereum-homestead.readthedocs.org/en/latest/index.html
* Github: https://github.com/ethereum/homestead-guide
* Gitter: https://gitter.im/ethereum/homestead-guide
* Google doc: https://docs.google.com/document/d/1rVjrNgaDRAQdPp4rGqWrEk5fPgiHff0xsYGCyf06oM8/edit

**Legacy Docs**

* Ethereum Wiki: https://github.com/ethereum/wiki/wiki
* Frontier Guide: https://ethereum.gitbooks.io/frontier-guide/content/ (see below for converted files)
* Souptacular's Giant List of Ethereum Resources: https://souptacular.gitbooks.io/ethereum-tutorials-and-tips-by-hudson/content/giant_ethereum_resource_list.html

**Read the Docs and Sphinx**

- Read the Docs: https://read-the-docs.readthedocs.org/en/latest/getting_started.html
- Sphinx docs: http://www.sphinx-doc.org/en/stable/contents.html
- reStructuredText Primer: http://www.sphinx-doc.org/en/stable/rest.html
- RST cheat sheet: https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst

Directory structure
=========================

.. code-block::

    homestead-guide
      build    - workdir, not commited to repo
      source   - actual content in rst
        conf.py - sphinx configuration
      old-docs-for-reference (Frontier era stuff)
        wiki    - the legacy wiki
        gitbook - the legacy gitbook resources (converted to rst)
      make.bat - windows command to build docs
      Makefile - platforms with make to build docs


Roadmap for Homestead Guide (Old)
================================================================================

* boilerplate using sphinx-quickstart
* settings in `conf.py`
* code up index with proposed structure
* compile/deploy on readthedocs
* include cheatsheat, rst/sphinx/readthedocs resources
* reach out to community reddit - homestead documentation initiative
* allocate chapters to people (ideally author and reviewer)
* migrate old wiki under frontier/wiki (all md files converted to rst)
* migrate old frontier-guide content under frontier/gitbook (all md content converted to rst)
* script to annotate entire wiki with legacy warning

Strategy for migrating old fronter-guide content (Old)
========================================================

* temporaritly include resources about the documentation project within the book itself
  * rst cheatsheet
  * rst/sphinx/readthedocs resources
  * compilation/deployment instructions
  * link to issues and process
  * style guide, conventions
* include the rst conversion of the wiki
* include the rst conversion of the gitbook

.. _Hosted on ReadTheDocs: https://ethereum-homestead.readthedocs.org/en/latest/

*****************************
Homestead-guide
*****************************

Homestead guide is the reference documentation accompanying the homestead release of the ethereum project.

Roadmap for homestead guide
==============================

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

Strategy for migrating old fronter-guide content
========================================================

* temporaritly include resources about the documentation project within the book itself
  * rst cheatsheet
  * rst/sphinx/readthedocs resources
  * compilation/deployment instructions
  * link to issues and process
  * style guide, conventions
* include the rst conversion of the wiki
* include the rst conversion of the gitbook

Directory structure
=========================

..  code::
  homestead-guide
    build    - workdir, not commited to repo
    source   - actual content in rst
      conf.py - sphinx configuration
    frontier
      wiki    - the legacy wiki
      gitbook - the legacy gitbook resources (converted to rst)
    make.bat - windows command to build docs
    Makefile - platforms with make to build docs





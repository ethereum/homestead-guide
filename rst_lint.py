# Load in our dependencies
import os
import sys


BASE_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(BASE_DIR, "source")


from docutils.core import Publisher
from docutils.parsers.rst.directives import register_directive
from docutils.parsers.rst import roles

from sphinx.application import Sphinx
from sphinx.domains.std import StandardDomain
# Just importing the directives also triggers registration.
from sphinx.directives import *  # NOQA


sphinx = Sphinx(
    srcdir=SOURCE_DIR,
    confdir=SOURCE_DIR,
    outdir=os.path.join(BASE_DIR, 'build'),
    doctreedir=os.path.join(BASE_DIR, 'build', 'doctree'),
    buildername='html',
)


class PublisherWithSphinxEnv(Publisher):
    def get_settings(self, *args, **kwargs):
        kwargs.setdefault('env', sphinx.env)
        return Publisher.get_settings(self, *args, **kwargs)


#
# MONKEYPATCHING!!!!
#
# The restructuredtext_lint library uses the `Publisher` class from `docutils`
# to generate linting errors.  Within this class, a `settings` object is
# generated which is then passed into the various directives which produce the
# errors and warnings.  Sphinx has some very specific needs in terms of what
# this settings object looks like, specifically, an `env` property that needs
# to be present.
#
# Here we monkeypatch the `docutils.core.Publisher` object with our own
# subclass which includes the sphinx `env` object such that when the Sphinx
# directives are used, they have the internals that they need available.
from docutils import core
core.Publisher = PublisherWithSphinxEnv

# This import **MUST** occur after the `core.Publisher` monkeypatch.
import restructuredtext_lint as rst_lint


# The Glossary directive is special and needs to be registered on it's own.
for role_name, role in StandardDomain.roles.items():
    roles.register_local_role(role_name, role)
for role_name, role in StandardDomain.directives.items():
    register_directive(role_name, role)


INFO = 10
WARNING = 20
ERROR = 30

LEVELS = {
    'INFO': INFO,
    'WARNING': WARNING,
    'ERROR': ERROR,
}


def lint(dir=SOURCE_DIR, log_level=WARNING):
    errors = []

    for root, subdirs, files in os.walk(SOURCE_DIR):
        for filename in files:
            extension = filename.rpartition('.')[2].lower()
            if extension == "rst":
                abs_path = os.path.abspath(os.path.join(root, filename))
                rel_path = os.path.relpath(abs_path, SOURCE_DIR)

                # Sphinx maintains a list of `docnames` that it has found which
                # are the relative paths to the docs from the SOURCE_DIR
                # without the file extension.  The `sphinx.env.temp_data`
                # dictionary needs to have the current docname populuated while
                # it's being processed for the Sphinx directives to function
                # properly.
                docname = rel_path.rpartition('.')[0]
                sphinx.env.temp_data['docname'] = docname
                linting_errors = rst_lint.lint_file(os.path.join(root, filename))
                if linting_errors:
                    errors.extend(linting_errors)

    if errors:
        for error in errors:
            message = "{prefix}: {full_file_path}:{line_no}: {message}\n".format(
                prefix=error.type,
                full_file_path=os.path.relpath(error.source),
                line_no=error.line,
                message=error.message,
            )
            if LEVELS[error.type] < log_level:
                continue
            elif LEVELS[error.type] < ERROR:
                sys.stdout.write(message)
            else:
                sys.stderr.write(message)
    if any(error.type == "ERROR" for error in errors):
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    lint()

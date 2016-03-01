# Load in our dependencies
import os
import sys

import restructuredtext_lint as rst_lint


BASE_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(BASE_DIR, "source")


def lint(dir=SOURCE_DIR):
    errors = []

    for root, subdirs, files in os.walk(SOURCE_DIR):
        for filename in files:
            extension = filename.rpartition('.')[2].lower()
            if extension == "rst":
                linting_errors = rst_lint.lint_file(os.path.join(root, filename))
                if linting_errors:
                    errors.extend(linting_errors)

    if errors:
        for error in errors:
            message = "{full_file_path}:{line_no}: {message}\n".format(
                full_file_path=os.path.relpath(error.source),
                line_no=error.line,
                message=error.message,
            )
            if error.type == "WARNING":
                sys.stdout.write(message)
            else:
                sys.stderr.write(message)
    if any(error.type == "ERROR" for error in errors):
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    lint()

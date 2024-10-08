"""PyDocStyle linter support module."""

from . import base


class PyDocstyleLinter(base.LinterBase):
    """PyDocStyle linter."""

    def __init__(self):
        # type: () -> None
        """Create a pydocstyle linter."""
        super(PyDocstyleLinter, self).__init__("pydocstyle", "6.1.1")

    def get_lint_version_cmd_args(self):
        # type: () -> List[str]
        """Get the command to run a linter version check."""
        return ["--version"]

    def get_lint_cmd_args(self, file_name):
        # type: (str) -> List[str]
        """Get the command to run a linter."""
        return [file_name]

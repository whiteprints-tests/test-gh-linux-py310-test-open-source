# SPDX-FileCopyrightText: © 2024 Romain Brault <mail@romainbrault.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""Everything related to the command line interface."""

from typing import Final

from test_gh_linux_py310_test_open_source.cli import exception


__all__: Final = ["APP_NAME", "__app_name__"]

__app_name__: Final = "test-gh-linux-py310-test-open-source"
"""The name of the application."""

APP_NAME = exception.check_app_name(__app_name__).replace("-", "_").upper()
"""The name of the application in capital letters."""

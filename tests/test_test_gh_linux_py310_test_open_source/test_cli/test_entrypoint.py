# SPDX-FileCopyrightText: © 2024 Romain Brault <mail@romainbrault.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""Test the CLI entrypoint."""

from click import testing

from test_gh_linux_py310_test_open_source import package_metadata
from test_gh_linux_py310_test_open_source.cli import __app_name__, entrypoint


class TestCLI:
    """Test the CLI."""

    @staticmethod
    def test_version(cli_runner: testing.CliRunner) -> None:
        """Check if the version printed by the CLI match the API one."""
        result = cli_runner.invoke(
            entrypoint.test_gh_linux_py310_test_open_source,
            ["--version"],
        )
        assert result.exit_code == 0, "The CLI did not exit properly."

        version_match = (
            f"{__app_name__}, version {package_metadata.__version__}"
            == result.stdout.rstrip()
        )
        assert version_match, (
            "The python version returned by the CLI do not match the API"
            " version (given by __version__)."
        )

    @staticmethod
    def test_copyright(cli_runner: testing.CliRunner) -> None:
        """Check if the copyright flag exists."""
        result = cli_runner.invoke(
            entrypoint.test_gh_linux_py310_test_open_source,
            ["--copyright"],
        )
        assert result.exit_code == 0, "The CLI did not exit properly."

    @staticmethod
    def test_license(cli_runner: testing.CliRunner) -> None:
        """Check if the license flag exists."""
        result = cli_runner.invoke(
            entrypoint.test_gh_linux_py310_test_open_source,
            ["--license"],
        )
        assert result.exit_code == 0, "The CLI did not exit properly."

    @staticmethod
    def test_help_flag_exists(cli_runner: testing.CliRunner) -> None:
        """Check if the version printed by the CLI match the API one."""
        result = cli_runner.invoke(
            entrypoint.test_gh_linux_py310_test_open_source,
            ["--help"],
        )
        assert result.exit_code == 0, "The CLI did not exit properly."

    @staticmethod
    def test_debug_info(cli_runner: testing.CliRunner) -> None:
        """Check if the debug-info flag exists."""
        result = cli_runner.invoke(
            entrypoint.test_gh_linux_py310_test_open_source,
            ["--debug-info"],
        )
        assert result.exit_code == 0, "The CLI did not exit properly."

    @staticmethod
    def test_default(cli_runner: testing.CliRunner) -> None:
        """Check if the CLI called with default arguments return prpperly.

        Args:
            cli_runner: the CLI test runner provided by typer.testing or a
                fixture.
        """
        result = cli_runner.invoke(
            entrypoint.test_gh_linux_py310_test_open_source
        )
        assert result.exit_code == 0, "The CLI did not exit properly."
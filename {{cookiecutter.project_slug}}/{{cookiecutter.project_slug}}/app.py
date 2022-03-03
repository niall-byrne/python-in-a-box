"""The default python-in-a-box app."""

import sys


def greeter(message: str) -> None:
    """Greets the user with the specified message.

    :param message: The message to greet with.
    """

    sys.stdout.write(message)


def main() -> None:
    """Greets the user."""

    greeter("Hello World!")

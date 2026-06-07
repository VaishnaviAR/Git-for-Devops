"""Simple demo functions for arithmetic examples.

This module provides a tiny example function used in CI/linting
demonstrations and the project exercises.
"""


def my_function():
    """Return the sum of two integers.

    This function adds two fixed integers and returns the result.
    It exists to demonstrate function docstrings for linters.
    """

    a = 5
    b = 6
    return a + b


if __name__ == "__main__":
    print(my_function())

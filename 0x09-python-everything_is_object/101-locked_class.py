#!/usr/bin/python3
"""The LockedClass module

Raises:
    AttributeError: only first_name allowed
"""


class LockedClass:
    """Class with no instnce attributes
    """

    __slots__ = ("first_name")

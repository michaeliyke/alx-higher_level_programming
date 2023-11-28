#!/usr/bin/python3
"""The LockedClass module

Raises:
    AttributeError: only first_name allowed
"""


class LockedClass:
    """Class with no instnce attributes
    """

    def __setattr__(self, name, value):
        """Prohibits setting of instace attributes except first_name

        Args:
            name (str): an attribute about to be set on on instance
            value (Any): The value to set the attribute to

        Raises:
            AttributeError: raises for all attribute setting except first_name
        """
        if name == "first_name":
            super().__setattr__(name, value)

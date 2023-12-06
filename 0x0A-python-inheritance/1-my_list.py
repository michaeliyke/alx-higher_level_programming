#!/usr/bin/python3
"""My List module"""


class MyList(list):
    """My ist class"""

    def print_sorted(self):
        """Prints the list, but sorted ascending"""
        lst = sorted(self)
        print(lst)

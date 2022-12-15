"""
Template for writing DCC agnostic tools
"""

from abc import ABC, abstractmethod


class XAppTemplate(ABC):
    """
    Simple class which gets the current selection and prints it out. Methods marked as @abstractmethod contain
    calls to DCC specific libraries such as maya.cmds or pyfbsdk. Methods without this decorator should not call
    these libraries.

    This class is meant to be inherited from per DCC.
    """

    def __init__(self):
        pass

    @abstractmethod
    def get_selection(self):
        """
        Gets the current selection

        TODO: Needs to be overridden per DCC

        Returns: list

        """

        return []

    def print_selection(self):
        """
        Prints the current selection

        Returns:

        """

        print(self.get_selection())

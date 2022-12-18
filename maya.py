"""
Module containing Maya specific code
"""

from .main import XAppTemplate
import maya.cmds


class Template(XAppTemplate):
    """
    Sub-class of XAppTemplate() containing Maya specific code.
    """

    def __init__(self):

        # Allow access to parent class methods
        super(Template, self).__init__()
        print("--- xapp running in Maya ---")


    def get_selection(self):
        """
        Gets the current selection

        Returns: list

        """

        return maya.cmds.ls(sl=True)
    

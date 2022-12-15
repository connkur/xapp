"""
Module containing Blender specific code
"""

from .main import XAppTemplate
import bpy


class Template(XAppTemplate):
    """
    Sub-class of XAppTemplate() containing Blender specific code.
    """

    def __init__(self):

        # Allow access to parent class methods
        super(Template, self).__init__()


    def get_selection(self):
        """
        Gets the current selection

        Returns: list

        """

        return [obj.name for obj in bpy.context.selected_objects]
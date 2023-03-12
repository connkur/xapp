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
        print("--- xapp running in Blender ---")


    def get_selection(self):
        """
        Gets the current selection

        Returns: list

        """
        
        return [ o.name for o in bpy.context.scene.objects if o.select_get() ]
    

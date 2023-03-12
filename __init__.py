"""
Imports correct modules based on the active DCC
"""

from pathlib import Path
import sys
    
def run(headless = False):
    """
    Entry point for interfacing with xapp
    
    TODO:
        - See if there is a way to consolidate if/else statements.
        - This function can return two different object types which is good for usability but is not best practice. See if a
        better method can be found.
    
    Returns: Template object if running in headless mode, otherwise XAppWin object aka the gui.
    
    """
    
    app_name = Path(sys.argv[0]).stem.lower()
    
    if headless:
        
        if app_name == "maya":
            from .maya import Template
        elif app_name == "blender":
            from .blender import Template
        else:
            # Will result in TypeError letting you know to sub-class XAppTemplate
            from .main import XAppTemplate as Template
            
        inst = Template()
    
    else:
        if app_name == "maya":
            from . import maya_gui as gui
        elif app_name == "blender":
            from . import blender_gui as gui
        else:
            from . import gui
            
        inst = gui.build()
        
    return inst
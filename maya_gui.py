from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide2 import QtWidgets
import shiboken2
import maya.OpenMayaUI

from .gui import XAppWinTemplate


win = None


class XAppWin(XAppWinTemplate):

    def get_parent_window(self):
        """
            Gets Maya's main window object

            TODO: Needs to be overridden per DCC

            Returns: Swig Object of type 'QWidget *'

        """

        ptr = maya.OpenMayaUI.MQtUtil.mainWindow()
        if ptr is not None:
            print("Found main window")
            return shiboken2.wrapInstance(int(ptr), QtWidgets.QMainWindow)
        else:
            return None


def build():
    """
    
    Returns: XAppWin objects
    
    """
    
    global win
    
    try:
        win.setParent( None )
        win.destroy( )
    except:
        pass
    
    win = XAppWin()
    win.show()
    
    return win
    
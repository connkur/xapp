import sys

from PySide2 import QtWidgets
import shiboken2

from .gui import XAppWinTemplate


win = None


class XAppWin(XAppWinTemplate):
    
    
    def closeEvent(self, *args):
        self.app.exit()


    def get_parent_window(self):
        """
            Gets Blender's main window object

            TODO: Needs to be overridden per DCC

            Returns: QMainWindow

        """
        self.app = QtWidgets.QApplication.instance()
        if not self.app:
            self.app = QtWidgets.QApplication(sys.argv)
            
        for widget in self.app.topLevelWidgets():
            if isinstance(widget, QtWidgets.QMainWindow):
                return widget
       
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


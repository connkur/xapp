"""
Module containing XApp's GUI
"""

import sys
from pathlib import Path
from PySide2 import QtGui, QtWidgets, QtCore
from . import const

# TODO: This is a little redundant since we do the same thing in __init__.py
app_name = Path(sys.argv[0]).stem.lower()
if app_name == "maya":
    from .maya import Template
elif app_name == "blender":
    from .blender import Template
else:
    from .main import XAppTemplate as Template


class XAppWinTemplate(QtWidgets.QDialog):
    """
    Class containing UI elements and connections.
    """

    def __init__(self):
        super(XAppWinTemplate, self).__init__(parent=self.get_parent_window())

        self.xapp_inst = Template()

        # Window Settings
        self.setWindowFlags(QtCore.Qt.Tool)  # Ensures GUI appears as a window
        self.setWindowTitle(const.TOOL_NAME)
        
        # Main layout
        self.layout_main = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout_main)
        
        # Button
        self.btn = QtWidgets.QPushButton()
        self.btn.setText("Print Selection")
        self.btn.clicked.connect(self.on_print_selection)
        
        # Add button to layout
        self.layout_main.addWidget(self.btn)


    def get_parent_window(self):
        """
            Gets DCC's main window object

            TODO: Needs to be overridden per DCC

            Returns: None

        """
        
        return None
        
        
    def on_print_selection(self):
        """
        Prints the names of the selected objects
        
        Returns: N/A
        
        """
        self.xapp_inst.print_selection()


def build():
    """

    Returns: MainWindow object

    """

    win = XAppWinTemplate()
    win.show()

    return win

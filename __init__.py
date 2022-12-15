"""
Imports correct modules based on the active DCC
"""

from pathlib import Path
import sys

app_name = Path(sys.argv[0]).stem.lower()
if app_name == "maya":
    from .maya import Template
elif app_name == "blender":
    from .blender import Template

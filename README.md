# xapp
A template package for writing app agnostic tools in Python

Expectations:
1. Package is imported into Blender or Maya. This is easily extendable though.

How To Use:
1. Add the xapp package to the desired app's PYTHONPATH or default scripts directory
2. Run the following lines of code:

  import xapp

  class_inst = xapp.Template()
  class_inst.print_selection()

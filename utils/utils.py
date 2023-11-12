''' utils.py '''

# Collect utils function 
import os

# Defining a function 
def readInput( path ):
  with open(path, 'r') as f:
    return f.readlines()


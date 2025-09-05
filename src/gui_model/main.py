import os
import sys
from pprint import pprint

print(os.getcwd())
print(__name__)
pprint(sys.path)

from gui import GUI

GUI()

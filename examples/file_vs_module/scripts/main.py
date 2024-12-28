import sys

for path in sys.path:
    print(path)

print(__name__)

from src.package_lvl_1.package_lvl_2.test import test

test()

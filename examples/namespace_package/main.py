import sys
from pprint import pprint

sys.path.append(
    "/home/jan/Desktop/projects/consistent_importing/examples/namespace_package/some/path"
)
sys.path.append(
    "/home/jan/Desktop/projects/consistent_importing/examples/namespace_package/some/another_path"
)
pprint(sys.path)


import my_package.computation
import my_package.model

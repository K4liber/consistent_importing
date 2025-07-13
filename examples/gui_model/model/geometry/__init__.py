from .node import Node
# from gui.plots.graph import Graph # it works -> no circular import
from gui import Graph  # it fails -> circular import

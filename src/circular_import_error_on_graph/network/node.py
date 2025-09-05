from examples.circular_graph.error.network.edge import Edge


class Node:
    def __init__(self):
        self._edges: set[Edge] = set()

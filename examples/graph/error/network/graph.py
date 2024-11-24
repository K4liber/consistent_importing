from network.edge import Edge


class Graph:
    def __init__(
            self,
            edges: set[Edge]
    ) -> None:
        self._edges = edges

from network.node import Node


class Edge:
    def __init__(
            self,
            node_from: Node,
            node_to: Node
    ) -> None:
        self._node_from = node_from
        self._node_to = node_to

    @property
    def node_from(self) -> Node:
        return self._node_from
    
    @property
    def node_to(self) -> Node:
        return self._node_to

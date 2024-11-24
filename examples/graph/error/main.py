
from network.edge import Edge
from network.node import Node
from network.graph import Graph


def print_graph():
    graph = Graph(
        edges={
            Edge(
                node_from=Node(),
                node_to=Node()
            )
        }
    )
    print(str(graph))


if __name__ == '__main__':
    print_graph()

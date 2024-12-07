
from examples.graph.error.network.edge import Edge
from examples.graph.error.network.node import Node
from examples.graph.error.network.graph import Graph


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

from examples.circular_import_error_on_graph.network.node import Node
from examples.circular_import_error_on_graph.network.graph import Graph
from examples.circular_import_error_on_graph.network.edge import Edge


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

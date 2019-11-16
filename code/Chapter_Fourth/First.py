from enum import Enum
from queue import Queue

from Chapter_Fourth.Graph import Graph
from Chapter_Fourth.GraphNode import Node


class State(Enum):
    UNVISITED = 1
    VISITED = 2
    VISITING = 3


def there_is_a_route(graph, start, end):
    if start.name == end.name:
        return True

    q = Queue()

    for node in graph.nodes:
        node.state = State.UNVISITED

    start.state = State.VISITING
    q.put(start)
    while not q.empty():
        next = q.get()
        if next is not None:
            for neighbour in next.children:
                if neighbour.state == State.UNVISITED:
                    if neighbour.name == end.name:
                        return True
                    else:
                        neighbour.state = State.VISITING
                        q.put(neighbour)
            next.state = State.VISITED
    return False


if __name__ == "__main__":
    graph = Graph()
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n0.children.append(n1)
    n0.children.append(n4)
    n0.children.append(n5)
    n1.children.append(n3)
    n1.children.append(n4)
    n2.children.append(n1)
    n3.children.append(n2)
    n3.children.append(n4)
    graph.nodes.append(n0)
    graph.nodes.append(n1)
    graph.nodes.append(n2)
    graph.nodes.append(n3)
    graph.nodes.append(n4)
    graph.nodes.append(n5)
    print(there_is_a_route(graph, n0, n3))
    print(there_is_a_route(graph, n5, n0))

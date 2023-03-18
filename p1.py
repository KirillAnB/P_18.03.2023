from typing import Hashable, List
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx



def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    path = []
    visited_nodes = {node: False for node in g.nodes}
    wait_nodes = deque()
    wait_nodes.append(start_node)
    visited_nodes[start_node] = True
    while wait_nodes:
        current_node = wait_nodes.popleft()
        neighbors = g[current_node]
        for neighbor in neighbors:
            if not visited_nodes[neighbor]:
                wait_nodes.append(neighbor)
                visited_nodes[neighbor] = True
        path.append(current_node)
    return path





if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ("A","B"),
        ("A","F"),
        ("B", "G"),
        ("F", "G"),
        ("G", "C"),
        ("G", "H"),
        ("G", "I"),
        ("C", "H"),
        ("H", "I"),
        ("H", "J"),
        ("H", "E"),
        ("H", "D"),
        ("E", "D")
    ])
    nx.draw_spring(graph)
    print(bfs(graph, "A"))
    # plt.show()

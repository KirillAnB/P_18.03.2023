from typing import Hashable, List
import matplotlib.pyplot as plt
import networkx as nx

def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    def rec_dfs(current_node):
        visited.add(current_node)
        result.append(current_node)
        for neighbor in g[current_node]:
            if neighbor not in visited:
                rec_dfs(neighbor)

    visited=set()
    result = []
    rec_dfs(start_node)
    return result





if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ("A","C"),
        ("A", "B"),
        ("C", "F"),
        ("B", "E"),
        ("B", "D"),
        ("E", "G")
    ])
    print(dfs(graph, "A"))

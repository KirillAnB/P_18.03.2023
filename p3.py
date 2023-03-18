from typing import Hashable, Mapping, Union
import networkx as nx

def dig_algo(g, starting_node):
    visited_nodes = {node:False for node in g.nodes}
    total_cost = {node:float("inf") for node in g.nodes}
    current_node = starting_node
    total_cost[current_node] = 0

    for _ in range(len(g)):
        not_visited_total_cost = {node:cost for node, cost in total_cost.items() if not visited_nodes[node]}
        min_cost = float("inf")
        for node, cost in not_visited_total_cost.items():
            if cost < min_cost:
                min_cost = cost
                current_node = node


        visited_nodes[current_node] = True
        for neighbor in g[current_node]:
            weight = g[current_node][neighbor]['weight']
            total_cost[neighbor] = min(total_cost[neighbor], total_cost[current_node]+ weight)

    return total_cost


if __name__ == '__main__':
    graph = nx.DiGraph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 3),
        ("C", "E", 4),
        ("E", "F", 3),
        ("B", "E", 8),
        ("C", "D", 1),
        ("D", "E", 2),
        ("B", "D", 2),
        ("G", "D", 1),
        ("D", "A", 2)

    ])
    print(dig_algo(graph, "A"))
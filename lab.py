from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_stair(g: set):
    visited_nodes = {node: False for node in g.nodes}
    total_cost = {node: float("inf") for node in g.nodes}
    current_node = g[0]#!!!
    total_cost[current_node] = 0

    for _ in range(len(g)):
        not_visited_total_cost = {node: cost for node, cost in total_cost.items() if not visited_nodes[node]}
        min_cost = float("inf")
        for node, cost in not_visited_total_cost.items():
            if cost < min_cost:
                min_cost = cost
                current_node = node

        visited_nodes[current_node] = True
        for neighbor in g[current_node]:
            weight = g[current_node][neighbor]['weight']
            total_cost[neighbor] = min(total_cost[neighbor], total_cost[current_node] + weight)

    return total_cost

def graph_from_stair(expensive_stair):
    pass



if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = graph_from_stair(stairway)
    print(dijkstra_stair(stairway_graph))
import pygame
import matplotlib.pyplot as plt
import networkx as nx
import time
import random

from src.graph import Graph
from src.dfs import DFS
from src.visualizer import DFSVisualizer
from src.problems.all_paths import AllPathsProblem


def create_circular_graph():
    graph = Graph()
    n_nodes = 15
    
    # Create the outer circle
    circle_edges = [(i, i+1) for i in range(1, n_nodes)] + [(n_nodes, 1)]
    graph.add_edges(circle_edges)
    
    # Add random cross connections (about 2 extra connections per node)
    nodes = list(range(1, n_nodes + 1))
    extra_edges = []
    for node in nodes:
        # Add 2 random connections for each node
        possible_targets = [n for n in nodes if n != node and (node, n) not in circle_edges]
        num_connections = min(2, len(possible_targets))
        if possible_targets and num_connections > 0:
            targets = random.sample(possible_targets, num_connections)
            extra_edges.extend((node, target) for target in targets)
    
    graph.add_edges(extra_edges)
    return graph

def main():
    graph = create_circular_graph()
    dfs = DFS(graph)

    print("Available nodes: 1-15")
    start = int(input("Enter the starting node: "))
    end = int(input("Enter the target node: "))

    problem = AllPathsProblem(dfs)
    paths = problem.find_all_paths(start, end)

    visualizer = DFSVisualizer(graph, dfs)
    visualizer.visualize(paths)


if __name__ == "__main__":
    main()

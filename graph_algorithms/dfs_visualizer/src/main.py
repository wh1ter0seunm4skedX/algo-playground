import pygame
import matplotlib.pyplot as plt
import networkx as nx
import time
import random

from src.graph import Graph
from src.dfs import DFS
from src.visualizer import DFSVisualizer
from src.problems.all_paths import AllPathsProblem


def create_demo_graph():
    graph = Graph()
    # Create a simple graph with 8 nodes for demo
    edges = [
        (1, 2), (1, 3), (2, 4), (2, 5),
        (3, 6), (4, 7), (5, 7), (6, 8),
        (7, 8), (3, 5)  # Some cross connections
    ]
    graph.add_edges(edges)
    return graph

def main():
    # Create graph with random layout
    graph = Graph()
    edges = graph.generate_random_graph(n_nodes=8, min_edges=10, max_edges=12)
    
    # Initialize DFS
    dfs = DFS(graph)
    
    # Select random start and end nodes
    nodes = list(range(1, 9))
    start = random.choice(nodes)
    nodes.remove(start)
    end = random.choice(nodes)
    
    print(f"Finding paths from node {start} to node {end}")
    print(f"Graph edges: {edges}")
    
    problem = AllPathsProblem(dfs)
    paths = problem.find_all_paths(start, end)
    
    if not paths:
        print(f"No paths found from {start} to {end}. Trying again...")
        main()
        return
        
    print(f"Found {len(paths)} paths")
    visualizer = DFSVisualizer(graph, dfs)
    visualizer.visualize(paths)

if __name__ == "__main__":
    main()

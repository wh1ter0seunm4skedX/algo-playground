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
    graph = create_demo_graph()
    dfs = DFS(graph)

    print("Available nodes: 1-8")
    start = int(input("Enter the starting node: "))
    end = int(input("Enter the target node: "))

    problem = AllPathsProblem(dfs)
    paths = problem.find_all_paths(start, end)

    visualizer = DFSVisualizer(graph, dfs)
    visualizer.visualize(paths)


if __name__ == "__main__":
    main()

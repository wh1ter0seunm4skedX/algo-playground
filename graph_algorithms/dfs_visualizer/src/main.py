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

class PathVisualizer:
    def __init__(self):
        self.graph = None
        self.dfs = None
        self.visualizer = None
    
    def generate_new_path(self):
        # Create new random graph
        self.graph = Graph()
        edges = self.graph.generate_random_graph(n_nodes=8, min_edges=10, max_edges=12)
        
        # Initialize DFS
        self.dfs = DFS(self.graph)
        
        # Select random start and end nodes
        nodes = list(range(1, 9))
        start = random.choice(nodes)
        nodes.remove(start)
        end = random.choice(nodes)
        
        print(f"Finding new paths from node {start} to node {end}")
        
        problem = AllPathsProblem(self.dfs)
        paths = problem.find_all_paths(start, end)
        
        if not paths:
            return self.generate_new_path()
            
        print(f"Found {len(paths)} paths")
        return paths

    def run(self):
        # Initial setup
        self.graph = Graph()
        self.dfs = DFS(self.graph)
        
        # Generate first random path
        paths = self.generate_new_path()
        
        # Create visualizer with randomize callback
        self.visualizer = DFSVisualizer(self.graph, self.dfs, 
                                      randomize_callback=self.generate_new_path)
        self.visualizer.visualize(paths)

def main():
    viz = PathVisualizer()
    viz.run()

if __name__ == "__main__":
    main()

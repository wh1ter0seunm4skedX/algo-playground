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
    
    def generate_new_graph(self):
        """Generate completely new graph and find a random path"""
        self.graph = Graph()
        edges = self.graph.generate_random_graph(n_nodes=8, min_edges=10, max_edges=12)
        self.dfs = DFS(self.graph)  # Reset DFS with new graph
        
        # Update visualizer first if it exists
        if self.visualizer:
            self.visualizer.update_graph_and_dfs(self.graph, self.dfs)
            
        # Then generate new paths
        return self.generate_new_path()
        
    def generate_new_path(self):
        """Generate new path in existing graph"""
        if not self.graph:
            return self.generate_new_graph()
            
        # Only create new graph if this is called directly (not from generate_new_graph)
        if self.visualizer and self.visualizer.paths:  # Check if we're not in initial setup
            self.dfs.edge_types = {}
            self.graph = Graph()
            edges = self.graph.generate_random_graph(n_nodes=8, min_edges=10, max_edges=12)
            self.dfs = DFS(self.graph)
            self.visualizer.update_graph_and_dfs(self.graph, self.dfs)
        
        # Select random start and end nodes that have a valid path between them
        nodes = list(range(1, 9))
        valid_path = False
        max_attempts = 20
        attempts = 0
        
        while not valid_path and attempts < max_attempts:
            start = random.choice(nodes)
            remaining = [n for n in nodes if n != start]
            end = random.choice(remaining)
            
            if self.graph.has_path(start, end):
                valid_path = True
            attempts += 1
            
        if not valid_path:
            return self.generate_new_graph()
        
        print(f"Finding new paths from node {start} to node {end}")
        problem = AllPathsProblem(self.dfs)
        paths = problem.find_all_paths(start, end)
        
        if not paths:
            return self.generate_new_path()
            
        print(f"Found {len(paths)} valid paths")
        return paths

    def run(self):
        # Initial setup
        self.graph = None
        self.dfs = None
        paths = self.generate_new_graph()
        
        # Create visualizer with both callbacks
        self.visualizer = DFSVisualizer(
            self.graph, 
            self.dfs,
            randomize_callback=self.generate_new_path,
            new_graph_callback=self.generate_new_graph
        )
        self.visualizer.visualize(paths)

def main():
    viz = PathVisualizer()
    viz.run()

if __name__ == "__main__":
    main()

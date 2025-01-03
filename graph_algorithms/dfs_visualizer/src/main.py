import pygame
import matplotlib.pyplot as plt
import networkx as nx
import time

from src.graph import Graph
from src.dfs import DFS
from src.visualizer import DFSVisualizer
from src.problems.all_paths import AllPathsProblem


class EnhancedDFSVisualizer(DFSVisualizer):
    def __init__(self, graph, dfs):
        super().__init__(graph, dfs)

    def visualize(self, paths):
        pos = nx.spring_layout(self.graph.graph, seed=42)  # Aesthetic layout

        plt.figure(figsize=(8, 6))
        nx.draw(self.graph.graph, pos, with_labels=True, node_size=2000, font_size=16, node_color='lightblue')

        # Highlight the paths step by step
        for path in paths:
            self.animate_path(path, pos)

        plt.show()

    def animate_path(self, path, pos):
        for i in range(len(path) - 1):
            edge_list = [(path[i], path[i + 1])]
            self.draw_single_step(pos, edge_list)
            time.sleep(0.5)  # Pause for animation effect

    def draw_single_step(self, pos, edge_list):
        plt.clf()  # Clear the previous drawing

        # Draw all nodes and edges first
        nx.draw(self.graph.graph, pos, with_labels=True, node_size=2000, font_size=16, node_color='lightblue')

        # Highlight the current edge and node in the path
        nx.draw_networkx_edges(self.graph.graph, pos, edgelist=edge_list, edge_color='red', width=3)
        nx.draw_networkx_nodes(self.graph.graph, pos, nodelist=[edge_list[0][0], edge_list[0][1]], node_color='orange')

        plt.draw()
        plt.pause(0.1)  # Display the update


def main():
    graph = Graph()
    graph.add_edges([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (2, 5)])

    dfs = DFS(graph)

    # Input the start and end nodes
    start = int(input("Enter the starting node: "))
    end = int(input("Enter the target node: "))

    problem = AllPathsProblem(dfs)
    paths = problem.find_all_paths(start, end)

    # Initialize the visualizer (remove EnhancedDFSVisualizer)
    visualizer = DFSVisualizer(graph, dfs)
    visualizer.visualize(paths)


if __name__ == "__main__":
    main()

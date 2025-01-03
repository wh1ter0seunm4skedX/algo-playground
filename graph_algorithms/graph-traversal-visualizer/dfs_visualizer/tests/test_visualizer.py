import unittest
from src.visualizer import DFSVisualizer
from src.graph import Graph
from src.dfs import DFS

class TestDFSVisualizer(unittest.TestCase):
    def test_visualization(self):
        graph = Graph()
        graph.add_edges([(1, 2), (1, 3)])
        dfs = DFS(graph)
        visualizer = DFSVisualizer(graph, dfs)
        visualizer.visualize([])
        # Further assertions to check the visual output

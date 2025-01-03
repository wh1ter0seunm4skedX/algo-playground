import unittest
from src.graph import Graph

class TestGraph(unittest.TestCase):
    def test_add_edges(self):
        graph = Graph()
        graph.add_edges([(1, 2), (1, 3)])
        self.assertEqual(graph.get_neighbors(1), [2, 3])

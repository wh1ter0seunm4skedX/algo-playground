import unittest
from src.graph import Graph
from src.dfs import DFS

class TestDFS(unittest.TestCase):
    def test_dfs_paths(self):
        graph = Graph()
        graph.add_edges([(1, 2), (1, 3), (2, 4)])
        dfs = DFS(graph)
        dfs.dfs(1, 4)
        self.assertEqual(dfs.paths, [[1, 2, 4], [1, 3]])

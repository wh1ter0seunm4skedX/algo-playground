import unittest
from src.problems.all_paths import AllPathsProblem
from src.graph import Graph
from src.dfs import DFS

class TestProblems(unittest.TestCase):
    def test_all_paths(self):
        graph = Graph()
        graph.add_edges([(1, 2), (1, 3), (2, 4)])
        dfs = DFS(graph)
        problem = AllPathsProblem(dfs)
        paths = problem.find_all_paths(1, 4)
        self.assertEqual(paths, [[1, 2, 4]])

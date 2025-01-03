import networkx as nx

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_edges(self, edges):
        self.graph.add_edges_from(edges)

    def get_neighbors(self, node):
        return list(self.graph.neighbors(node))

    def get_nodes(self):
        return list(self.graph.nodes)

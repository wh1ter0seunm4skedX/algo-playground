class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = edges
        self.adj_list = self._build_adj_list(edges)
    
    def _build_adj_list(self, edges):
        adj_list = {i: [] for i in range(self.num_nodes)}
        for u, v in edges:
            adj_list[u].append(v)
        return adj_list

    def reverse(self):
        reversed_edges = [(v, u) for u, v in self.edges]
        return Graph(self.num_nodes, reversed_edges)
    
    def get_adj_list(self):
        return self.adj_list

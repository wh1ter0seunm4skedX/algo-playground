class Graph:
    def __init__(self, edges):
        """
        edges: List of tuples (node1, node2, weight)
        """
        self.edges = edges
        self.adjacency_list = self._create_adjacency_list(edges)
    
    def _create_adjacency_list(self, edges):
        adjacency_list = {}
        for node1, node2, weight in edges:
            if node1 not in adjacency_list:
                adjacency_list[node1] = []
            if node2 not in adjacency_list:
                adjacency_list[node2] = []

            adjacency_list[node1].append((node2, weight))
            adjacency_list[node2].append((node1, weight))
        return adjacency_list
    
    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

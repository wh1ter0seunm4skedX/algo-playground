import random
from graph import Graph

class RandomGraph:
    def __init__(self, min_nodes=10, max_nodes=15):
        self.min_nodes = min_nodes
        self.max_nodes = max_nodes
    
    def create_random_graph(self):
        # Randomize the number of nodes
        num_nodes = random.randint(self.min_nodes, self.max_nodes)
        
        # Determine a reasonable number of edges
        max_edges = num_nodes * (num_nodes - 1)  # Max possible edges in a directed graph
        num_edges = random.randint(num_nodes, min(max_edges, 2 * num_nodes))
        
        edges = set()
        while len(edges) < num_edges:
            u = random.randint(0, num_nodes - 1)
            v = random.randint(0, num_nodes - 1)
            if u != v:  # Avoid self-loops
                edges.add((u, v))
        
        return Graph(num_nodes, list(edges))


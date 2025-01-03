import networkx as nx
import random

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def generate_random_graph(self, n_nodes=10, min_edges=12, max_edges=15):
        # Clear existing graph
        self.graph.clear()
        nodes = list(range(1, n_nodes + 1))
        self.graph.add_nodes_from(nodes)
        
        # Create a random spanning tree to ensure connectivity
        edges = []
        used = {1}
        unused = set(nodes[1:])
        
        while unused:
            src = random.choice(list(used))
            dst = random.choice(list(unused))
            edges.append((src, dst))
            used.add(dst)
            unused.remove(dst)
        
        # Add random additional edges
        possible_edges = [(i, j) for i in nodes for j in nodes if i != j]
        additional = random.randint(min_edges - len(edges), max_edges - len(edges))
        random_edges = random.sample([e for e in possible_edges if e not in edges], additional)
        edges.extend(random_edges)
        
        self.graph.add_edges_from(edges)
        return edges

    def add_edges(self, edges):
        self.graph.add_edges_from(edges)

    def get_neighbors(self, node):
        return list(self.graph.neighbors(node))

    def get_nodes(self):
        return list(self.graph.nodes)

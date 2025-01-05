import matplotlib.pyplot as plt
import networkx as nx

class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph
    
    def draw_graph(self, title="Graph"):
        g = nx.DiGraph()
        for u, neighbors in self.graph.get_adj_list().items():
            for v in neighbors:
                g.add_edge(u, v)
        
        plt.figure(figsize=(8, 6))
        nx.draw(g, with_labels=True, node_color="skyblue", edge_color="black", node_size=1000, font_size=15)
        plt.title(title)
        plt.show()
    
    def draw_sccs(self, sccs, title="Strongly Connected Components"):
        g = nx.DiGraph()
        color_map = []
        colors = plt.cm.get_cmap("tab10", len(sccs))
        
        for idx, scc in enumerate(sccs):
            for node in scc:
                g.add_node(node)
                color_map.append(colors(idx))
            for u in scc:
                for v in self.graph.get_adj_list()[u]:
                    if v in scc:
                        g.add_edge(u, v)
        
        plt.figure(figsize=(8, 6))
        nx.draw(g, with_labels=True, node_color=color_map, edge_color="black", node_size=1000, font_size=15)
        plt.title(title)
        plt.show()

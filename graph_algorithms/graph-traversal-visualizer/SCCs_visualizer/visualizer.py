import matplotlib.pyplot as plt
import networkx as nx

class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph
        self.figure, self.ax = plt.subplots(figsize=(8, 6))
        self.g = nx.DiGraph()
        self._initialize_graph()
    
    def _initialize_graph(self):
        # Add edges to the NetworkX graph
        for u, neighbors in self.graph.get_adj_list().items():
            for v in neighbors:
                self.g.add_edge(u, v)
        
    def draw_graph(self, title="Graph", highlighted_nodes=None):
        self.ax.clear()
        
        # Highlight specific nodes if needed
        node_colors = ["red" if highlighted_nodes and node in highlighted_nodes else "skyblue" for node in self.g.nodes()]
        
        # Draw the graph
        nx.draw(
            self.g,
            ax=self.ax,
            with_labels=True,
            node_color=node_colors,
            edge_color="black",
            node_size=1000,
            font_size=15
        )
        self.ax.set_title(title, fontsize=16)
        plt.pause(0.5)  # Pause to allow for real-time updates
    
    def draw_sccs(self, sccs, title="Strongly Connected Components"):
        self.ax.clear()
        
        # Assign colors to SCCs
        color_map = {}
        colors = plt.cm.get_cmap("tab10", len(sccs))
        
        for idx, scc in enumerate(sccs):
            for node in scc:
                color_map[node] = colors(idx)
        
        node_colors = [color_map.get(node, "skyblue") for node in self.g.nodes()]
        
        # Draw the graph with SCC coloring
        nx.draw(
            self.g,
            ax=self.ax,
            with_labels=True,
            node_color=node_colors,
            edge_color="black",
            node_size=1000,
            font_size=15
        )
        self.ax.set_title(title, fontsize=16)
        plt.show(block=True)  # Final display

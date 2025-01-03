import matplotlib.pyplot as plt
import networkx as nx

class DFSVisualizer:
    def __init__(self, graph, dfs):
        self.graph = graph
        self.dfs = dfs

    def visualize(self, paths):
        pos = nx.spring_layout(self.graph.graph)
        nx.draw(self.graph.graph, pos, with_labels=True, node_size=2000, font_size=16)
        
        for path in paths:
            edge_list = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(self.graph.graph, pos, edgelist=edge_list, edge_color="red", width=2)

        plt.show()

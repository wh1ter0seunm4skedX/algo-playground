import matplotlib.pyplot as plt
import networkx as nx

class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph
        self.g = nx.DiGraph()
        self.positions = None
        self.steps = []
        self.current_step = 0
        self.stack = []

        self.figure, self.ax = plt.subplots(figsize=(10, 8))
        self._initialize_graph()

    def _initialize_graph(self):
        for u, neighbors in self.graph.get_adj_list().items():
            for v in neighbors:
                self.g.add_edge(u, v)
        self.positions = nx.spring_layout(self.g)

    def add_step(self, title, highlighted_nodes=None):
        self.steps.append((title, highlighted_nodes))

    def display_step(self):
        if not self.steps:
            return

        title, highlighted_nodes = self.steps[self.current_step]
        self._draw_graph(title, highlighted_nodes)

    def _draw_graph(self, title, highlighted_nodes):
        self.ax.clear()
        
        node_colors = [
            "red" if highlighted_nodes and node in highlighted_nodes else "skyblue"
            for node in self.g.nodes()
        ]

        nx.draw(
            self.g,
            pos=self.positions,
            with_labels=True,
            node_color=node_colors,
            edge_color="black",
            node_size=1000,
            font_size=15,
            ax=self.ax
        )
        self.ax.set_title(title, fontsize=16)
        plt.draw()

    def navigate_steps(self, event):
        if event.key == "right":
            self.current_step = min(self.current_step + 1, len(self.steps) - 1)
        elif event.key == "left":
            self.current_step = max(self.current_step - 1, 0)
        self.display_step()

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Button
from matplotlib.patches import Patch

class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph
        self.g = nx.DiGraph()
        self.positions = None
        self.steps = []  # Store steps for navigation
        self.current_step = 0

        self._initialize_graph()

    def _initialize_graph(self):
        for u, neighbors in self.graph.get_adj_list().items():
            for v in neighbors:
                self.g.add_edge(u, v)
        self.positions = nx.spring_layout(self.g)  # Fixed layout

    def add_step(self, title, highlighted_nodes=None, explanation=""):
        self.steps.append((title, highlighted_nodes, explanation))

    def display_step(self):
        if not self.steps:
            print("No steps available to display.")
            return

        title, highlighted_nodes, explanation = self.steps[self.current_step]
        self._draw_graph(title, highlighted_nodes, explanation)

    def _draw_graph(self, title, highlighted_nodes, explanation):
        plt.clf()
        node_colors = [
            "red" if highlighted_nodes and node in highlighted_nodes else "skyblue"
            for node in self.g.nodes()
        ]

        # Draw the graph
        nx.draw(
            self.g,
            pos=self.positions,
            with_labels=True,
            node_color=node_colors,
            edge_color="black",
            node_size=1000,
            font_size=15,
        )

        # Add title and explanation
        plt.title(title, fontsize=16)
        plt.text(
            1.05, 0.5, explanation, fontsize=12, transform=plt.gca().transAxes, verticalalignment="center"
        )

        # Add legend
        legend = [
            Patch(color="skyblue", label="Unvisited Nodes"),
            Patch(color="red", label="Current/Highlighted Node(s)"),
        ]
        plt.legend(handles=legend, loc="upper left", bbox_to_anchor=(1, 1))
        plt.draw()

    def navigate_steps(self, event):
        if event.key == "right":
            self.current_step = min(self.current_step + 1, len(self.steps) - 1)
        elif event.key == "left":
            self.current_step = max(self.current_step - 1, 0)
        self.display_step()

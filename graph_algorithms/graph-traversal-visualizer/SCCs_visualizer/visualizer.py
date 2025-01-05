import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Patch, Rectangle

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
        plt.figure(figsize=(12, 8))  # Larger window size
        plt.clf()
        node_colors = [
            "red" if highlighted_nodes and node in highlighted_nodes else "skyblue"
            for node in self.g.nodes()
        ]

        # Draw the graph on the left side
        ax_graph = plt.subplot(1, 2, 1)
        nx.draw(
            self.g,
            pos=self.positions,
            with_labels=True,
            node_color=node_colors,
            edge_color="black",
            node_size=1000,
            font_size=15,
            ax=ax_graph
        )
        ax_graph.set_title(title, fontsize=16)

        # Add explanation on the right side
        ax_text = plt.subplot(1, 2, 2)
        ax_text.axis("off")  # Turn off axis
        ax_text.set_xlim(0, 1)
        ax_text.set_ylim(0, 1)

        # Add a rectangle for the explanation box
        rect = Rectangle((0.05, 0.05), 0.9, 0.9, color="lightgray", alpha=0.3)
        ax_text.add_patch(rect)

        # Display the explanation inside the box
        ax_text.text(
            0.1, 0.8,
            "Explanation:",
            fontsize=14,
            fontweight="bold"
        )
        ax_text.text(
            0.1, 0.7,
            explanation,
            fontsize=12,
            wrap=True,
            verticalalignment="top",
        )

        # Add legend for graph colors
        legend = [
            Patch(color="skyblue", label="Unvisited Nodes"),
            Patch(color="red", label="Current/Highlighted Node(s)"),
        ]
        ax_graph.legend(handles=legend, loc="lower left", fontsize=10)

        plt.tight_layout()
        plt.draw()

    def navigate_steps(self, event):
        if event.key == "right":
            self.current_step = min(self.current_step + 1, len(self.steps) - 1)
        elif event.key == "left":
            self.current_step = max(self.current_step - 1, 0)
        self.display_step()

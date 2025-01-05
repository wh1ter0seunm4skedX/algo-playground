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
        self.finish_times = {}  # To store finish times for nodes
        self.stack = []         # To store the stack

        # Create a single figure for the entire program
        self.figure, self.axs = plt.subplots(1, 2, figsize=(14, 8))
        self.ax_graph = self.axs[0]
        self.ax_text = self.axs[1]

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
        self.ax_graph.clear()  # Clear the graph subplot
        self.ax_text.clear()   # Clear the text subplot

        node_colors = [
            "red" if highlighted_nodes and node in highlighted_nodes else "skyblue"
            for node in self.g.nodes()
        ]

        # Draw the graph on the left
        nx.draw(
            self.g,
            pos=self.positions,
            with_labels=True,
            node_color=node_colors,
            edge_color="black",
            node_size=1000,
            font_size=15,
            ax=self.ax_graph
        )
        self.ax_graph.set_title(title, fontsize=16)

        # Add explanation and table on the right
        self.ax_text.axis("off")  # Turn off the axis for the text box
        rect = Rectangle((0.05, 0.05), 0.9, 0.9, color="lightgray", alpha=0.3)
        self.ax_text.add_patch(rect)
        self.ax_text.text(
            0.1, 0.85, "Explanation:", fontsize=14, fontweight="bold"
        )
        self.ax_text.text(
            0.1, 0.75, explanation, fontsize=12, wrap=True, verticalalignment="top"
        )

        # Display Finish Times and Stack
        if self.finish_times:
            finish_text = "\n".join(
                f"Node {node}: Finish Time {time}" for node, time in self.finish_times.items()
            )
            self.ax_text.text(
                0.1, 0.5, f"Finish Times:\n{finish_text}", fontsize=10, verticalalignment="top"
            )
        if self.stack:
            stack_text = ", ".join(map(str, self.stack))
            self.ax_text.text(
                0.1, 0.3, f"Stack: {stack_text}", fontsize=10, verticalalignment="top"
            )

        self.figure.tight_layout()
        plt.draw()

    def navigate_steps(self, event):
        if event.key == "right":
            self.current_step = min(self.current_step + 1, len(self.steps) - 1)
        elif event.key == "left":
            self.current_step = max(self.current_step - 1, 0)
        self.display_step()

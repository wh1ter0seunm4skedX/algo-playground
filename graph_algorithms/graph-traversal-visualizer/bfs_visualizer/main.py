import matplotlib.pyplot as plt
import networkx as nx

def bfs_visualizer(graph, start_node):
    # Initialize the graph for visualization
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Define node positions for consistent layout
    pos = nx.spring_layout(G, seed=42)

    # Initialize BFS data structures
    visited = set()
    queue = [start_node]
    traversal_order = []  # Keep track of traversal order for navigation

    visited.add(start_node)
    traversal_order.append(start_node)

    while queue:
        current_node = queue.pop(0)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                traversal_order.append(neighbor)

    # Set up visualization
    plt.close('all')  # Close any existing windows
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.subplots_adjust(right=0.8)  # Leave space for legend

    # Legend setup
    legend_ax = fig.add_axes([0.85, 0.3, 0.1, 0.4])  # [x, y, width, height]
    legend_ax.axis('off')
    legend_ax.text(0.5, 0.9, "Legend", fontsize=12, weight='bold', ha='center')
    legend_ax.text(0.5, 0.7, "Visited", color="skyblue", fontsize=10, ha='center')
    legend_ax.text(0.5, 0.5, "Current", color="green", fontsize=10, ha='center')
    legend_ax.text(0.5, 0.3, "Unvisited", color="lightgray", fontsize=10, ha='center')

    # Variables for navigation
    current_index = 0

    def draw_graph():
        """Draw the graph with the current traversal state."""
        ax.clear()
        nx.draw(G, pos, ax=ax, with_labels=True, node_color="lightgray", edge_color="black", node_size=800, font_size=10, font_weight='bold')
        # Highlight visited nodes
        nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=traversal_order[:current_index], node_color="skyblue", node_size=800)
        # Highlight current node
        if current_index < len(traversal_order):
            nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=[traversal_order[current_index]], node_color="green", node_size=800)
        ax.set_title(f"BFS Visualizer - Step {current_index + 1}/{len(traversal_order)}")

    def on_key(event):
        """Handle keyboard events for navigation."""
        nonlocal current_index
        if event.key == 'right' and current_index < len(traversal_order) - 1:
            current_index += 1
        elif event.key == 'left' and current_index > 0:
            current_index -= 1
        draw_graph()
        fig.canvas.draw()

    # Initial draw
    draw_graph()
    fig.canvas.mpl_connect('key_press_event', on_key)

    plt.show()

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Start BFS visualization
bfs_visualizer(graph, 'A')

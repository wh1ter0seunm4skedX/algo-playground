import matplotlib.pyplot as plt
import networkx as nx

def bfs_visualizer(graph, start_node):
    # Initialize the directed graph for visualization
    G = nx.DiGraph()  # Use DiGraph for directed edges
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
    fig, (ax_graph, ax_queue) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [3, 1]})
    plt.subplots_adjust(wspace=0.3)

    # Variables for navigation
    current_index = 0

    def draw_graph():
        """Draw the graph with the current traversal state."""
        ax_graph.clear()
        nx.draw(
            G, pos, ax=ax_graph, with_labels=True, node_color="lightgray", 
            edge_color="black", node_size=800, font_size=10, font_weight='bold',
            arrows=True  # Add arrows for directed edges
        )
        # Highlight visited nodes
        nx.draw_networkx_nodes(
            G, pos, ax=ax_graph, nodelist=traversal_order[:current_index], 
            node_color="skyblue", node_size=800
        )
        # Highlight current node
        if current_index < len(traversal_order):
            nx.draw_networkx_nodes(
                G, pos, ax=ax_graph, nodelist=[traversal_order[current_index]], 
                node_color="green", node_size=800
            )
        ax_graph.set_title(f"BFS Visualizer - Step {current_index + 1}/{len(traversal_order)}")

    def draw_queue():
        """Display the BFS queue and visited nodes."""
        ax_queue.clear()
        ax_queue.axis("off")
        queue_display = queue[current_index:] if current_index < len(queue) else []
        visited_display = traversal_order[:current_index]
        
        # BFS Queue
        ax_queue.text(0.5, 0.9, "BFS Queue", fontsize=12, weight="bold", ha="center")
        for i, node in enumerate(queue_display):
            ax_queue.text(0.5, 0.8 - i * 0.05, node, fontsize=10, ha="center", color="blue")

        # Visited Nodes
        ax_queue.text(0.5, 0.4, "Visited Nodes", fontsize=12, weight="bold", ha="center")
        for i, node in enumerate(visited_display):
            ax_queue.text(0.5, 0.3 - i * 0.05, node, fontsize=10, ha="center", color="green")

    def on_key(event):
        """Handle keyboard events for navigation."""
        nonlocal current_index
        if event.key == 'right' and current_index < len(traversal_order) - 1:
            current_index += 1
        elif event.key == 'left' and current_index > 0:
            current_index -= 1
        draw_graph()
        draw_queue()
        fig.canvas.draw()

    # Initial draw
    draw_graph()
    draw_queue()
    fig.canvas.mpl_connect('key_press_event', on_key)

    plt.show()

# Example directed graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Start BFS visualization
bfs_visualizer(graph, 'A')

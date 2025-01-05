import matplotlib.pyplot as plt
import networkx as nx
import time

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
    visited.add(start_node)

    # Close any existing plots and setup visualization
    plt.close('all')  # Important: closes any existing windows
    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 6))  # Create ONE figure and axes

    while queue:
        current_node = queue.pop(0)
        ax.clear()  # Clear only the axes content, not the whole figure

        # Draw the graph
        nx.draw(G, pos, ax=ax, with_labels=True, node_color="lightgray", 
                edge_color="black", node_size=800, font_size=10, font_weight='bold')

        # Highlight visited nodes
        nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=list(visited), 
                             node_color="skyblue", node_size=800)

        # Highlight the current node
        nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=[current_node], 
                             node_color="green", node_size=800)

        # Update the display
        ax.set_title(f"BFS Visualizer - Visiting Node: {current_node}")
        fig.canvas.draw()
        plt.pause(0.5)  # More reliable than time.sleep()

        # Visit neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Final visualization
    ax.set_title("BFS Complete")
    plt.ioff()
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

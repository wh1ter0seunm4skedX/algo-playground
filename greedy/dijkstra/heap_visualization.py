import networkx as nx
import matplotlib.pyplot as plt

def visualize_min_heap(heap, ax):
    ax.clear()  # Clear the previous heap display

    # Create a directed graph representing the heap as a binary tree
    G = nx.DiGraph()
    positions = {}  # To store node positions for drawing

    # Build the binary tree structure from the heap
    for i, (distance, node) in enumerate(heap):
        G.add_node(i, label=f"({distance}, {node})")
        x_position = i  # X position for layout

        # Calculate parent-child relationships
        if i > 0:  # Skip the root node
            parent_index = (i - 1) // 2
            G.add_edge(parent_index, i)

        # Set the position for this node in the tree
        level = i.bit_length() - 1  # Determine which level of the tree this node is on
        positions[i] = (x_position, -level)

    # Draw the tree-like structure of the heap
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos=positions, labels=labels, with_labels=True, node_color='skyblue',
            node_size=1500, font_size=8, font_weight='bold', ax=ax, arrows=False)
    ax.set_title("Min-Heap (Tree Representation)")
    ax.axis('off')  # Turn off axis

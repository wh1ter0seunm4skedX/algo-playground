import networkx as nx
import matplotlib.pyplot as plt

def visualize_min_heap(heap, ax):
    ax.clear()

    # Create directed graph to represent heap as a tree
    G = nx.DiGraph()
    positions = {}

    for i, (distance, node) in enumerate(heap):
        G.add_node(i, label=f"({distance}, {node})")

        # Parent-child relationships
        if i > 0:
            parent = (i - 1) // 2
            G.add_edge(parent, i)

        # Tree positioning
        level = i.bit_length() - 1
        positions[i] = (i, -level)

    # Draw tree-like min-heap
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos=positions, labels=labels, with_labels=True, node_color='skyblue',
            node_size=1500, font_size=8, font_weight='bold', ax=ax, arrows=False)
    ax.set_title("Min-Heap (Tree Representation)")
    ax.axis('off')

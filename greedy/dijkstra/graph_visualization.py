import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pseudocode import pseudocode_lines
from heap_visualization import visualize_min_heap

def visualize_graph(graph, distances, predecessor, heap_state, iteration, current_node, ax1, ax2, ax3):
    ax1.clear()  # Clear the graph plot
    ax2.clear()  # Clear the pseudocode plot

    # Create graph
    G = nx.Graph()
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10, font_weight='bold', ax=ax1)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax1)

    # Highlight visited nodes and paths
    visited_nodes = [node for node in distances if distances[node] < float('inf')]
    nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color='lightgreen', node_size=800, ax=ax1)
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='orange', node_size=800, ax=ax1)

    path_edges = [(predecessor[node], node) for node in predecessor if predecessor[node] is not None]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2, ax=ax1)

    # Legend
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='lightblue', markersize=10, label='Unvisited Node'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgreen', markersize=10, label='Visited Node'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', markersize=10, label='Current Node'),
        Line2D([0], [0], color='red', lw=2, label='Shortest Path')
    ]
    ax1.legend(handles=legend_elements, loc='upper left')
    ax1.set_title(f"Iteration {iteration}: Visiting '{current_node}'")

    # Highlight the current step in the pseudocode
    highlight_line = determine_highlight_line(iteration)
    y = 1.0  # Y-position for text
    for i, line in enumerate(pseudocode_lines):
        color = 'red' if i == highlight_line else 'black'
        ax2.text(0.05, y, line, fontsize=10, family='monospace', color=color, verticalalignment='top')
        y -= 0.07
    ax2.axis('off')  # Turn off axis for pseudocode display

    # Visualize the min-heap as a tree structure
    visualize_min_heap(heap_state, ax3)


def determine_highlight_line(iteration):
    """
    Determine which pseudocode line to highlight based on the current iteration.
    """
    if iteration == 0:
        return 1  # Highlight the function initialization
    elif iteration == 1:
        return 7  # Highlight "while Q is not empty"
    elif iteration == 2:
        return 8  # Highlight "U <- extract min from Q"
    elif iteration == 3:
        return 9  # Highlight "for each unvisited neighbor V"
    elif iteration == 4:
        return 10  # Highlight distance comparison
    else:
        return 13  # Final step or any remaining state

def handle_key(event, iteration_data, graph, current_index, ax1, ax2, ax3):
    if event.key == 'right' and current_index[0] < len(iteration_data) - 1:
        current_index[0] += 1
    elif event.key == 'left' and current_index[0] > 0:
        current_index[0] -= 1

    distances, predecessor, heap_state, iteration, current_node = iteration_data[current_index[0]]
    visualize_graph(graph, distances, predecessor, heap_state, iteration, current_node, ax1, ax2, ax3)
    plt.draw()  # Redraw the updated figure

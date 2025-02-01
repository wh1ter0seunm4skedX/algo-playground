import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pseudocode import pseudocode

def visualize_graph(graph, distances, predecessor, iteration, current_node, ax1, ax2):
    ax1.clear()  # Clear the plot before drawing
    ax2.clear()  # Clear the pseudocode text area

    G = nx.Graph()
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10, font_weight='bold', ax=ax1)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax1)

    visited_nodes = [node for node in distances if distances[node] < float('inf')]
    nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color='lightgreen', node_size=800, ax=ax1)
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='orange', node_size=800, ax=ax1)

    path_edges = [(predecessor[node], node) for node in predecessor if predecessor[node] is not None]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2, ax=ax1)

    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='lightblue', markersize=10, label='Unvisited Node'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgreen', markersize=10, label='Visited Node'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', markersize=10, label='Current Node'),
        Line2D([0], [0], color='red', lw=2, label='Shortest Path')
    ]
    ax1.legend(handles=legend_elements, loc='upper left')
    ax1.set_title(f"Iteration {iteration}: Visiting '{current_node}'")

    ax2.axis('off')
    ax2.text(0, 1, pseudocode, fontsize=12, family='monospace', verticalalignment='top')

def handle_key(event, iteration_data, graph, current_index, ax1, ax2):
    if event.key == 'right' and current_index[0] < len(iteration_data) - 1:
        current_index[0] += 1
    elif event.key == 'left' and current_index[0] > 0:
        current_index[0] -= 1

    distances, predecessor, iteration, current_node = iteration_data[current_index[0]]
    visualize_graph(graph, distances, predecessor, iteration, current_node, ax1, ax2)
    plt.draw()  # Redraw the updated figure

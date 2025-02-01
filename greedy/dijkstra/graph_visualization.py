import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pseudocode import pseudocode_lines
from heap_visualization import visualize_min_heap
from decision_visualization import visualize_decisions
from matplotlib.table import Table

def visualize_graph(graph, distances, predecessor, heap_state, iteration, current_node, decisions, ax1, ax2, ax3, ax4, ax5):
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    ax5.clear()

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

    # Highlight the current pseudocode line
    highlight_line = determine_highlight_line(iteration)
    y = 1.0
    for i, line in enumerate(pseudocode_lines):
        color = 'red' if i == highlight_line else 'black'
        ax2.text(0.05, y, line, fontsize=10, family='monospace', color=color, verticalalignment='top')
        y -= 0.07
    ax2.axis('off')

    visualize_min_heap(heap_state, ax3)
    visualize_decisions(decisions, ax4)

    # Extract nodes being updated
    updated_nodes = [decision.split(":")[0].strip().split(" ")[-1] for decision in decisions if "Updating" in decision]
    visualize_table(graph, distances, predecessor, updated_nodes, ax5)

def determine_highlight_line(iteration):
    # Updated highlight logic to reflect correct progression
    highlight_lines = {
        0: 1,   # Initialization
        1: 4,   # Start node exploration
        2: 7,   # Update neighbors
        3: 8,   # Continue exploring unvisited nodes
        4: 10,  # Prioritize next shortest path
        5: 13   # Completion and result gathering
    }
    return highlight_lines.get(iteration, 13)

def visualize_table(graph, distances, predecessor, updated_nodes, ax):
    ax.clear()
    table = Table(ax, bbox=[0, 0, 1, 1])
    ax.set_title("Current State of Distances and Paths")

    # Table header
    columns = ["Vertex", "Known", "Cost", "Path"]
    for i, column in enumerate(columns):
        cell = table.add_cell(0, i, width=0.2, height=0.1, text=column, loc='center', facecolor='gray')
        cell.get_text().set_color('white')
        cell.get_text().set_weight('bold')

    # Table rows with highlights for updated nodes
    for row_index, node in enumerate(sorted(graph.keys()), start=1):
        known = "Yes" if distances[node] < float('inf') and predecessor[node] is not None else "No"
        cost = distances[node] if distances[node] < float('inf') else "∞"
        path = predecessor[node] if predecessor[node] else "-"

        # Highlight updated rows
        highlight_color = 'yellow' if node in updated_nodes else 'white'

        table.add_cell(row_index, 0, width=0.2, height=0.1, text=node, loc='center', facecolor=highlight_color)
        table.add_cell(row_index, 1, width=0.2, height=0.1, text=known, loc='center', facecolor=highlight_color)
        table.add_cell(row_index, 2, width=0.2, height=0.1, text=str(cost), loc='center', facecolor=highlight_color)
        table.add_cell(row_index, 3, width=0.2, height=0.1, text=path, loc='center', facecolor=highlight_color)

    table.auto_set_font_size(False)
    table.set_fontsize(10)

    ax.add_table(table)
    ax.axis('off')

import heapq
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import random

graph_data = None
iteration_data = []
current_index = 0

graph_options = [
    {
        'name': 'Graph 1',
        'graph': {
            'A': {'B': 2, 'D': 1, 'E': 3},
            'B': {'A': 2, 'C': 4, 'F': 5},
            'C': {'B': 4, 'D': 2, 'G': 1},
            'D': {'A': 1, 'C': 2, 'H': 4},
            'E': {'A': 3, 'F': 1, 'I': 2},
            'F': {'B': 5, 'E': 1, 'J': 3},
            'G': {'C': 1, 'H': 2},
            'H': {'D': 4, 'G': 2, 'J': 2},
            'I': {'E': 2, 'J': 1},
            'J': {'F': 3, 'H': 2, 'I': 1}
        }
    },
    {
        'name': 'Graph 2',
        'graph': {
            'A': {'B': 3, 'C': 1, 'D': 2},
            'B': {'A': 3, 'E': 4, 'F': 5},
            'C': {'A': 1, 'G': 2},
            'D': {'A': 2, 'H': 3},
            'E': {'B': 4, 'I': 1},
            'F': {'B': 5, 'J': 2},
            'G': {'C': 2, 'H': 1},
            'H': {'D': 3, 'G': 1},
            'I': {'E': 1, 'J': 3},
            'J': {'F': 2, 'I': 3}
        }
    },
    {
        'name': 'Graph 3',
        'graph': {
            'X': {'Y': 4, 'Z': 2, 'W': 3},
            'Y': {'X': 4, 'V': 1, 'U': 5},
            'Z': {'X': 2, 'T': 6},
            'W': {'X': 3, 'S': 2},
            'V': {'Y': 1, 'T': 3},
            'U': {'Y': 5, 'S': 1},
            'T': {'V': 3, 'Z': 6},
            'S': {'W': 2, 'U': 1}
        }
    }
]

def dijkstra(graph, start_node):
    global iteration_data
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    predecessor = {node: None for node in graph}

    iteration = 0
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        # Store state for each iteration
        iteration_data.append((distances.copy(), predecessor.copy(), iteration, current_node))
        iteration += 1
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessor[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

def visualize_graph(graph, distances, predecessor, iteration, current_node):
    G = nx.Graph()
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    plt.clf()  # Clear previous plot
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Highlight visited nodes and paths
    visited_nodes = [node for node in distances if distances[node] < float('inf')]
    nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color='lightgreen', node_size=800)
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='orange', node_size=800)

    path_edges = [(predecessor[node], node) for node in predecessor if predecessor[node] is not None]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    # Add legend
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='lightblue', markersize=10, label='Unvisited Node'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgreen', markersize=10, label='Visited Node'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', markersize=10, label='Current Node'),
        Line2D([0], [0], color='red', lw=2, label='Shortest Path')
    ]
    plt.legend(handles=legend_elements, loc='upper left')

    plt.title(f"Iteration {iteration}: Visiting '{current_node}'")
    plt.draw()

def on_key(event):
    global current_index
    if event.key == 'right' and current_index < len(iteration_data) - 1:
        current_index += 1
    elif event.key == 'left' and current_index > 0:
        current_index -= 1
    distances, predecessor, iteration, current_node = iteration_data[current_index]
    visualize_graph(graph_data, distances, predecessor, iteration, current_node)

def choose_graph():
    print("Choose a graph:")
    for i, option in enumerate(graph_options):
        print(f"{i + 1}. {option['name']}")
    choice = int(input("Enter the number of the graph you want to visualize: ")) - 1
    return graph_options[choice]['graph']

if __name__ == "__main__":
    graph_data = choose_graph()
    start_node = random.choice(list(graph_data.keys()))
    print(f"Randomly chosen start node: {start_node}")
    dijkstra(graph_data, start_node)

    # Display initial iteration
    distances, predecessor, iteration, current_node = iteration_data[0]
    visualize_graph(graph_data, distances, predecessor, iteration, current_node)

    # Connect key press event and start the event loop
    plt.gcf().canvas.mpl_connect('key_press_event', on_key)
    plt.show()

import heapq
import networkx as nx
import matplotlib.pyplot as plt

graph_data = None
iteration_data = []
current_index = 0

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

if __name__ == "__main__":
    example_graph = {
        'A': {'B': 2, 'D': 1},
        'B': {'A': 2, 'D': 2, 'E': 3},
        'C': {'E': 1},
        'D': {'A': 1, 'B': 2, 'E': 1},
        'E': {'B': 3, 'D': 1, 'C': 1}
    }

    graph_data = example_graph
    dijkstra(example_graph, 'A')

    # Display initial iteration
    distances, predecessor, iteration, current_node = iteration_data[0]
    visualize_graph(graph_data, distances, predecessor, iteration, current_node)

    # Connect key press event and start the event loop
    plt.gcf().canvas.mpl_connect('key_press_event', on_key)
    plt.show()

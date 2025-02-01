import random
from dijkstra import dijkstra
from graphs import choose_graph
from graph_visualization import visualize_graph, handle_key
import matplotlib.pyplot as plt

if __name__ == "__main__":
    graph_data = choose_graph()
    start_node = random.choice(list(graph_data.keys()))
    print(f"Randomly chosen start node: {start_node}")
    iteration_data = dijkstra(graph_data, start_node)

    # Create subplots for the graph, pseudocode, and min-heap
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 7), gridspec_kw={'width_ratios': [2, 1, 1]})
    distances, predecessor, heap_state, iteration, current_node = iteration_data[0]
    visualize_graph(graph_data, distances, predecessor, heap_state, iteration, current_node, ax1, ax2, ax3)

    current_index = [0]  # Mutable list to track the current iteration

    plt.gcf().canvas.mpl_connect(
        'key_press_event',
        lambda event: handle_key(event, iteration_data, graph_data, current_index, ax1, ax2, ax3)
    )
    plt.show()

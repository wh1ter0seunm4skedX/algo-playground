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

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), gridspec_kw={'width_ratios': [2, 1]})
    distances, predecessor, iteration, current_node = iteration_data[0]
    visualize_graph(graph_data, distances, predecessor, iteration, current_node, ax1, ax2)

    current_index = [0]  # Mutable list to track the current iteration

    plt.gcf().canvas.mpl_connect('key_press_event', lambda event: handle_key(event, iteration_data, graph_data, current_index, ax1, ax2))
    plt.show()

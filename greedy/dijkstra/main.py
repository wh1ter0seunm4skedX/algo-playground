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

    # Create subplots
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(24, 7), gridspec_kw={'width_ratios': [2, 1, 1, 1]})
    distances, predecessor, heap_state, iteration, current_node, decisions = iteration_data[0]
    visualize_graph(graph_data, distances, predecessor, heap_state, iteration, current_node, decisions, ax1, ax2, ax3, ax4)

    current_index = [0]

    def handle_key(event):
        if event.key == 'right' and current_index[0] < len(iteration_data) - 1:
            current_index[0] += 1
        elif event.key == 'left' and current_index[0] > 0:
            current_index[0] -= 1
        distances, predecessor, heap_state, iteration, current_node, decisions = iteration_data[current_index[0]]
        visualize_graph(graph_data, distances, predecessor, heap_state, iteration, current_node, decisions, ax1, ax2, ax3, ax4)
        plt.draw()

    plt.gcf().canvas.mpl_connect('key_press_event', handle_key)
    plt.show()

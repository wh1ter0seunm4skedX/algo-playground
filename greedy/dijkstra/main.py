from dijkstra import dijkstra
from graphs import choose_graph
from graph_visualization import visualize_graph
import matplotlib.pyplot as plt

if __name__ == "__main__":
    graph_data = choose_graph()
    start_node = 'A'

    # Initial iteration data (all distances set to ∞ except start)
    initial_distances = {node: float('inf') for node in graph_data}
    initial_distances[start_node] = 0
    initial_predecessor = {node: None for node in graph_data}
    initial_iteration_data = [(initial_distances, initial_predecessor, [], 0, start_node, [])]

    # Compute the rest of the iterations using Dijkstra’s algorithm
    iteration_data = initial_iteration_data + dijkstra(graph_data, start_node)

    fig, axes = plt.subplots(3, 2, figsize=(18, 15))
    ax1, ax2 = axes[0]
    ax3, ax4 = axes[1]
    ax5, ax_empty = axes[2]

    for ax in [ax1, ax2, ax3, ax4, ax5]:
        for spine in ax.spines.values():
            spine.set_edgecolor('black')
            spine.set_linewidth(2)

    ax_empty.axis('off')  # Disable the right-bottom axis

    distances, predecessor, heap_state, iteration, current_node, decisions = iteration_data[0]
    visualize_graph(graph_data, distances, predecessor, heap_state, iteration, current_node, decisions, ax1, ax2, ax3, ax4, ax5)

    current_index = [0]

    def handle_key(event):
        if event.key == 'right' and current_index[0] < len(iteration_data) - 1:
            current_index[0] += 1
        elif event.key == 'left' and current_index[0] > 0:
            current_index[0] -= 1
        distances, predecessor, heap_state, iteration, current_node, decisions = iteration_data[current_index[0]]
        visualize_graph(graph_data, distances, predecessor, heap_state, iteration, current_node, decisions, ax1, ax2, ax3, ax4, ax5)
        plt.draw()

    manager = plt.get_current_fig_manager()
    manager.set_window_title("Dijkstra Visualizer")
    plt.gcf().canvas.mpl_connect('key_press_event', handle_key)
    plt.tight_layout()
    plt.show()

import random
from dijkstra import dijkstra
from graphs import choose_graph
from graph_visualization import visualize_graph
import matplotlib.pyplot as plt

if __name__ == "__main__":
    graph_data = choose_graph()
    start_node = 'A'
    iteration_data = dijkstra(graph_data, start_node)

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    ax1, ax2 = axes[0]
    ax3, ax4 = axes[1]

    for ax in [ax1, ax2, ax3, ax4]:
        for spine in ax.spines.values():
            spine.set_edgecolor('black')
            spine.set_linewidth(2)

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

    manager = plt.get_current_fig_manager()
    manager.set_window_title("Dijkstra Visualizer")
    plt.gcf().canvas.mpl_connect('key_press_event', handle_key)
    plt.tight_layout()
    plt.show()

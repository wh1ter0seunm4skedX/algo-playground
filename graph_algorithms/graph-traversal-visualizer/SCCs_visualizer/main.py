import matplotlib.pyplot as plt
from graph import Graph
from kosaraju import Kosaraju
from visualizer import GraphVisualizer

def create_example_graph():
    # Define the number of nodes
    num_nodes = 8

    # Define the edges as per the provided diagram
    edges = [
        (0, 1), (0, 2),
        (1, 3),
        (3, 1), (3, 5),
        (5, 6), (6, 5),
        (5, 7),
        (6, 4),
        (4, 6),
    ]
    return Graph(num_nodes, edges)

def main():
    graph = create_example_graph()
    visualizer = GraphVisualizer(graph)
    visualizer.add_step(title="Original Graph")
    visualizer.display_step()
    
    kosaraju = Kosaraju(graph, visualizer)
    kosaraju.find_sccs()
    
    print("Use left/right arrow keys to navigate")
    plt.gcf().canvas.mpl_connect("key_press_event", visualizer.navigate_steps)
    plt.show()

if __name__ == "__main__":
    main()

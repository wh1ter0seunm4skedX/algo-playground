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
    print("Welcome to the SCC Visualizer using Kosaraju's Algorithm!")
    graph = create_example_graph()
    print(f"Created example graph with {graph.num_nodes} nodes and {len(graph.edges)} edges.")

    # Visualize the original graph
    visualizer = GraphVisualizer(graph)
    visualizer.add_step(
        title="Original Graph",
        highlighted_nodes=None,
        explanation="This is the original graph before any processing."
    )
    visualizer.display_step()  # Display the initial graph
    
    # Step 2: Run Kosaraju's Algorithm
    kosaraju = Kosaraju(graph, visualizer)
    sccs = kosaraju.find_sccs()
    
    # Step 3: Visualize SCCs
    visualizer.add_step(
        title="Strongly Connected Components",
        highlighted_nodes=None,
        explanation="Final output showing all strongly connected components."
    )
    visualizer.display_step()
    
    # Connect keyboard navigation
    print("Press the right and left arrow keys to navigate through the steps.")
    fig = plt.gcf()  # Get the current figure
    fig.canvas.mpl_connect("key_press_event", visualizer.navigate_steps)
    plt.show()

if __name__ == "__main__":
    main()

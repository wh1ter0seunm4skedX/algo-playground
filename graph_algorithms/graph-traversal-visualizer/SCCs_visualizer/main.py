import matplotlib.pyplot as plt
from graph import Graph
from kosaraju import Kosaraju
from visualizer import GraphVisualizer
from random_graph import RandomGraph

def main():
    print("Welcome to the SCC Visualizer using Kosaraju's Algorithm!")
    random_graph = RandomGraph()
    graph = random_graph.create_random_graph()
    print(f"Generated graph with {graph.num_nodes} nodes and {len(graph.edges)} edges.")

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
    
    print("Press the right and left arrow keys to navigate through the steps.")
    plt.gcf().canvas.mpl_connect("key_press_event", visualizer.navigate_steps)
    plt.show()

if __name__ == "__main__":
    main()

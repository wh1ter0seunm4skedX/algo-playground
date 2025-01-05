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
    visualizer.draw_graph(title="Original Graph")
    
    # Step 2: Run Kosaraju's Algorithm
    kosaraju = Kosaraju(graph, visualizer)
    sccs = kosaraju.find_sccs()
    
    # Step 3: Visualize SCCs
    visualizer.draw_sccs(sccs, title="Strongly Connected Components")
    
if __name__ == "__main__":
    main()

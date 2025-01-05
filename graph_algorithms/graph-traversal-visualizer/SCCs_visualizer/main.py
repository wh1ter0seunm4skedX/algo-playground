from graph import Graph
from kosaraju import Kosaraju
from visualizer import GraphVisualizer

def main():
    print("Welcome to the SCC Visualizer using Kosaraju's Algorithm!")
    
    # Input: Number of nodes and edges
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    num_edges = int(input("Enter the number of edges in the graph: "))
    
    print("Enter edges in the format 'source destination':")
    edges = []
    for _ in range(num_edges):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    # Step 1: Create the graph
    graph = Graph(num_nodes, edges)
    visualizer = GraphVisualizer(graph)
    visualizer.draw_graph(title="Original Graph")
    
    # Step 2: Run Kosaraju's Algorithm
    kosaraju = Kosaraju(graph)
    sccs = kosaraju.find_sccs()
    
    # Step 3: Visualize SCCs
    visualizer.draw_sccs(sccs, title="Strongly Connected Components")
    
if __name__ == "__main__":
    main()

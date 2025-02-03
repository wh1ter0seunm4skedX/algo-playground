from prim import prim_algorithm
from graph import Graph
from graph_visualizer import display_graph

if __name__ == "__main__":
    # Graph definition
    edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 4),
        (3, 4, 2),
        (4, 0, 5)
    ]
    
    graph = Graph(edges)
    
    # Run Prim's algorithm and display steps in the CLI
    mst_edges = prim_algorithm(graph, start_node=0)
    
    # Display the graph with the MST highlighted
    display_graph(edges, "Graph with MST Highlighted", mst_edges)

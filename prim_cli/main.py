from prim import prim_algorithm
from graph import Graph

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
    
    # Initialize and run
    graph = Graph(edges)
    prim_algorithm(graph, start_node=0)

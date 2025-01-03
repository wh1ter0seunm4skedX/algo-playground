from graph import Graph
from traversal import dfs_steps, bfs_steps
from visualizer import GraphVisualizer
import sys
import os
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama

def create_simple_path():
    """Creates a simple path graph: 1-2-3-4-5"""
    g = Graph()
    vertices = range(1, 6)
    edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_binary_tree():
    """Creates a binary tree graph"""
    g = Graph()
    vertices = range(1, 8)
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_cycle():
    """Creates a cycle graph: 1-2-3-4-1"""
    g = Graph()
    vertices = range(1, 5)
    edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_complex_path_1():
    """Creates a complex path graph with branches: 1-2-3-4-5-6-7-8-9-10 with side branches"""
    g = Graph()
    vertices = range(1, 11)
    edges = [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), 
        (6, 7), (7, 8), (8, 9), (9, 10),
        (3, 11), (11, 12),  # branch from 3
        (5, 13), (13, 14),  # branch from 5
        (8, 15)            # branch from 8
    ]
    for vertex in list(vertices) + [11, 12, 13, 14, 15]:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_complex_path_2():
    """Creates another complex path graph with different branches"""
    g = Graph()
    vertices = range(1, 11)
    edges = [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), 
        (6, 7), (7, 8), (8, 9), (9, 10),
        (2, 11), (11, 12),  # branch from 2
        (4, 13), (13, 14),  # branch from 4
        (7, 15)            # branch from 7
    ]
    for vertex in list(vertices) + [11, 12, 13, 14, 15]:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_complex_tree_1():
    """Creates a larger binary tree with additional connections"""
    g = Graph()
    vertices = range(1, 16)
    edges = [
        (1, 2), (1, 3),      # level 1
        (2, 4), (2, 5),      # level 2 left
        (3, 6), (3, 7),      # level 2 right
        (4, 8), (4, 9),      # level 3
        (5, 10), (5, 11),
        (6, 12), (6, 13),
        (7, 14), (7, 15),
        (8, 9), (10, 11),    # horizontal connections
        (12, 13), (14, 15)
    ]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_complex_tree_2():
    """Creates another larger binary tree with different connections"""
    g = Graph()
    vertices = range(1, 16)
    edges = [
        (1, 2), (1, 3),      # level 1
        (2, 4), (2, 5),      # level 2 left
        (3, 6), (3, 7),      # level 2 right
        (4, 8), (4, 9),      # level 3
        (5, 10), (5, 11),
        (6, 12), (6, 13),
        (7, 14), (7, 15),
        (8, 10), (9, 11),    # different horizontal connections
        (12, 14), (13, 15)
    ]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_complex_cycle_1():
    """Creates a cycle graph with inner connections: 10 vertices with cross-edges"""
    g = Graph()
    vertices = range(1, 11)
    edges = [
        # Outer cycle
        (1, 2), (2, 3), (3, 4), (4, 5),
        (5, 6), (6, 7), (7, 8), (8, 9),
        (9, 10), (10, 1),
        # Cross connections
        (1, 6), (2, 7), (3, 8),
        (4, 9), (5, 10)
    ]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_complex_cycle_2():
    """Creates another cycle graph with different inner connections"""
    g = Graph()
    vertices = range(1, 11)
    edges = [
        # Outer cycle
        (1, 2), (2, 3), (3, 4), (4, 5),
        (5, 6), (6, 7), (7, 8), (8, 9),
        (9, 10), (10, 1),
        # Different cross connections
        (1, 7), (2, 8), (3, 9),
        (4, 10), (5, 6)
    ]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_large_path():
    """Creates a large path graph with 25 vertices and multiple branches"""
    g = Graph()
    vertices = range(1, 26)
    edges = [
        # Main path
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
        (6, 7), (7, 8), (8, 9), (9, 10), (10, 11),
        (11, 12), (12, 13), (13, 14), (14, 15),
        # Branches
        (3, 16), (16, 17), (17, 18),  # Branch 1
        (7, 19), (19, 20), (20, 21),  # Branch 2
        (11, 22), (22, 23),           # Branch 3
        (14, 24), (24, 25)            # Branch 4
    ]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_large_tree():
    """Creates a large tree with 25 vertices"""
    g = Graph()
    vertices = range(1, 26)
    edges = [
        # Level 1
        (1, 2), (1, 3), (1, 4),
        # Level 2
        (2, 5), (2, 6), (3, 7), (3, 8), (4, 9), (4, 10),
        # Level 3
        (5, 11), (5, 12), (6, 13), (6, 14), (7, 15), (7, 16),
        (8, 17), (8, 18), (9, 19), (9, 20), (10, 21), (10, 22),
        # Level 4
        (11, 23), (12, 24), (13, 25),
        # Cross connections
        (15, 16), (17, 18), (19, 20), (21, 22)
    ]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_large_cycle():
    """Creates a large cycle with 25 vertices and inner connections"""
    g = Graph()
    vertices = range(1, 26)
    # Create outer cycle
    cycle_edges = [(i, i+1) for i in range(1, 25)] + [(25, 1)]
    # Create inner connections (every 5th vertex)
    inner_edges = [
        (1, 6), (6, 11), (11, 16), (16, 21),
        (2, 7), (7, 12), (12, 17), (17, 22),
        (3, 8), (8, 13), (13, 18), (18, 23),
        (4, 9), (9, 14), (14, 19), (19, 24),
        (5, 10), (10, 15), (15, 20), (20, 25)
    ]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in cycle_edges + inner_edges:
        g.add_edge(v1, v2)
    return g

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu(title, options):
    clear_screen()
    print(f"\n=== {title} ===")
    print("Select an option:")
    for idx, option in enumerate(options, 1):
        name = option[0]
        desc = option[2] if len(option) > 2 else ""
        print(f"{idx}. {name}")
        if desc:
            if "Path" in name:
                print(f"   {Fore.CYAN}{desc}{Style.RESET_ALL}")
            elif "Tree" in name:
                print(f"   {Fore.GREEN}{desc}{Style.RESET_ALL}")
            elif "Cycle" in name:
                print(f"   {Fore.MAGENTA}{desc}{Style.RESET_ALL}")
    print("0. Exit")

def get_valid_input(max_value):
    while True:
        try:
            choice = int(input(f"\nEnter your choice (0-{max_value}): "))
            if 0 <= choice <= max_value:
                return choice
            print(f"Please enter a number between 0 and {max_value}")
        except ValueError:
            print("Please enter a valid number")

def interactive_graph_learning():
    algorithms = [
        ("Depth-First Search (DFS)", dfs_steps, "Explores deeply before backtracking"),
        ("Breadth-First Search (BFS)", bfs_steps, "Explores nearest neighbors first")
    ]
    
    graph_types = [
        ("Path", [
            ("Complex Path 1", create_complex_path_1, "Linear path with side branches"),
            ("Complex Path 2", create_complex_path_2, "Another path variant with branches"),
            ("Large Path", create_large_path, "Extended path with multiple branches")
        ]),
        ("Tree", [
            ("Complex Tree 1", create_complex_tree_1, "Binary tree with horizontal connections"),
            ("Complex Tree 2", create_complex_tree_2, "Binary tree with diagonal connections"),
            ("Large Tree", create_large_tree, "Multi-level tree with cross connections")
        ]),
        ("Cycle", [
            ("Complex Cycle 1", create_complex_cycle_1, "Cycle with cross-edges"),
            ("Complex Cycle 2", create_complex_cycle_2, "Cycle with different inner connections"),
            ("Large Cycle", create_large_cycle, "Large cycle with systematic inner connections")
        ])
    ]

    while True:
        try:
            # Algorithm selection menu
            print_menu("Select Traversal Algorithm", algorithms)
            algo_choice = get_valid_input(len(algorithms))
            
            if algo_choice == 0:
                print("\nGoodbye!")
                return
            
            selected_algo = algorithms[algo_choice - 1]
            algo_name, algo_func = selected_algo[0], selected_algo[1]
            
            while True:
                try:
                    # Graph type selection menu
                    print_menu("Select Graph Type", graph_types)
                    graph_type_choice = get_valid_input(len(graph_types))
                    
                    if graph_type_choice == 0:
                        break  # Go back to algorithm selection
                    
                    graph_type_name, graph_examples = graph_types[graph_type_choice - 1]
                    
                    while True:
                        try:
                            # Graph example selection menu
                            print_menu(f"Select {graph_type_name} Example", graph_examples)
                            graph_example_choice = get_valid_input(len(graph_examples))
                            
                            if graph_example_choice == 0:
                                break  # Go back to graph type selection
                            
                            selected_example = graph_examples[graph_example_choice - 1]
                            graph_name, graph_func = selected_example[0], selected_example[1]  # Only get first two elements
                            
                            # Create visualization
                            clear_screen()
                            
                            graph = graph_func()
                            visualizer = GraphVisualizer(graph)
                            visualizer.set_speed(0.75)
                            
                            if not visualizer.visualize_traversal(
                                algo_func(graph, 1),
                                f"{algo_name} on {graph_name}"
                            ):
                                print("\nGoodbye!")
                                return
                            
                        except Exception as e:
                            print(f"\nError: {e}")
                            input("\nPress Enter to continue...")
                except Exception as e:
                    print(f"\nError: {e}")
                    input("\nPress Enter to continue...")
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        interactive_graph_learning()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)

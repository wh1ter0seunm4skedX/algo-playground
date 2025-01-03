from src.graph import Graph
from src.dfs import DFS
from src.visualizer import DFSVisualizer
from src.problems.all_paths import AllPathsProblem
from src.problems.cycle_detection import CycleDetectionProblem
from src.problems.topological_sort import TopologicalSortProblem
from src.problems.connected_components import ConnectedComponentsProblem

def show_menu():
    print("Select a problem to solve using DFS:")
    print("1. Find all paths between two nodes in a graph")
    print("2. Detect cycles in a directed graph")
    print("3. Perform topological sorting")
    print("4. Find connected components in an undirected graph")
    print("5. Exit")

def solve_all_paths(graph, dfs):
    start = int(input("Enter the starting node: "))
    end = int(input("Enter the target node: "))
    problem = AllPathsProblem(dfs)
    paths = problem.find_all_paths(start, end)
    print(f"All paths from {start} to {end}: {paths}")
    visualizer = DFSVisualizer(graph, dfs)
    visualizer.visualize(paths)

def solve_cycle_detection(graph, dfs):
    problem = CycleDetectionProblem(dfs)
    has_cycle = problem.has_cycle()
    print(f"Graph contains a cycle: {has_cycle}")

def solve_topological_sort(graph, dfs):
    problem = TopologicalSortProblem(dfs)
    sorted_nodes = problem.sort()
    print(f"Topological Sort: {sorted_nodes}")

def solve_connected_components(graph, dfs):
    problem = ConnectedComponentsProblem(dfs)
    components = problem.find_components()
    print(f"Connected components: {components}")

def main():
    graph = Graph()
    graph.add_edges([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

    dfs = DFS(graph)

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            solve_all_paths(graph, dfs)
        elif choice == "2":
            solve_cycle_detection(graph, dfs)
        elif choice == "3":
            solve_topological_sort(graph, dfs)
        elif choice == "4":
            solve_connected_components(graph, dfs)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

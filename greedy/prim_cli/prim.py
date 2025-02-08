import heapq
from cli_helper import print_step
from colorama import Fore, Style

def prim_algorithm(graph, start_node):
    visited = set()
    min_heap = [(0, start_node, None)]  # (weight, node, previous_node)
    mst_edges = []

    print_step(f"{Fore.GREEN}Starting Prim's algorithm at node {start_node}{Style.RESET_ALL}")
    print(f"Initial priority queue: {min_heap}\n")

    while min_heap:
        # Pop the minimum weight edge from the priority queue
        weight, current_node, previous_node = heapq.heappop(min_heap)
        print(f"{Fore.CYAN}[INFO] Popped edge with weight {weight}, current node: {current_node}, previous node: {previous_node}{Style.RESET_ALL}")

        # If the current node is already visited, skip this step
        if current_node in visited:
            print(f"{Fore.RED}[SKIP] Node {current_node} is already visited. Skipping...{Style.RESET_ALL}\n")
            continue

        # Mark the node as visited
        visited.add(current_node)
        print(f"{Fore.YELLOW}[VISIT] Visiting node {current_node}, adding to visited nodes: {visited}{Style.RESET_ALL}")

        # If the edge is valid (previous node exists), add it to the MST
        if previous_node is not None:
            mst_edges.append((previous_node, current_node, weight))
            print(f"{Fore.MAGENTA}[MST] Adding edge ({previous_node} -> {current_node}) with weight {weight} to MST{Style.RESET_ALL}")

        # Explore neighbors of the current node
        for neighbor, edge_weight in graph.get_neighbors(current_node):
            if neighbor not in visited:
                # Add the edge to the priority queue
                heapq.heappush(min_heap, (edge_weight, neighbor, current_node))
                print(f"{Fore.BLUE}[QUEUE] Adding edge ({current_node} -> {neighbor}) with weight {edge_weight} to the priority queue{Style.RESET_ALL}")
        
        # Show the current state of the priority queue after the iteration
        print(f"Current priority queue: {min_heap}\n")

    print_step(f"{Fore.GREEN}Minimum Spanning Tree constructed:{Style.RESET_ALL}")
    for edge in mst_edges:
        print_step(f"{Fore.MAGENTA}Edge {edge[0]} -> {edge[1]} with weight {edge[2]}{Style.RESET_ALL}")

    return mst_edges  # Return MST edges to visualize

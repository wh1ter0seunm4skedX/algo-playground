import heapq
from cli_helper import print_step

def prim_algorithm(graph, start_node):
    visited = set()
    min_heap = [(0, start_node, None)]  # (weight, node, previous_node)
    mst_edges = []

    print_step(f"Starting Prim's algorithm at node {start_node}")

    while min_heap:
        weight, current_node, previous_node = heapq.heappop(min_heap)

        if current_node in visited:
            print_step(f"Node {current_node} is already visited. Skipping...")
            continue

        visited.add(current_node)
        if previous_node is not None:
            mst_edges.append((previous_node, current_node, weight))
            print_step(f"Adding edge ({previous_node} -> {current_node}) with weight {weight} to MST")

        for neighbor, edge_weight in graph.get_neighbors(current_node):
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_node))
                print_step(f"Adding edge ({current_node} -> {neighbor}) with weight {edge_weight} to the priority queue")

    print_step("Minimum Spanning Tree constructed:")
    for edge in mst_edges:
        print_step(f"Edge {edge[0]} -> {edge[1]} with weight {edge[2]}")

    return mst_edges  # Return MST edges to visualize

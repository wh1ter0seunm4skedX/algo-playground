import heapq

def dijkstra(graph, start_node):
    iteration_data = []
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    predecessor = {node: None for node in graph}

    iteration = 0
    while priority_queue:
        heap_state = list(priority_queue)
        heapq.heapify(heap_state)

        current_distance, current_node = heapq.heappop(priority_queue)
        decisions = []  # Track decisions made during this iteration

        if current_distance > distances[current_node]:
            continue

        # Analyze neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            decision_reason = f"Analyzing edge ({current_node}, {neighbor}) with weight {weight}"

            # Handle ties using lexicographic order when weights are equal
            if distance == distances[neighbor]:
                decision_reason += f" - Tie detected, preferring lexicographic order: {min(current_node, neighbor)}"

            if distance < distances[neighbor]:
                decision_reason += f" - Updating {neighbor}: {distances[neighbor]} → {distance}"
                distances[neighbor] = distance
                predecessor[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

            decisions.append(decision_reason)

        iteration_data.append((distances.copy(), predecessor.copy(), heap_state, iteration, current_node, decisions))
        iteration += 1

    return iteration_data

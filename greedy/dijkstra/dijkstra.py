import heapq

def dijkstra(graph, start_node):
    iteration_data = []
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    predecessor = {node: None for node in graph}

    iteration = 0
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        iteration_data.append((distances.copy(), predecessor.copy(), iteration, current_node))
        iteration += 1
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessor[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    return iteration_data

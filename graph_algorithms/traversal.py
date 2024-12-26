def dfs_steps(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            yield vertex, visited.copy(), stack.copy()
            
            for neighbor in reversed(graph.get_neighbors(vertex)):
                if neighbor not in visited:
                    stack.append(neighbor)

def bfs_steps(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    
    while queue:
        vertex = queue.pop(0)
        yield vertex, visited.copy(), queue.copy()
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

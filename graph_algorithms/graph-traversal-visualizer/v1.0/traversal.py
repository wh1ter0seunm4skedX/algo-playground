def dfs_steps(graph, start):
    visited = set()
    stack = [start]
    current = start
    
    # Initial state
    yield current, visited.copy(), stack.copy()
    
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            yield current, visited.copy(), stack.copy()
            
            for neighbor in reversed(graph.get_neighbors(current)):
                if neighbor not in visited:
                    stack.append(neighbor)
            
            # Only yield stack updates if there are unvisited neighbors
            if stack:
                yield current, visited.copy(), stack.copy()

def bfs_steps(graph, start):
    visited = set()
    queue = [start]
    current = start
    
    # Initial state
    yield current, visited.copy(), queue.copy()
    
    visited.add(start)
    while queue:
        current = queue.pop(0)
        yield current, visited.copy(), queue.copy()
        
        # Sort neighbors to process smaller vertices first
        neighbors = sorted(graph.get_neighbors(current))
        neighbors_added = False
        
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                neighbors_added = True
                # Show intermediate state after each neighbor addition
                yield current, visited.copy(), queue.copy()

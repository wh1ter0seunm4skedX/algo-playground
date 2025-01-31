from collections import deque

def draw_grid(game_map, visited, start, goal):
    """
    Print the grid showing visited cells, start, goal, and obstacles.
    """
    rows = len(game_map)
    cols = len(game_map[0]) if rows > 0 else 0

    for r in range(rows):
        row_str = []
        for c in range(cols):
            if (r, c) == start:
                row_str.append('S')
            elif (r, c) == goal:
                row_str.append('G')
            elif game_map[r][c] == 1:
                row_str.append('#')
            elif (r, c) in visited:
                row_str.append('v')
            else:
                row_str.append('.')
        print(" ".join(row_str))
    print()  # Blank line for spacing

def bfs_with_step_input(game_map, start, goal):
    """
    Perform BFS to find the shortest path from start to goal in a 2D grid,
    pausing each time before moving on to the next step of the search.
    
    :param game_map: 2D list representing the game map, 0 = free cell, 1 = obstacle
    :param start: (row, col) tuple for the starting position
    :param goal: (row, col) tuple for the goal position
    :return: A list of cells (row, col) representing the path from start to goal.
             If no path is found or the user quits, returns an empty list.
    """
    # Basic checks
    if not game_map or not game_map[0]:
        return []
    if start == goal:
        return [start]
    
    rows = len(game_map)
    cols = len(game_map[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    
    # Initial print
    print("Initial Grid:")
    draw_grid(game_map, visited, start, goal)
    user_input = input("Press Enter to continue (or 'q' to quit): ").strip().lower()
    if user_input == 'q':
        return []
    
    # BFS Loop
    while queue:
        current = queue.popleft()
        current_row, current_col = current
        
        print(f"Processing cell: {current}")
        draw_grid(game_map, visited, start, goal)
        user_input = input("Press Enter to continue (or 'q' to quit): ").strip().lower()
        if user_input == 'q':
            return []
        
        # Check if this is the goal
        if current == goal:
            return reconstruct_path(parent, goal)
        
        # Enqueue valid neighbors
        for dr, dc in directions:
            nr, nc = current_row + dr, current_col + dc
            # Must be within bounds, not an obstacle, and not visited
            if (0 <= nr < rows and 0 <= nc < cols 
                and game_map[nr][nc] == 0 
                and (nr, nc) not in visited):
                
                visited.add((nr, nc))
                parent[(nr, nc)] = current
                queue.append((nr, nc))
    
    return []  # No path found

def reconstruct_path(parent, goal):
    """
    Reconstruct the path from the goal back to the start
    using the parent dictionary.
    """
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

# ------------------------------------------------------------------
# Example usage
if __name__ == "__main__":
    # Example 5x5 grid
    # 0 = free cell, 1 = obstacle
    game_map = [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    start_position = (0, 0)
    goal_position = (4, 4)

    path = bfs_with_step_input(game_map, start_position, goal_position)
    
    if path:
        print("\nShortest path (from start to goal):")
        for step in path:
            print(step)
    else:
        print("\nNo path found (or user quit).")

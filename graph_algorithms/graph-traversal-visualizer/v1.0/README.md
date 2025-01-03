# Graph Traversal Visualizer

An interactive visualization tool for understanding graph traversal algorithms (DFS and BFS) with various graph structures.

## Features

- Interactive CLI menu system
- Real-time visualization of traversal algorithms
- Multiple graph types with complex structures
- Step-by-step animation control
- Educational information panel

## Installation

1. Clone the repository
2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the visualizer:
```bash
python demo.py
```

### Menu Structure

1. Select Traversal Algorithm:
   - Depth-First Search (DFS)
   - Breadth-First Search (BFS)

2. Select Graph Type:
   - Path (Complex branching paths)
   - Tree (Binary trees with additional connections)
   - Cycle (Cycles with cross-edges)

3. Select specific graph example from each type

### Visualization Controls

- `<` : Step backwards
- `||`: Pause/Play animation
- `>` : Step forward
- `>>`: Next visualization
- `X` : Exit program

### Color Coding

- Red: Current vertex being visited
- Green: Already visited vertices
- Yellow: Vertices in queue/stack
- Light Blue: Unvisited vertices
- Green Edges: Traversed paths
- Gray Edges: Unexplored paths

## Graph Types

### Path Graphs
Complex paths with multiple branches, demonstrating how algorithms handle branching decisions.

### Tree Graphs
Modified binary trees with additional connections, showing traversal patterns in hierarchical structures.

### Cycle Graphs
Circular structures with cross-connections, illustrating how algorithms handle cycles and multiple paths.

## Algorithms

### Depth-First Search (DFS)
- Uses a stack (LIFO)
- Explores as far as possible along each branch before backtracking
- Good for finding paths and exploring tree structures

### Breadth-First Search (BFS)
- Uses a queue (FIFO)
- Explores all vertices at the current depth before moving deeper
- Optimal for finding shortest paths in unweighted graphs

## Contributing

Feel free to contribute by:
- Adding new graph types
- Implementing additional algorithms
- Improving visualizations
- Enhancing documentation

## License

This project is licensed under the MIT License.
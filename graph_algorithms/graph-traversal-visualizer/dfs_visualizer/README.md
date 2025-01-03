# DFS Path Visualizer

An interactive visualization tool for Depth-First Search (DFS) path finding in directed graphs. This tool helps understand how DFS works by visualizing the search process, path discovery, and edge classifications.

## Features

- **Interactive Graph Visualization**
  - Real-time visualization of DFS path finding
  - Step-by-step navigation through paths
  - Edge classification (Tree, Back, Forward, Cross edges)
  - Stack and visited nodes visualization

- **Dynamic Graph Generation**
  - Random graph generation
  - Guaranteed connected graphs
  - Customizable number of nodes and edges

- **Path Finding Controls**
  - Multiple path discovery between nodes
  - Forward and backward stepping
  - Path-by-path navigation

## Controls

- **Navigation**
  - Right Arrow: Next step
  - Left Arrow: Previous step
  - Up Arrow: Next path
  - Down Arrow: Previous path
  - Space: Pause/Resume
  - R: Reset current path
  - N: Generate new random path
  - G: Generate new random graph

## Edge Types

- **Tree Edge** (Green, Solid)
  - Edges that form the DFS tree
  
- **Back Edge** (Red, Dashed)
  - Edges pointing to ancestors in the DFS tree
  
- **Forward Edge** (Blue, Dashed)
  - Edges pointing to descendants in the DFS tree
  
- **Cross Edge** (Purple, Dashed)
  - Edges between nodes not in ancestor-descendant relationship

## Installation

1. Clone the repository
2. Install required packages:
```bash
pip install matplotlib networkx
```

## Usage

Run the main script:
```bash
python -m src.main
```

The visualization will show:
- Graph structure on the left
- DFS state information on the right
  - Current stack
  - Visited nodes
  - Path progress
  - Edge type legend

## Implementation Details

- Uses NetworkX for graph operations
- Matplotlib for visualization
- Custom DFS implementation with edge classification
- Interactive controls using matplotlib event handling

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.
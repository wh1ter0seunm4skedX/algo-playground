from graph import Graph
from traversal import dfs_steps
from visualizer import GraphVisualizer

def all_paths_demo():
    """Find all paths from a start vertex to an end vertex in a graph."""
    g = Graph()
    vertices = range(1, 6)
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    
    start, end = 1, 5
    paths = []
    visualizer = GraphVisualizer(g)
    
    def dfs_all_paths(current, path):
        visualizer.highlight_path(path)
        if current == end:
            paths.append(path.copy())
            visualizer.highlight_path(path, final=True)
            return
        for neighbor in g.get_neighbors(current):
            if neighbor not in path:
                path.append(neighbor)
                dfs_all_paths(neighbor, path)
                path.pop()
    
    dfs_all_paths(start, [start])
    print(f"All paths from {start} to {end}: {paths}")
    visualizer.show()

def connected_components_demo():
    """Find all connected components in a graph."""
    g = Graph()
    vertices = range(1, 11)
    edges = [(1, 2), (2, 3), (4, 5), (6, 7), (7, 8), (8, 9), (9, 10)]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    
    visited = set()
    components = []
    visualizer = GraphVisualizer(g)
    
    def dfs_component(v, component):
        visited.add(v)
        component.append(v)
        visualizer.highlight_path(component)
        for neighbor in g.get_neighbors(v):
            if neighbor not in visited:
                dfs_component(neighbor, component)
    
    for vertex in vertices:
        if vertex not in visited:
            component = []
            dfs_component(vertex, component)
            components.append(component)
    
    print(f"Connected components: {components}")
    visualizer.show()

def dependency_graph_demo():
    """Find a valid build order in a dependency graph."""
    g = Graph()
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [('A', 'D'), ('F', 'B'), ('B', 'D'), ('F', 'A'), ('D', 'C')]
    for vertex in vertices:
        g.add_vertex(vertex)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    
    visited = set()
    stack = []
    visualizer = GraphVisualizer(g)
    
    def dfs_dependency(v):
        visited.add(v)
        visualizer.highlight_path([v])
        for neighbor in g.get_neighbors(v):
            if neighbor not in visited:
                dfs_dependency(neighbor)
        stack.append(v)
    
    for vertex in vertices:
        if vertex not in visited:
            dfs_dependency(vertex)
    
    stack.reverse()
    print(f"Build order: {stack}")
    visualizer.show()

def run_demos():
    print("Running all paths demo...")
    all_paths_demo()
    print("\nRunning connected components demo...")
    connected_components_demo()
    print("\nRunning dependency graph demo...")
    dependency_graph_demo()

if __name__ == "__main__":
    run_demos()
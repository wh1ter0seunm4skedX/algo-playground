class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.paths = []
        self.current_path = []
        self.edge_types = {}  
        self.discovery_time = {}  
        self.finish_time = {}    
        self.time = 0

    def dfs(self, node, target):
        self.time += 1
        self.discovery_time[node] = self.time
        self.visited.add(node)
        self.current_path.append(node)

        if node == target:
            self.paths.append(list(self.current_path))
        else:
            for neighbor in self.graph.get_neighbors(node):
                edge = (node, neighbor)
                # Only process if it's a valid edge in the directed graph
                if not self.graph.has_edge(node, neighbor):
                    continue
                    
                if neighbor not in self.visited:
                    self.edge_types[edge] = 'tree'
                    self.dfs(neighbor, target)
                else:
                    # Classify edge based on discovery and finish times
                    if neighbor in self.current_path:  # Back edge
                        self.edge_types[edge] = 'back'
                    elif neighbor in self.discovery_time:  # Forward or cross edge
                        if self.discovery_time[node] < self.discovery_time[neighbor]:
                            self.edge_types[edge] = 'forward'
                        else:
                            self.edge_types[edge] = 'cross'

        self.time += 1
        self.finish_time[node] = self.time
        self.current_path.pop()
        self.visited.remove(node)

class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.paths = []
        self.current_path = []

    def dfs(self, node, target):
        self.visited.add(node)
        self.current_path.append(node)

        if node == target:
            self.paths.append(list(self.current_path))
        else:
            for neighbor in self.graph.get_neighbors(node):
                if neighbor not in self.visited:
                    self.dfs(neighbor, target)

        self.current_path.pop()
        self.visited.remove(node)

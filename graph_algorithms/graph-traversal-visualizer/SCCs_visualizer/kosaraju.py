class Kosaraju:
    def __init__(self, graph):
        self.graph = graph
        self.num_nodes = graph.num_nodes
        self.visited = [False] * self.num_nodes
        self.stack = []
    
    def _dfs(self, node, graph, result):
        self.visited[node] = True
        for neighbor in graph.get_adj_list()[node]:
            if not self.visited[neighbor]:
                self._dfs(neighbor, graph, result)
        result.append(node)
    
    def _fill_order(self):
        for node in range(self.num_nodes):
            if not self.visited[node]:
                self._dfs(node, self.graph, self.stack)
    
    def find_sccs(self):
        # Step 1: Fill order
        self._fill_order()
        
        # Step 2: Reverse graph
        reversed_graph = self.graph.reverse()
        
        # Step 3: DFS on reversed graph
        self.visited = [False] * self.num_nodes
        sccs = []
        while self.stack:
            node = self.stack.pop()
            if not self.visited[node]:
                scc = []
                self._dfs(node, reversed_graph, scc)
                sccs.append(scc)
        
        return sccs

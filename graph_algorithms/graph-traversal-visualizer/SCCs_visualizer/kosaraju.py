class Kosaraju:
    def __init__(self, graph, visualizer):
        self.graph = graph
        self.visualizer = visualizer
        self.num_nodes = graph.num_nodes
        self.visited = [False] * self.num_nodes
        self.stack = []
    
    def _dfs(self, node, graph, result, title="DFS Progress"):
        self.visited[node] = True
        for neighbor in graph.get_adj_list()[node]:
            if not self.visited[neighbor]:
                self._dfs(neighbor, graph, result, title)
        result.append(node)
        self.visualizer.draw_graph(title=title, highlighted_nodes=[node])
    
    def _fill_order(self):
        for node in range(self.num_nodes):
            if not self.visited[node]:
                self._dfs(node, self.graph, self.stack, title="First DFS (Fill Order)")
    
    def find_sccs(self):
        # Step 1: Fill order
        self._fill_order()
        self.visualizer.draw_graph(title="After First DFS (Stack Order)")
        
        # Step 2: Reverse graph
        reversed_graph = self.graph.reverse()
        self.visualizer.graph = reversed_graph
        self.visualizer._initialize_graph()  # Reinitialize the reversed graph
        self.visualizer.draw_graph(title="Reversed Graph")
        
        # Step 3: DFS on reversed graph
        self.visited = [False] * self.num_nodes
        sccs = []
        while self.stack:
            node = self.stack.pop()
            if not self.visited[node]:
                scc = []
                self._dfs(node, reversed_graph, scc, title="Second DFS (SCC Discovery)")
                sccs.append(scc)
                self.visualizer.draw_graph(title=f"Found SCC: {scc}", highlighted_nodes=scc)
        
        return sccs

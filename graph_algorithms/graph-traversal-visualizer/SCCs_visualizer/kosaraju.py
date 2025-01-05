class Kosaraju:
    def __init__(self, graph, visualizer):
        self.graph = graph
        self.visualizer = visualizer
        self.num_nodes = graph.num_nodes
        self.visited = [False] * self.num_nodes

    def _dfs(self, node, graph, result):
        self.visited[node] = True
        for neighbor in graph.get_adj_list()[node]:
            if not self.visited[neighbor]:
                self._dfs(neighbor, graph, result)
        result.append(node)
        self.visualizer.stack.append(node)
        self.visualizer.add_step(
            title=f"DFS Step",
            highlighted_nodes=[node]
        )

    def _fill_order(self):
        for node in range(self.num_nodes):
            if not self.visited[node]:
                self._dfs(node, self.graph, [])

    def find_sccs(self):
        self._fill_order()
        
        reversed_graph = self.graph.reverse()
        self.visualizer.graph = reversed_graph
        self.visualizer._initialize_graph()
        
        self.visited = [False] * self.num_nodes
        sccs = []
        while self.visualizer.stack:
            node = self.visualizer.stack.pop()
            if not self.visited[node]:
                scc = []
                self._dfs(node, reversed_graph, scc)
                sccs.append(scc)
                self.visualizer.add_step(
                    title=f"SCC Found",
                    highlighted_nodes=scc
                )

        return sccs

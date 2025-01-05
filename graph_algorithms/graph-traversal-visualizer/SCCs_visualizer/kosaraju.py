class Kosaraju:
    def __init__(self, graph, visualizer):
        self.graph = graph
        self.visualizer = visualizer
        self.num_nodes = graph.num_nodes
        self.visited = [False] * self.num_nodes
        self.stack = []

    def _dfs(self, node, graph, result, explanation):
        self.visited[node] = True
        for neighbor in graph.get_adj_list()[node]:
            if not self.visited[neighbor]:
                self._dfs(neighbor, graph, result, explanation)
        result.append(node)
        self.visualizer.add_step(
            title=f"DFS visiting {node}",
            highlighted_nodes=[node],
            explanation=explanation,
        )

    def _fill_order(self):
        explanation = "Performing first DFS to determine finish times of nodes."
        for node in range(self.num_nodes):
            if not self.visited[node]:
                self._dfs(node, self.graph, self.stack, explanation)

    def find_sccs(self):
        # Step 1: Fill order
        self._fill_order()
        self.visualizer.add_step(
            title="Completed First DFS",
            explanation="Finish times determined. Moving to reverse the graph.",
        )

        # Step 2: Reverse graph
        reversed_graph = self.graph.reverse()
        self.visualizer.graph = reversed_graph
        self.visualizer._initialize_graph()
        self.visualizer.add_step(
            title="Reversed Graph",
            explanation="Graph reversed. Performing second DFS.",
        )

        # Step 3: DFS on reversed graph
        self.visited = [False] * self.num_nodes
        sccs = []
        while self.stack:
            node = self.stack.pop()
            if not self.visited[node]:
                scc = []
                self._dfs(node, reversed_graph, scc, explanation="Finding SCC.")
                sccs.append(scc)
                self.visualizer.add_step(
                    title=f"Found SCC: {scc}",
                    highlighted_nodes=scc,
                    explanation="Identified an SCC using the reversed graph.",
                )

        return sccs

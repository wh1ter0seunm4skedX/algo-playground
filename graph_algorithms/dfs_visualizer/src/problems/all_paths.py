class AllPathsProblem:
    def __init__(self, dfs):
        self.dfs = dfs

    def find_all_paths(self, start, end):
        self.dfs.dfs(start, end)
        return self.dfs.paths

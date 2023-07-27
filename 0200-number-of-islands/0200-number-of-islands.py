class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        def dfs(i, j, visited):
            if i >= m or j >= n or i < 0 or j < 0 or (i, j) in visited or grid[i][j] == "0":
                return
            
            visited.add((i, j))
            grid[i][j] = "0"
            dfs(i - 1, j, visited)
            dfs(i + 1, j, visited)
            dfs(i, j - 1, visited)
            dfs(i, j + 1, visited)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j, set())
                    res += 1
        
        return res
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        
        def dfs(i, j, prev, visited):
            if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited or heights[i][j] < prev:
                return
            visited.add((i, j))
            dfs(i + 1, j, heights[i][j], visited)
            dfs(i - 1, j, heights[i][j], visited)
            dfs(i, j + 1, heights[i][j], visited)
            dfs(i, j - 1, heights[i][j], visited)
            
        for i in range(m):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, n - 1, heights[i][n - 1], atl)
        
        for i in range(n):
            dfs(0, i, heights[0][i], pac)
            dfs(m - 1, i, heights[m - 1][i], atl)
        
        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        
        return res
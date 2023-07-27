class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        
        def dfs(i, j, visited, prev):
            if i >= m or j >= n or i < 0 or j < 0 or (i,j) in visited or heights[i][j] < prev:
                return
        
            visited.add((i, j))
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
        
        for i in range(n):
            dfs(0, i, pac, heights[0][i])
            dfs(m - 1, i, atl, heights[m - 1][i])
        
        for i in range(m):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, n - 1, atl, heights[i][n - 1])
        
        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    res.append((i, j))
        
        return res
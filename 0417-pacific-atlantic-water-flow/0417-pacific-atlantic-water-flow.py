class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()
        
        def dfs(i,j, visited, preHeight):
            if (i < 0 or j < 0 or i >= ROWS or j >= COLS or 
                (i,j) in visited or heights[i][j] < preHeight):
                return
            visited.add((i,j))
            dfs(i+1,j,visited,heights[i][j])
            dfs(i-1,j,visited,heights[i][j])
            dfs(i,j+1,visited,heights[i][j])
            dfs(i,j-1,visited,heights[i][j])
        
        for c in range(COLS):
            dfs(0, c, atl, heights[0][c])
            dfs(ROWS-1, c, pac, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, atl, heights[r][0])
            dfs(r, COLS-1, pac, heights[r][COLS-1])
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        
        return res
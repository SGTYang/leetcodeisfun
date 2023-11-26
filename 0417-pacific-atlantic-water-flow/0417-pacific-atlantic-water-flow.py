class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()
        res = []
        
        def dfs(i, j, prev, ocean):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in ocean or prev > heights[i][j]:
                return

            ocean.add((i, j))
            
            dfs(i + 1, j, heights[i][j], ocean)
            dfs(i - 1, j, heights[i][j], ocean)
            dfs(i, j + 1, heights[i][j], ocean)
            dfs(i, j - 1, heights[i][j], ocean)
            
        # find
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols - 1], atl)
        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows - 1][c], atl)
            

        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        
        return res
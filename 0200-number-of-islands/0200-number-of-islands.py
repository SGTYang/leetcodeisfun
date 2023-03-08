class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        ans = 0
        
        def dfs(y,x):
            if y>=m or x>=n or y<0 or x<0 or grid[y][x] == "0":
                return
            
            grid[y][x] = "0"
            
            dfs(y-1,x)
            dfs(y+1,x)
            dfs(y,x-1)
            dfs(y,x+1)
            
            return
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ans += 1
        
        return ans
    
        
            
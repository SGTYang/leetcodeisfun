class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m,n = len(grid), len(grid[0])
        
        def dfs(y,x,island):
            if y>=m or x>=n or y<0 or x<0 or grid[y][x]==0:
                return 0
            
            grid[y][x] = 0
            
            return dfs(y-1,x,island+1)+dfs(y+1,x,island+1)+dfs(y,x-1,island+1)+dfs(y,x+1,island+1)+1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans,dfs(i,j,0))
        
        return ans
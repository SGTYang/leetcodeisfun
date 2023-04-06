class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        ans = 0
        visited = set()
        
        def dfs(i,j):
            if i == m or j == n or i < 0 or j < 0:
                return 0
            
            if grid[i][j] == 1 or (i,j) in visited:
                return 1
            
            visited.add((i,j))
            
            return min(
                dfs(i-1,j),
                dfs(i+1,j),
                dfs(i,j+1),
                dfs(i,j-1),
            )
            
        for i in range(m):
            for j in range(n):
                if not grid[i][j] and (i,j) not in visited:
                    ans += dfs(i,j)
        
        return ans
    
        # 
        
        m,n = len(grid), len(grid[0])
        ans = 0
        
        def dfs(y,x):
            if y>=m or x>=n or y<0 or x<0:
                return False
            
            if grid[y][x] == 1:
                return True
            
            grid[y][x] = 1
            
            res = True
            res &= dfs(y-1,x)
            res &= dfs(y+1,x)
            res &= dfs(y,x-1)
            res &= dfs(y,x+1)
            
            return res
            
            #return dfs(y-1,x) and dfs(y+1,x) and dfs(y,x-1) and dfs(y,x+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dfs(i,j):
                    ans +=1
        
        return ans
    
    # solution 2
        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            if i == n or j == m or i < 0 or j < 0 or grid[i][j]:
                return
            
            grid[i][j] = 1
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and (i in (0, n-1) or j in (0, m-1)):
                    dfs(i, j)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i, j)
                    res += 1
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        diff = [[0 for j in range(n)]for i in range(m)]
        ROW = [0 for i in range(m)]
        COL = [0 for j in range(n)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ROW[i] += 1
        
        for i in range(n):
            for j in range(m):
                if grid[j][i] == 1:
                    COL[i] += 1
        
        for i in range(m):
            for j in range(n):
                diff[i][j] = 2*ROW[i] + 2*COL[j] - m - n
                    
        
        return diff
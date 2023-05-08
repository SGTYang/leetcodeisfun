class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        m = len(mat)
        mid = m//2
        
        for i in range(m):
            res += mat[i][i]
        
        for j in range(m):
            res += mat[m-j-1][j]
            
        if m%2 != 0:
            res -= mat[mid][mid]
            
        return res
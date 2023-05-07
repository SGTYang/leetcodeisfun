class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n * m - 1
        
        while l <= r:
            mid = (l+r)//2
            i,j = mid//m, mid%m
            
            if matrix[i][j] == target:
                return True
            
            if matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i = 0
        
        while i < m and matrix[i][0] <= target:
            l, r = 0, n - 1
            
            while l <= r:
                mid = (l + r) // 2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            i += 1
        
        return False
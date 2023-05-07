class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        i = 0
        
        while i < n and target >= matrix[i][0]:
            l, r = 0, m-1

            while l <= r:
                mid = (l+r)//2
                if matrix[i][mid] == target:
                    return True
                
                if matrix[i][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            i += 1
        
        return False
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l, r = matrix[0][0], matrix[n-1][n-1]
        
        while l < r:
            mid = (l+r)//2
            
            cnt = 0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] <= mid:
                        cnt += 1
            
            if cnt >= k:
                r = mid
            else:
                l = mid + 1 
            
        return l
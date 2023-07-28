class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]
        
        while left < right:
            mid = (left + right) // 2
            
            cnt = 0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] <= mid:
                        cnt += 1
            
            if cnt >= k:
                right = mid
            else:
                left = mid + 1
        
        return left
    
        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]
        
        while left < right:
            mid = (left + right) // 2
            
            count = 0
            row, col = n - 1, 0
            
            while row >= 0 and col < n:
                if matrix[row][col] > mid:
                    row -= 1
                else:
                    count += row + 1
                    col += 1

            if count < k:
                left = mid + 1
            else:
                right = mid
        
        return left
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time: O(m * n)
        # Space: O(m * n)
        
        row = [1] * (n + 1)
        
        for i in range(m - 1):
            tmp_row = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                tmp_row[j] = tmp_row[j + 1] + row[j]
            row = tmp_row
        
        return row[0]
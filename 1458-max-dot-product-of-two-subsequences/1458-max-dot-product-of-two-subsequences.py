class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf') for j in range(n + 1)] for i in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = float('-inf')
                else:
                    curr = nums1[i - 1] * nums2[j - 1] + max(dp[i - 1][j - 1], 0)
                    dp[i][j] = max(curr, dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
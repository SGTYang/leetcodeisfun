class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[nums1[i] * nums2[j] for j in range(n)] for i in range(m)]
        
        for i in range(1, m):
            dp[i][0] = max(dp[i][0], dp[i - 1][0])
        
        for i in range(1, n):
            dp[0][i] = max(dp[0][i], dp[0][i - 1])
        
        for i in range(1, m):
            for j in range(1, n):
                curr = dp[i][j] + max(dp[i - 1][j - 1], 0)
                dp[i][j] = max(curr, dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
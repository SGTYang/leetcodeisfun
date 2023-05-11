class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1) + 1)]
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j])
                    
        return dp[len(nums1)][len(nums2)]
        
        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if nums1[i] == nums2[j]:
                dp[(i, j)] = 1 + dfs(i+1, j+1)
            
            else:
                dp[(i, j)] = max(dfs(i, j+1), dfs(i+1, j))
            
            return dp[(i, j)]
                                 
        dp = {}
        return dfs(0,0)
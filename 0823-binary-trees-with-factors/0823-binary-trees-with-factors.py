class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = [1] * len(arr)
        
        arr.sort()
        modulo = 10**9+7
        
        index = {v:i for i,v in enumerate(arr)}
        
        for i,v in enumerate(arr):
            for j in range(i):
                if v%arr[j]==0:
                    right = v/arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= modulo
                        
        return sum(dp) % modulo
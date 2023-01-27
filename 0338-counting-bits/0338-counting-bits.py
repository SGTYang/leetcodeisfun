class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # 0   0
        # 1   1
        # 2  10
        # 3  11
        # 4 100
        # 5 101
        
        dp = [0]*(n+1)
        offset = 1
        
        for i in range(1,n+1):
            if offset*2 == i:
                offset = i
            dp[i] = dp[i-offset] + 1
            
        
        return dp
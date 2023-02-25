class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = 0
        for r in range(1,len(prices)):
            ans = max(ans, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
        
        return ans
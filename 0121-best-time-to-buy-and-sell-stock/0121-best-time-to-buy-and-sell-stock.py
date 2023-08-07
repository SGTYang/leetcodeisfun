class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l = 0
        res = 0
        for i in range(len(prices)):
            if prices[i] > prices[l]:
                res = max(res, prices[i] - prices[l])
            else:
                l = i
        
        return res
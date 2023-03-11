class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i]-lowest_price>0:
                res = max(res, prices[i]-lowest_price)
            lowest_price = min(lowest_price, prices[i])
        
        return res
            
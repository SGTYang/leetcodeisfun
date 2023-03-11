class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        max_price = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                max_price = max(max_price, prices[r]-prices[l])
            else:
                l = r
            r += 1
        
        return max_price
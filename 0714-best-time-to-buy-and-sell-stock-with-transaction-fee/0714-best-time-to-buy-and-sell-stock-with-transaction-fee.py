class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2: return 0

        profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])

            if prices[i] > min_price + fee:
                profit += prices[i] - (min_price + fee)
                min_price = prices[i] - fee

        return profit
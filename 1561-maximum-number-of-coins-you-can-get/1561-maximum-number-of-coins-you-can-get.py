class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # 2, 4, 1, 2, 7, 8
        piles.sort()
        res = 0
        for i in range(len(piles)-1, len(piles)//3, -2):
            res += piles[i - 1]
        
        return res
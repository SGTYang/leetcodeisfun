class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp solution
        
        # dfs solution
        cache = {}
        def dfs(i, a):
            if i == len(coins) or a > amount:
                return 0
            if a == amount:
                return 1
            if (i, a) in cache:
                return cache[(i, a)]
            
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]
        
        return dfs(0, 0)
        
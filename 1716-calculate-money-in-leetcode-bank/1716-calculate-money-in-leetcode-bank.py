class Solution:
    def totalMoney(self, n: int) -> int:
        base = n // 7
        rest = n % 7
        res = 0
        week_sum = 28
        
        for i in range(1, rest + 1):
            res += i + base
        
        
        while base:
            res += week_sum
            week_sum += 7
            base -= 1
        
        return res
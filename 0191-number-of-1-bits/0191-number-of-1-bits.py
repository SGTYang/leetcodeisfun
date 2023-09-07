class Solution:
    def hammingWeight(self, n: int) -> int:
        # O(num of '1')
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res
        
        # O(32)
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        
        return res
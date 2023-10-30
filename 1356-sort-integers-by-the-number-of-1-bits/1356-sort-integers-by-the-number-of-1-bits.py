class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def cnt_bits(n):
            res = 0
            while n:
                n = n & (n - 1)
                res += 1
            
            return res
        
        return sorted(arr, key = lambda x : [cnt_bits(x), x])
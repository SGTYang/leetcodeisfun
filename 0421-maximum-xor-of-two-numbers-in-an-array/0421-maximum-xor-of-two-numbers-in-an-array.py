class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(31, -1, -1):
            prefixs = set([num>>i for num in nums])
            
            ans <<= 1
            candidate = ans + 1
            
            for pre in prefixs:
                if candidate ^ pre in prefixs:
                    ans = candidate
                    break
        
        return ans
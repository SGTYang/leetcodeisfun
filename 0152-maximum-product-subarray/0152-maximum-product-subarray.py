class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxP, minP = 1, 1
        
        for n in nums:
            if n == 0:
                maxP, minP = 1, 1
                continue
            temp = maxP*n
            maxP = max(maxP*n, minP*n, n)
            minP = min(temp, minP*n, n)
            res = max(res, maxP)
        
        return res
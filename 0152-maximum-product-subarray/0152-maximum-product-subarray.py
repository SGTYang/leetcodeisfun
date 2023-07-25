class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_max = 1
        curr_min = 1
        
        for n in nums:

            tmp = curr_max * n
            curr_max = max(n, curr_max * n, curr_min * n)
            curr_min = min(n, tmp, curr_min * n)
            res = max(res, curr_max)
            
        return res
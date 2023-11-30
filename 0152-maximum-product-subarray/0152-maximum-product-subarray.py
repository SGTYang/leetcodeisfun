class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        
        curr_max = curr_min = 1
        
        for num in nums:
            tmp = curr_max
            curr_max = max(curr_min * num, curr_max * num, num)
            curr_min = min(curr_min * num, tmp * num, num)
            res = max(res, curr_max)
        
        return res
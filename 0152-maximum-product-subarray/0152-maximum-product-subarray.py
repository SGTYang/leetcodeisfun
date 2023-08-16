class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        curr_min = 1
        curr_max = 1
        
        for i in range(len(nums)):
            tmp = curr_min
            curr_min = min(nums[i], nums[i] * curr_min, nums[i] * curr_max)
            curr_max = max(nums[i], nums[i] * tmp, nums[i] * curr_max)
            res = max(res, curr_min, curr_max)
        return res
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp_max = [0]*len(nums)
        dp_max[0] = nums[0]
        for i in range(1,len(nums)):
            dp_max[i] = max(dp_max[i-1]+nums[i], nums[i])
            
        dp_min = [0]*len(nums)
        dp_min[0] = nums[0]
        for i in range(1, len(nums)):
            dp_min[i] = min(dp_min[i-1]+nums[i], nums[i])
        
        if sum(nums) == min(dp_min):
            return max(dp_max)
        return max(max(dp_max), sum(nums)-min(dp_min))
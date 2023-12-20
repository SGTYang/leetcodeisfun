class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        left = 0
        for i in range(len(nums)):
            if (total - nums[i]) / 2 == left:
                return i
            left += nums[i]
        
        return -1
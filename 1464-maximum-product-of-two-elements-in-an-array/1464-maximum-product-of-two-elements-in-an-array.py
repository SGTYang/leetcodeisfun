class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -1
        left, right = 0, len(nums) - 1
        
        while left < right:
            res = max(res, (nums[left] - 1) * (nums[right] - 1))
            if nums[left] > nums[right]:
                right -= 1
            else:
                left += 1
        
        return res
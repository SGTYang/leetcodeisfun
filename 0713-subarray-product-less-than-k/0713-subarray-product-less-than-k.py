class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left, right = 0, 0
        curr = 1
        res = 0
        while right < len(nums):
            curr *= nums[right]
            while curr >= k:
                curr = curr // nums[left]
                left += 1
            res = res + right - left + 1
            right += 1
        
        return res
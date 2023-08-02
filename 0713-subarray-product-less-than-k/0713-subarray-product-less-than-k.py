class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        curr = 1
        left = 0
        
        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr = curr // nums[left]
                left += 1
            
            res += right - left + 1
        return res
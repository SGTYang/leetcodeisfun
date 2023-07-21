class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: 
            return 0
        res = 0
        left = 0
        prev = 1
        for i in range(len(nums)):
            prev = prev*nums[i]
            while prev >= k:
                prev = prev//nums[left]
                left += 1
            
            res = res + i - left + 1
        
        return res
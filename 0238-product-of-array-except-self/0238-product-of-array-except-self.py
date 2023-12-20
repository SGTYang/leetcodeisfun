class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
        
        prefix = suffix = 1
        for i in range(len(nums)):
            if i > 0:
                prefix *= nums[i-1]
                res[i] = prefix
        
        for i in range(len(nums)-1,-1,-1):
            if i + 1 < len(nums):
                suffix *= nums[i+1]
                res[i] *= suffix
        
        return res
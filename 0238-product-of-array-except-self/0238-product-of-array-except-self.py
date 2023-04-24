class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*(len(nums)+1)
        suffix = [1]*(len(nums)+1)
        
        for i in range(len(nums)):
            prefix[i] = nums[i]*prefix[i-1]
        
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = nums[i]*suffix[i+1]
        
        return [prefix[i-1]*suffix[i+1] for i in range(len(nums))]
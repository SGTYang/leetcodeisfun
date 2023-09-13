class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, 1, 1, 2, 6
        #    24, 12,4, 1, 1,
        
        res = [1] * len(nums)
        prefix = postfix= 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
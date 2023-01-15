class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #  1, 2, 3, 4
        
        #     1, 2, 6
        # 24,12, 4
        # 24,12, 8, 6
        
        ans = [1]*len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= postfix
            postfix *= nums[i]
            
        return ans
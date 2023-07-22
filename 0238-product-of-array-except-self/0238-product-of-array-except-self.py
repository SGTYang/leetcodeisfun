class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #  1,  1,  2,  6, 24
        # 24, 24, 12,  4,  1
        n = len(nums)
        res = []
        curr = 1
        
        for i in range(n):
            res.append(curr)
            curr = nums[i] * curr
        
        print(res)
        curr = 1
        for i in range(n-1, -1, -1):
            res[i] *= curr
            curr *= nums[i]
        
        return res
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        
        first_num = nums[0]
        for i in range(1,len(nums)):
            first_num *= nums[i]
        
        if first_num == 0:
            return 0
        elif first_num > 0:
            return 1
        else:
            return -1
            
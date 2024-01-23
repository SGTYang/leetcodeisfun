class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        
        for n in nums:
            num = abs(n)
            nums[num - 1] = -nums[num - 1]
            if nums[num - 1] > 0:
                res[0] = num
        
        for i, n in enumerate(nums):
            if n > 0 and i + 1 != res[0]:
                res[1] = i + 1
        
        return res
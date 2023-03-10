class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        
        curMax = curMin = 1
        for num in nums:
            tmp = curMax*num
            curMax = max(tmp, curMin*num, num)
            curMin = min(tmp, curMin*num, num)
            
            res = max(res, curMax)
        return res
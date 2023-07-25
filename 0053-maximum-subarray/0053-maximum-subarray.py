class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr = float('-inf'), float('-inf')
        
        for n in nums:
            curr = max(n + curr, n)
            res = max(res, curr)
        
        return res
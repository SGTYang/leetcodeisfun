class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        total_sum = float('-inf')
        
        for n in nums:
            if total_sum + n < n:
                total_sum = n
            else:
                total_sum += n
            res = max(res, total_sum)
        
        return res
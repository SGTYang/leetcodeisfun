class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = float('-inf')
        total_sum = float('-inf')
        for num in nums:
            if total_sum+num < num:
                total_sum = num
            else:
                total_sum += num
            
            max_sum = max(max_sum, total_sum)
        return max_sum
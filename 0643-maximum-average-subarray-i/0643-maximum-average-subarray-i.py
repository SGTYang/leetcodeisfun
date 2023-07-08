class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        k_sum = sum(nums[:k])
        max_sum = k_sum
        
        for i in range(k,len(nums)):
            k_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, k_sum)
        
        return max_sum / k
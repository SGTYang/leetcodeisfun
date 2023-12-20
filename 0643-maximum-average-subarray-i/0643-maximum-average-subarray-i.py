class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]
        res = curr/k
        
        for i in range(k, len(nums)):
            curr -= nums[i - k]
            curr += nums[i]
            res = max(res, curr/k)
        
        return res
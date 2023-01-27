class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for i in range(len(nums)):
            ans += i-nums[i]
        return ans
            
        
        return sum([i for i in range(len(nums)+1)]) - sum(nums)
    
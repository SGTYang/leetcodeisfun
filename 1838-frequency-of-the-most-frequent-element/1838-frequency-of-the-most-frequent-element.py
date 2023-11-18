class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = ii = sm = 0 
        for i in range(len(nums)): 
            sm += nums[i]
            while k < nums[i]*(i-ii+1) - sm: 
                sm -= nums[ii]
                ii += 1
            ans = max(ans, i - ii + 1)
        return ans
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        left, right = 0, 0
        res = 0
        cnt = 0
        
        for i in range(len(nums)):
            if nums[i] != 1:
                cnt += 1
                while cnt > 1:
                    if nums[left] == 0:
                        cnt -= 1
                    left += 1
            
            res = max(res, i - left + 1 - cnt)
        
        return res - 1 if res == len(nums) else res
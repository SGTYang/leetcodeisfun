class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res = curr_min = nums[k]
        l = r = k
        
        while l - 1 >= 0 or r + 1 < len(nums):
            if l == 0 or (r + 1 < len(nums) and nums[l - 1] < nums[r + 1]):
                r += 1
                curr_min = min(curr_min, nums[r])
            else:
                l -= 1
                curr_min = min(curr_min, nums[l])
            
            res = max(res, curr_min * (r - l + 1))
        
        return res
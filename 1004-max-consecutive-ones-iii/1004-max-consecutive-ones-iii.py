class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        res = 0
        
        while left < len(nums) and right < len(nums):
            if k != 0 or nums[right] == 1:
                if nums[right] == 0:
                    k -= 1
                right += 1
            elif k == 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            res = max(res, right - left)
        
        return res
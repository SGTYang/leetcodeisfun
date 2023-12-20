class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 0
        left, right = 0, 0
        res = 0
        
        while right < len(nums):
            if nums[right] == 1:
                right += 1
                
            elif nums[right] == 0:
                if not k:
                    k += 1
                    right += 1
                else:
                    while k:
                        if nums[left] == 0:
                            k -= 1
                        left += 1
            
            res = max(res, right - left - k)
        
        return res if res != len(nums) else len(nums) - 1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        left, right = 0, 0
        
        while right < len(nums):
            if nums[right] == 1:
                right += 1
                
            elif nums[right] == 0:
                while not k:
                    if nums[left] == 0:
                        k += 1
                    left += 1
                right += 1
                k -= 1
            
            
            res = max(res, right - left)
        
        return res
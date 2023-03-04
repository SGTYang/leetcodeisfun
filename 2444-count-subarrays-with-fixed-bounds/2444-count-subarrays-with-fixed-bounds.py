class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_position = max_position = left_bound = -1
        
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                left_bound = i
            
            if nums[i] == minK:
                min_position = i
            if nums[i] == maxK:
                max_position = i
                
            res += max(0, min(min_position, max_position) - left_bound)
        
        return res
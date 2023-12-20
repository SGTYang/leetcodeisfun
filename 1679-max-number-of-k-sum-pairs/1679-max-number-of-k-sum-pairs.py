class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        res = 0
        
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                left += 1
                right -= 1
                res += 1
                
            elif total > k:
                right -= 1
            else:
                left += 1
        
        return res
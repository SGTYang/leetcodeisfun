class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True

        last_idx = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if last_idx <= nums[i] + i:
                last_idx = i
        
        return last_idx == 0
            
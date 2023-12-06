class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy
        jumps = [float('inf')] * len(nums)
        jumps[0] = 0
        
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                jumps[min(i + j, len(nums) - 1)] = min(jumps[min(i + j, len(nums) - 1)], jumps[i] + 1)
        
        return jumps[-1]
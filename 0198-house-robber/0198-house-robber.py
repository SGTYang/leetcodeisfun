class Solution:
    def rob(self, nums: List[int]) -> int:
        # [rob1, rob2, n, n+1, ...]
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = rob2
            rob2 = max(rob1 + n, rob2)
            rob1 = tmp
        
        return max(rob1, rob2)
class Solution:
    def rob(self, nums: List[int]) -> int:
        # [rob1, rob2, n, n+1, ...]
        one, two = 0, 0
        
        for i in range(len(nums)):
            tmp = two
            two = max(one + nums[i], two)
            one = tmp
        
        return max(one, two)
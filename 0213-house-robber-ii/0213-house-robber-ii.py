class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for i in range(len(nums) - 1):
            tmp = two
            two = max(two, one + nums[i])
            one = tmp
        
        first_cycle = max(one, two)
        
        one, two = 0, 0
        for i in range(1, len(nums)):
            tmp = two
            two = max(two, one + nums[i])
            one = tmp
        
        second_cycle = max(one, two)
        
        return max(nums[0], first_cycle, second_cycle)
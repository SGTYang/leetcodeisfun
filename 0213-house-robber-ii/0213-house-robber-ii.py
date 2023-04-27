class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(num_list):
            rob1, rob2 = 0, 0

            for n in num_list:
                temp = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = temp

            return max(rob2, rob1)
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
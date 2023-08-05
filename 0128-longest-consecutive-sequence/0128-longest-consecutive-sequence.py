class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        for num in nums:
            curr_len = 0
            if num - 1 not in num_set:
                while num + curr_len in num_set:
                    curr_len += 1
            res = max(res, curr_len)
        
        return res
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        
        num_set = set(nums)
        
        for num in nums:
            curr_len = 1
            if num-1 not in num_set:
                while num in num_set:
                    res = max(res, curr_len)
                    curr_len += 1
                    num += 1
        
        return res
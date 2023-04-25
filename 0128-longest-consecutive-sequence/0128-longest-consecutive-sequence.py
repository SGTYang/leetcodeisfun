class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for n in nums:
            if n-1 not in num_set:
                long = 0
                while (long+n) in num_set:
                    long += 1
                res = max(res, long)
        
        return res
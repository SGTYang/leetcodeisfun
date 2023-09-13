class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set()
        for num in nums:
            num_set.add(num)
        
        for i in range(len(nums)):
            curr = nums[i]
            cnt = 0
            if curr - 1 not in num_set:
                while curr in num_set:
                    cnt += 1
                    curr += 1
            res = max(res, cnt)
        
        return res
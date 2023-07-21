class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                if k == 0:
                    while nums[left] != 0:
                        left += 1
                    left += 1
                else:
                    k -= 1
            res = max(res, i - left + 1)
        return res
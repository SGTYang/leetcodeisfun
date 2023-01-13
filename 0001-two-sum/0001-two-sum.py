class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        search = {}

        for idx in range(len(nums)):
            find = target-nums[idx]

            if find in search:
                return [idx, search[find]]
            search[nums[idx]] = idx
        
        return -1
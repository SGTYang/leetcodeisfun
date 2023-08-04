class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] in num_dict:
                return [i, num_dict[nums[i]]]
            ct = target - nums[i]
            num_dict[ct] = i
        
        
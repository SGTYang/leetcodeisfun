class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        
        for i in range(len(nums)):
            f = target - nums[i]
            
            if f in nums_dict:
                return[i, nums_dict[f]]
            nums_dict[nums[i]] = i
        
        return None
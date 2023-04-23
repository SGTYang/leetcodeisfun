class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        
        for i in range(len(nums)):
            fid = target-nums[i]
            if fid in num_dict:
                return[i, num_dict[fid]]
            else:
                num_dict[nums[i]] = i
        
        return None
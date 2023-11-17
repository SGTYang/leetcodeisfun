class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        for i in range(len(nums)//2):
            res.append(nums[i] + nums[-(i+1)])
        
        return max(res)
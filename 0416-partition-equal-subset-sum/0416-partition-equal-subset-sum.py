class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        
        target = sum(nums)//2
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            nextDP = set()
            for j in dp:
                if nums[i]+j == target:
                    return True
                nextDP.add(nums[i]+j)
                nextDP.add(j)
            dp = nextDP
        
        return True if target in dp else False
        
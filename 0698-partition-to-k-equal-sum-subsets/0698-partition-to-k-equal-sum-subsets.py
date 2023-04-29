class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k:
            return False
        nums.sort(reverse=True)
        target = sum(nums)//k
        used = [False]*len(nums)
        
        def backtrack(i, k, curr_sum):
            if k == 0:
                return True
            if curr_sum == target:
                return backtrack(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if j > 0 and not used[j - 1] and nums[j] == nums[j - 1]:
                    continue
                if used[j] or nums[j] + curr_sum > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, nums[j] + curr_sum):
                    return True
                used[j] = False
            return False
        
        return backtrack(0,k,0)
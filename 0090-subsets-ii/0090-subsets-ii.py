class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        curr = []
        
        def backtracking(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            backtracking(i+1)
            curr.pop()
            
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtracking(i+1)
            
        backtracking(0)
        return res
            
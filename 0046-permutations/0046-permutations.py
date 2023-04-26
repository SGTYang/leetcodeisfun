class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(subset, visited):
            if len(subset) == len(nums):
                res.append(subset)
                return
            
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backtracking(subset+[nums[i]], visited)
                    visited.remove(i)
        
        backtracking([], set())
        
        return res
    
#         res = []
#         if len(nums) == 1:
#             return [nums[:]]
        
#         for i in range(len(nums)):
#             num = nums.pop(0)
            
#             perms = self.permute(nums)
            
#             for p in perms:
#                 p.append(num)
#             res.extend(perms)
#             nums.append(num)
        
#         return res
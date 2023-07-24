class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(bucket, visited):
            if len(bucket) == len(nums):
                res.append(bucket.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    dfs(bucket + [nums[i]], visited)
                    visited.remove(nums[i])
                    
        dfs([], set())
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
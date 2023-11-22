class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time: O(2^n)
        # Space: O(n)
        
        res = []
        curr = []
        def dfs(idx):
            if idx == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[idx])
            dfs(idx + 1)
            curr.pop()
            dfs(idx + 1)
        
        dfs(0)
        return res
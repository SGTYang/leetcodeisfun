class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def dfs(i, total, curr):
            if total > target or i >= n:
                return
            if total == target:
                res.append(curr.copy())
                return
            for i in range(i, n): 
                dfs(i, total + candidates[i], curr + [candidates[i]])
        
        dfs(0, 0, [])
        return res
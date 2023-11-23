class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def dfs(idx, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or idx >= len(candidates):
                return
            
            curr.append(candidates[idx])
            dfs(idx + 1, curr, total + candidates[idx])
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            curr.pop()
            dfs(idx + 1, curr, total)
        
        dfs(0, [], 0)
        return res
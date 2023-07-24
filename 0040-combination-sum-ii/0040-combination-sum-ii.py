class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        visited = set()
        
        def dfs(i, curr, total):
            if total > target:
                return
            if total == target:
                res.append(curr.copy())
            
            prev = -1
            for i in range(i, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                dfs(i+1, curr, total+candidates[i])
                curr.pop()
                
                prev = candidates[i]
            
        dfs(0, [], 0)
        
        return res
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time: O(2^target)
        # Space: O(target)
        
        res = []
        curr = []
        def dfs(idx, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return
            
            for i in range(idx, len(candidates)):
                curr.append(candidates[i])
                dfs(i, total + candidates[i])
                curr.pop()
        
        for i in range(len(candidates)):
            curr.append(candidates[i])
            dfs(i, candidates[i])
            curr.pop()
        return res
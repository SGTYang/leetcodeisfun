class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()
        
        def backtrack(idx, total):
            if total > target:
                return
            
            if total == target:
                res.append(curr.copy())
                return
            
            prev = -1
            for i in range(idx, len(candidates)):
                if prev == candidates[i]:
                    continue
                curr.append(candidates[i])
                
                backtrack(i+1, total+candidates[i])
                curr.pop()
                
                prev = candidates[i]
        
        backtrack(0,0)
        return res
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        
        def backtrack(i):
            res = 0
            
            if i < len(s):
                for i_idx in range(i+1, len(s)+1):
                    if s[i:i_idx] not in seen:
                        seen.add(s[i:i_idx])
                        res = max(res, 1 + backtrack(i_idx))
                        seen.remove(s[i:i_idx])
            
            return res
        
        return backtrack(0)
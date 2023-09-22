class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for c in t:
            if idx < len(s) and s[idx] == c:
                idx += 1
        
        return len(s) == idx
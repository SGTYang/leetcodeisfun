class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        open_paren = 0
        
        for c in s:
            if c == "(":
                open_paren += 1
            elif c == ")":
                if open_paren:
                    open_paren -= 1
                else:
                    res += 1
        
        res += open_paren
        return res
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        open_p = 0
        for i in range(len(s)):
            if s[i] == "(":
                open_p += 1
            elif s[i] == ")":
                if not open_p:
                    s[i] = ""
                else:
                    open_p -= 1
        
        for i in range(len(s)-1, -1, -1):
            if not open_p:
                break
            if s[i] == "(":
                s[i] = ""
                open_p -= 1
        
        return "".join(s)
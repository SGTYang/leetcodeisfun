class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"(":")", "{":"}", "[":"]"}
        
        for i in range(len(s)):
            if s[i] in pair:
                stack.append(s[i])
            elif stack and pair[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False
        
        return True if not stack else False
class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }
        stack = []
        for c in s:
            if c in valid:
                stack.append(c)
            else:
                if not stack or valid[stack[-1]] != c:
                    return False
                stack.pop()
        
        return True if not stack else False
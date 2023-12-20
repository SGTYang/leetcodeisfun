class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        left, right = 0, 0
        
        while right < len(s):
            while right < len(s) and s[right] == " ":
                left = right + 1
                right += 1
            
            while right < len(s) and s[right] != " ":
                right += 1
            
            if s[left:right]:
                stack.append(s[left:right])
        
        stack = stack[::-1]
        return " ".join(stack)
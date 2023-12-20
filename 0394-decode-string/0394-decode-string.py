class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        curr_num = 0
        
        for c in s:
            if c == "[":
                stack.append(curr)
                stack.append(curr_num)
                curr = ""
                curr_num = 0
            elif c == "]":
                num = stack.pop()
                prev = stack.pop()
                curr = prev + num * curr
            elif c.isdigit():
                curr_num = curr_num * 10 + int(c)
            else:
                curr += c
        
        return curr
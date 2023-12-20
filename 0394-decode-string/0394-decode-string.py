class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        num = 0
        for c in s:
            if c == "[":
                stack.append(curr)
                stack.append(num)
                curr = ""
                num = 0
            
            elif c == "]":
                curr_num = stack.pop()
                prev = stack.pop()
                curr = prev + curr * curr_num
            
            elif c.isdigit():
                num = num * 10 + int(c)
            
            else:
                curr += c
        
        return curr
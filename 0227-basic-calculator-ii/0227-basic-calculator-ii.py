class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        s += "+"
        sign = "+"
        stack = []
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in "+*-/":
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(math.trunc(stack.pop() / num))

                sign = s[i]
                num = 0
        return sum(stack)
class Solution:
    def calculate(self, s: str) -> int:
        " 10 + 3 * 4"
        # store the number in an array, when the c is not an number append in the stack
        # only if c is equal to */ pop the last element from the array and calculate
        # return sum(array)
        # num = num * 10 + int(c)
        num = 0
        stack = []
        sign = "+"
        
        for c in s+"-":
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+*-/":
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(math.trunc(stack.pop() / num))
                num = 0
                sign = c
        
        return sum(stack)
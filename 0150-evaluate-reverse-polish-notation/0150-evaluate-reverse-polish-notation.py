class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
        
        return stack[0]
                    
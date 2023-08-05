class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        
        operator = {"+", "-", "*", "/"}
        for i in range(len(tokens)):
            if tokens[i] not in operator:
                num_stack.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    num_stack.append(num_stack.pop() + num_stack.pop())
                elif tokens[i] == "-":
                    a, b = num_stack.pop(), num_stack.pop()
                    num_stack.append(b -a)
                elif tokens[i] == "*":
                    num_stack.append(num_stack.pop() * num_stack.pop())
                else:
                    a, b = num_stack.pop(), num_stack.pop()
                    num_stack.append(int(b/a))
        
        return num_stack[-1]
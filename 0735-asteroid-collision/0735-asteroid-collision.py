class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(asteroids)):
            a = asteroids[i]
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] < abs(a):
                    stack.pop()

                elif stack[-1] > abs(a):
                    a = 0
                    break

                elif stack[-1] == abs(a):
                    stack.pop()
                    a = 0
                    break
            if a :
                stack.append(a)
                    
        return stack
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        step_one = 1
        step_two = 2
        for i in range(2,n):
            if i%2 == 0:
                step_one = step_one + step_two
            else:
                step_two = step_one + step_two
        
        return max(step_one, step_two)
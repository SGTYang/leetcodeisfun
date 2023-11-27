class Solution:
    def climbStairs(self, n: int) -> int:
        one_step = 1
        two_step = 1
        
        for i in range(n - 1):
            tmp = two_step
            two_step = one_step + two_step
            one_step = tmp
        
        return two_step
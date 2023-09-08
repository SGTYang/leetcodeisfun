class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n not in visited:
            visited.add(n)
            if n == 1:
                return True
            curr_sum = 0
            while n:
                curr_sum = curr_sum + (n%10) ** 2
                n = n//10
            n = curr_sum
        return False
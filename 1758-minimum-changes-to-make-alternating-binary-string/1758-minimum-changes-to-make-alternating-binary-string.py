class Solution:
    def minOperations(self, s: str) -> int:
        odd = even = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != "0":
                    even += 1
                elif s[i] != "1":
                    odd += 1
            
            else:
                if s[i] != "1":
                    even += 1
                elif s[i] != "0":
                    odd += 1
         
        return min(odd, even)
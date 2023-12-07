class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
        
        res = ""
        curr = ""
        for c in num:
            curr += c
            if int(c) % 2 != 0:
                res = curr
        
        return res
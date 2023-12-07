class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = ""
        curr = ""
        for c in num:
            curr += c
            if int(c) % 2 != 0:
                res = curr
        
        return res
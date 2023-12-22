class Solution:
    def maxScore(self, s: str) -> int:
        # left : # of zeros
        # right : # of ones
        total_ones = 0
        total_zeros = 0 if s[0] == "1" else 1
        
        for i in range(1, len(s)):
            if s[i] == '1':
                total_ones += 1

        res = total_zeros + total_ones
        
        for i in range(1, len(s) - 1):
            if s[i] == '1':
                total_ones -= 1
            elif s[i] == '0':
                total_zeros += 1
            res = max(res, total_ones + total_zeros)
        
        return res
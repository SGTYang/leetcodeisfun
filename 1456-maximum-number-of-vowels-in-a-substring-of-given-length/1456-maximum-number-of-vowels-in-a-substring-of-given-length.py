class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = {"a", "e", "i", "o", "u"}
        cnt = 0
        for i in range(k):
            if s[i] in vow:
                cnt += 1
                
        res = cnt
        
        for i in range(k, len(s)):
            if s[i-k] in vow:
                cnt -= 1
            if s[i] in vow:
                cnt += 1
            res = max(res, cnt)
        
        return res
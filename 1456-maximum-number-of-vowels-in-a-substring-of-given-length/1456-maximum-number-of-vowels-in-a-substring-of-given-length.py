class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        curr_vow = 0
        res = 0
        
        for i in range(len(s)):
            if i >= k and s[i-k] in vowels:
                curr_vow -= 1
            
            if s[i] in vowels:
                curr_vow += 1
            
            res = max(res, curr_vow)
        
        return res
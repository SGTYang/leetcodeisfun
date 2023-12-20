class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        res = ""
        vowels=[]
        for i in range(len(s)):
            if s[i] in vow:
                vowels.append(s[i])
        
        for i in range(len(s)):
            if s[i] in vow:
                res += vowels.pop()
            else:
                res += s[i]
        
        return res
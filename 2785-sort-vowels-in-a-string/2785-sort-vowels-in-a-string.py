class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        vow_list = [c for c in s if c in vowels]
        vow_list.sort(reverse=True)
        
        res = ""
        
        for c in s:
            if c in vowels:
                res += vow_list.pop()
            else:
                res += c
        
        return res
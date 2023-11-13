class Solution:
    def sortVowels(self, s: str) -> str:
        # Time O(n)
        # Space O(1)
        vowel = "AEIOUaeiou"
        vowel_cnt = [0]*len(vowel)
        vowels = {"A":0, "E":1, "I":2, "O":3, "U":4, "a":5, "e":6, "i":7, "o":8, "u":9}
        
        for c in s:
            if c in vowels:
                vowel_cnt[vowels[c]] += 1
        
        res = ""
        idx = 0
        for c in s:
            if c in vowels:
                while vowel_cnt[idx] == 0:
                    idx += 1
                vowel_cnt[idx] -= 1
                res += vowel[idx]
            else:
                res += c
        
        return res
        
        # Time O(nlogn)
        # Space O(1)
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
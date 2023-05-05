class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        max_vowels = curr_vowels = 0
        for i, c in enumerate(s):
            if i >= k and s[i-k] in vowels:
                curr_vowels -= 1
            if c in vowels:
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels

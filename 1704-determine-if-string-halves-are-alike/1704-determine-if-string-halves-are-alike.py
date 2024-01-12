class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        half = len(s)//2
        left = right = 0
        
        for i in range(half):
            if s[i] in vowels:
                left += 1
            if s[i+half] in vowels:
                right += 1
        return left == right
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        word_dict = defaultdict(int)
        for c in s:
            word_dict[c] += 1
        
        for c in t:
            if c not in word_dict or word_dict[c] == 0:
                return c
            word_dict[c] -= 1
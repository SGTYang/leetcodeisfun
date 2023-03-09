class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word_cnt = defaultdict(int)
        for w in s:
            word_cnt[w] += 1
        
        for w in t:
            if w not in word_cnt or word_cnt[w] == 0:
                return False
            word_cnt[w] -= 1
        
        return True
        
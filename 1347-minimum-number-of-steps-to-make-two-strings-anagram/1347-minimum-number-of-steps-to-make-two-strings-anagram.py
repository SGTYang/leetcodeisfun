class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt = [0] * 26
        res = 0
        for c in s:
            s_cnt[ord(c) - ord("a")] += 1
        
        for c in t:
            if s_cnt[ord(c) - ord("a")] > 0:
                s_cnt[ord(c) - ord("a")] -= 1
        
        return sum(s_cnt)
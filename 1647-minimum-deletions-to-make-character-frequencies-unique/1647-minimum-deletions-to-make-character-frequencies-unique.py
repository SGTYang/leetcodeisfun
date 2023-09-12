class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = defaultdict(int)
        cnt_set = set()
        res = 0
        
        for c in s:
            cnt[c] += 1
        
        for k,v in cnt.items():
            while v and v in cnt_set:
                v -= 1
                res += 1
            cnt_set.add(v)
        
        return res
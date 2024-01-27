class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # order = "ebd" s = "abcde" -> aecbd, eacbd, ...
        # is characters order unique?
        
        res = ""
        
        word_cnt = defaultdict(int)
        for c in s:
            word_cnt[c] += 1
        
        for c in order:
            if c in word_cnt:
                res += c * word_cnt[c]
                del word_cnt[c]
        
        for k, v in word_cnt.items():
            res += k * v
        
        return res
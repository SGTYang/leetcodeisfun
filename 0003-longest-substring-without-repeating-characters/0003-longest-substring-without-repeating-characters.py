class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        res = 0
        l,r = 0, 1
        sub_set = set(s[l])
        
        while r < len(s):
            while s[r] in sub_set:
                sub_set.remove(s[l])
                l += 1
            sub_set.add(s[r])
            res = max(res, len(sub_set))
            r += 1
        return res
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        t_count = defaultdict(int)
        s_count = defaultdict(int)
        
        for c in t:
            t_count[c] += 1
        
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            s_count[c] += 1
            
            if c in t_count and s_count[c] == t_count[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
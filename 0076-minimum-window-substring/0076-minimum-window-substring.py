class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        
        for i in range(len(t)):
            t_count[t[i]] += 1
            
        have, need = 0, len(t_count)
        l = 0
        min_len = float('inf')
        res = [0, 0]
        
        for r in range(len(s)):
            s_count[s[r]] += 1
            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = [l, r]
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1] + 1] if min_len != float('inf') else ""
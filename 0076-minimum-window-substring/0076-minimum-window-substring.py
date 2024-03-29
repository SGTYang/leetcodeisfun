class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        for c in t:
            t_dict[c] += 1
            
        need = len(t_dict)
        have = 0
        l = 0
        res = [-1, -1]
        res_len = float('inf')
        
        for r in range(len(s)):
            window_dict[s[r]] += 1
            if s[r] in t_dict and window_dict[s[r]] == t_dict[s[r]]:
                have += 1
            
            while have == need:
                if res_len > r - l + 1:
                    res_len = r - l + 1
                    res = [l, r]
                
                window_dict[s[l]] -= 1
                
                if s[l] in t_dict and window_dict[s[l]] < t_dict[s[l]]:
                    have -= 1
                    
                l += 1
        
        return s[res[0]:res[1] + 1] if res_len != float('inf') else ""
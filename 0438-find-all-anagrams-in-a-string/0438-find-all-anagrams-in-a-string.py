class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        
        p_cnt = defaultdict(int)
        s_cnt = defaultdict(int)
        for i in range(len(p)):
            p_cnt[p[i]] += 1
            s_cnt[s[i]] += 1
            
        res = [0] if s_cnt == p_cnt else []
        
        left = 0
        for right in range(len(p), len(s)):
            s_cnt[s[right]] += 1
            s_cnt[s[left]] -= 1
            
            if s_cnt[s[left]] == 0:
                del s_cnt[s[left]]
                
            left += 1
            
            if s_cnt == p_cnt:
                res.append(left)
                
        
        return res
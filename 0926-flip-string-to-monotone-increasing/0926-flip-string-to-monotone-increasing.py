class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        z_cnt = [0]*len(s)
        o_cnt = [0]*len(s)
        
        for i in range(1,len(s)):
            if s[i-1] == "1":
                o_cnt[i] = 1+o_cnt[i-1]
            else:
                o_cnt[i] = o_cnt[i-1]
        
        for i in range(len(s)-2,-1,-1):
            if s[i+1] == "0":
                z_cnt[i] = z_cnt[i+1]+1
            else:
                z_cnt[i] = z_cnt[i+1]
                
        ans = len(s)
        
        for i in range(len(s)):
            ans = min(ans, z_cnt[i]+o_cnt[i])
        
        return ans
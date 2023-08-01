class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_cnt = defaultdict(int)
        s2_cnt = defaultdict(int)
        
        for i in range(len(s1)):
            s1_cnt[s1[i]] += 1
            s2_cnt[s2[i]] += 1
        
        left = 0
        
        for right in range(len(s1), len(s2)):
            if s1_cnt == s2_cnt:
                return True
            s2_cnt[s2[right]] += 1
            s2_cnt[s2[left]] -= 1
            if s2_cnt[s2[left]] == 0:
                s2_cnt.pop(s2[left])
            left += 1
        
        return True if s1_cnt == s2_cnt else False
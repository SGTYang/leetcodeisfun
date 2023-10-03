class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = defaultdict(int)
        window_dict = defaultdict(int)
        
        for c in s1:
            s1_count[c] += 1
        
        l = 0
        for r in range(len(s2)):
            if s2[r] in s1_count:
                window_dict[s2[r]] += 1
            
            if r - l + 1 == len(s1): 
                if s1_count == window_dict:
                    return True
                
                if s2[l] in window_dict:
                    window_dict[s2[l]] -= 1
                    
                l += 1
        
        return False
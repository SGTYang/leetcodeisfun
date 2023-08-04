class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        compare = defaultdict(int)
        for c in s:
            compare[c] += 1
        
        for c in t:
            if compare[c] == 0 or c not in compare:
                return False
            compare[c] -= 1
        
        return True
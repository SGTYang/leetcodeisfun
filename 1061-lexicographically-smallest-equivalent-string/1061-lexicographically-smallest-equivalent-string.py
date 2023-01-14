class Unionfind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, idx):
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]
    
    def union(self, s1, s2):
        s1_idx = ord(s1) - ord("a")
        s2_idx = ord(s2) - ord("a")
        
        if s1_idx == s2_idx:
            return
        
        s1_idx = self.find(s1_idx)
        s2_idx = self.find(s2_idx)
        
        self.parent[s1_idx] = self.parent[s2_idx] = min(s1_idx, s2_idx)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        uni = Unionfind(26)
        
        ans = ""
        
        for i in range(len(s1)):
            uni.union(s1[i], s2[i])
        
        for s in baseStr:
            idx = ord(s) - ord("a")
            ans += chr(uni.find(idx)+ord("a"))
        
        return ans
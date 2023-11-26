class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Time: 
        # Space:
        res = []
        
        def dfs(i, part):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.is_pali(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j+1, part)
                    part.pop()
        
        dfs(0, [])
        
        return res
        
    def is_pali(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
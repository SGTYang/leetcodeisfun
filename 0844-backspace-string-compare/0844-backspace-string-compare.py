class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s), len(t)
        
        while i >= 0 and j >= 0:
            delete = 1
            while delete > 0: 
                i -= 1
                if i >= 0 and s[i] == '#':
                    delete += 1 
                else:
                    delete -= 1
            
            delete = 1
            while delete > 0:
                j -= 1
                if j >= 0 and t[j] == '#':
                    delete += 1
                else:
                    delete -= 1
                
            if i >= 0 and j >= 0 and s[i] != t[j]: return False
        
        return i < 0 and j < 0
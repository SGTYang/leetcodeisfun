class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        l1, l2 = len(str1), len(str2)
        
        def dividable(l):
            if l1 % l != 0 or l2 % l != 0:
                return False
            
            return str1[:l]*(l1//l) == str1 and str1[:l]*(l2//l) == str2
        
        
        res = ""
        
        for i in range(1,min(l1,l2)+1):
            if dividable(i):
                res = str1[:i]
        
        return res
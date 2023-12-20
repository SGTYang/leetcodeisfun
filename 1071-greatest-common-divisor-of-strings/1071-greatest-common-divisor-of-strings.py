class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = min(len(str1), len(str2))
        res = ""
        for i in range(1, n + 1):
            s1 = str1[:i]
            s2 = str2[:i]
            
            if s1 == s2 and s1 * (len(str1)//i) == str1 and s2 * (len(str2)//i) == str2:
                res = s1
        
        return res
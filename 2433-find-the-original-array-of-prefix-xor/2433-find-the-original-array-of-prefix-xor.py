class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) == 1:
            return pref
        
        res = [pref[0]]
        for i in range(len(pref) - 1):
            res.append(pref[i] ^ pref[i+1])
            
        return res

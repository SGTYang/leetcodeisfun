class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        res = 0
        
        for i in range(len(gain)):
            curr += gain[i]
            res = max(res, curr)
        
        return res
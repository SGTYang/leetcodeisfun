class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        curr_alt = 0
        for alt in gain:
            curr_alt += alt
            res = max(res, curr_alt)
        
        return res
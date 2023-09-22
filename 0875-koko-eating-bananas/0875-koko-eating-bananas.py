class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = sum(piles)
        
        while left <= right:
            mid = (left + right) // 2
            hour = 0
            for banana in piles:
                hour += math.ceil(banana / mid)
            
            if hour <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res
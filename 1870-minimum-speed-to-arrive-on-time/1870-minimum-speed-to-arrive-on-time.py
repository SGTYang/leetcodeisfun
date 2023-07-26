class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        
        lo, hi = 1, 10 ** 7 + 1
        
        while lo < hi:
            mid = (lo + hi) // 2
			
            time_taken = sum(
                math.ceil(d / mid) 
                for d in dist[:-1]
            ) + dist[-1] / mid
			
            if time_taken > hour:
                lo = mid + 1
            else:
                hi = mid
                
        return lo
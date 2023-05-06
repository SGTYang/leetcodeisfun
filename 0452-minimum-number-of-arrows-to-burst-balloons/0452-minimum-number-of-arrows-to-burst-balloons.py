class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # [1,6], [2,8], [6,12], [10,16]
        points.sort(key = lambda x : x[0])
        res = 1
        prev_start, prev_end = points[0]
        
        for start, end in points:
            if prev_end < start:
                res += 1
                prev_end = end
                prev_start = start
            else:
                prev_end = min(end, prev_end)
                prev_start = max(prev_start, start)
        return res
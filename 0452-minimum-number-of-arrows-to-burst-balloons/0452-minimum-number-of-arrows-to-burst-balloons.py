class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # [1,6], [2,8], [6,12], [10,16]
        points.sort()
        prev_start, prev_end = points[0]
        res = 1
        
        for i in range(1, len(points)):
            start, end = points[i]
            if prev_end < start:
                res += 1
                prev_end = end
            else:
                prev_end = min(end, prev_end)
        
        return res
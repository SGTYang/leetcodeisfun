class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        res = 0
        if not points:
            return res
        points.sort(key = lambda x : x[0])

        prev = points[0][0]
        for i in range(1, len(points)):
            x, y = points[i]
            res = max(res, x - prev)
            prev = x

        return res
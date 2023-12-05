class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        if not intervals:
            return res
        intervals.sort()
        prev_start, prev_end = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if prev_end > start:
                res += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        return res
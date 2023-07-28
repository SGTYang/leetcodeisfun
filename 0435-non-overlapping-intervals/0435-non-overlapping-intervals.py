class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        _, prev_end = intervals[0]
        res = 0
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                res += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        
        return res
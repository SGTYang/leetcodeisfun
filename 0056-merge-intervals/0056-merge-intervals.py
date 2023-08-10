class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = []
        prev_start, prev_end = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if prev_end < start:
                res.append([prev_start, prev_end])
                prev_start, prev_end = start, end
            else:
                prev_start = min(prev_start, start)
                prev_end = max(prev_end, end)
        
        res.append([prev_start, prev_end])
        return res
            
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        prev_start, prev_end = intervals[0][0], intervals[0][1]
        res = []
        for start, end in intervals:
            if start > prev_end:
                res.append([prev_start, prev_end])
                prev_end = end
                prev_start = start
            elif end > prev_end:
                prev_end = end
        res.append([prev_start, prev_end])
        return res
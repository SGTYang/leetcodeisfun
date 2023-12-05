class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x : x[0])
        res = []
        
        prev_start, prev_end = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            if prev_end >= start:
                prev_start = min(prev_start, start)
                prev_end = max(prev_end, end)
            else:
                res.append([prev_start, prev_end])
                prev_start = start
                prev_end = end
        
        res.append([prev_start, prev_end])
        return res
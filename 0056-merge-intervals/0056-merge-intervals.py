class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev_start, prev_end = intervals[0]
        res = []
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            if start > prev_end:
                res.append([prev_start, prev_end])
                prev_start, prev_end = start, end
            
            prev_start = min(prev_start, start)
            prev_end = max(prev_end, end)
        
        res.append([prev_start, prev_end])
        
        return res
                
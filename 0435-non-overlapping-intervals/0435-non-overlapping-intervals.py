class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        res = 0
        prev_start, prev_end = intervals[0]
        
        for start, end in intervals[1:]:
            if prev_end > start:
                res +=1
                prev_end = min(prev_end, end)
            else:
                prev_start, prev_end = start, end
        
        return res
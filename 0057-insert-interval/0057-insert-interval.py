class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if start > newInterval[1]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            elif end < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
        res.append(newInterval)
        return res
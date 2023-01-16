class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        
        for i in range(len(intervals)):
            start, end = intervals[i]
            
            if newInterval[1] < start:
                ans.append(newInterval)
                return ans + intervals[i:]
            
            elif end < newInterval[0]:
                ans.append(intervals[i])
                
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
                
        ans.append(newInterval)
        
        return ans
                
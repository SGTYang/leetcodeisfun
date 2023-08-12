class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = {}
        min_heap = []

        idx = 0
        for q in sorted(queries):
            while idx < len(intervals) and intervals[idx][0] <= q:
                heapq.heappush(min_heap, [intervals[idx][1] - intervals[idx][0] + 1, intervals[idx][1]])
                idx += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            res[q] = min_heap[0][0] if min_heap else - 1
        
        return [res[q] for q in queries]
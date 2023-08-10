class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [[x**2 + y**2, [x,y]] for x, y in points]
        heapq.heapify(min_heap)
        res = []
        while k:
            _, cord = heapq.heappop(min_heap)
            res.append(cord)
            k -= 1
        return res
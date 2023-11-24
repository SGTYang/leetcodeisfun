class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            heapq.heappush(heap, (x**2 + y**2, [x,y]))
        
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
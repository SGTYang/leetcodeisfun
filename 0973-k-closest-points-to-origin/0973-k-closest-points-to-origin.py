class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate all the point's distances to the origin
        res = []
        dist = []
        # O(P)
        for x, y in points:
            dist.append([y*y + x*x, [x, y]])
        
        # O(P)
        heapq.heapify(dist)
        
        # O(klogP)
        while k:
            d, c = heapq.heappop(dist)
            res.append(c)
            k -= 1
        
        return res
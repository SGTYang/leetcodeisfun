class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                adj[i].append([abs(x1 - x2) + abs(y1 - y2), j])
                adj[j].append([abs(x1 - x2) + abs(y1 - y2), i])
        
        visited = set()
        min_heap = [[0, 0]]
        res = 0
        while len(visited) < len(points):
            cost, point = heapq.heappop(min_heap)
            if point in visited:
                continue
            visited.add(point)
            res += cost
            for c, p in adj[point]:
                if p in visited:
                    continue
                heapq.heappush(min_heap, [c, p])
        
        return res
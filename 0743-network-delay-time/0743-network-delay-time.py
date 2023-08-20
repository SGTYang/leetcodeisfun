class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dst, time in times:
            adj[src].append([time, dst])
            
        res = 0
        visited = set()
        min_heap = [[0, k]]
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, time)
            for t, d in adj[node]:
                if d in visited:
                    continue
                heapq.heappush(min_heap, [t + time, d])
        
        return res if len(visited) == n else -1
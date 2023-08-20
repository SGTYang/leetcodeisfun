class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        min_heap = [[grid[0][0], 0, 0]]
        visited.add(0)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        while True:
            t, r, c = heapq.heappop(min_heap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr == n or nc == n or (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                heapq.heappush(min_heap, [max(t, grid[nr][nc]), nr, nc])
        
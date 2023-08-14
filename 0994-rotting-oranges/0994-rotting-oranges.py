class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        m, n = len(grid), len(grid[0])
        
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        que = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    que.append([i, j])
        
        while que and fresh > 0:
            q = len(que)
            for _ in range(q):
                ci, cj = que.popleft()
                for di, dj in direction:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or nj < 0 or ni == m or nj == n or grid[ni][nj] != 1:
                        continue
                    grid[ni][nj] = 2
                    fresh -= 1
                    que.append([ni, nj])
            time += 1
        
        return time if fresh == 0 else -1
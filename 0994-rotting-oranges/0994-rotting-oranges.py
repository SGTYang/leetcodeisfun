class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque([])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        rows, cols = len(grid), len(grid[0])
        
        fresh = time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    que.append((i, j))
                
        while que and fresh:
            n = len(que)
            for _ in range(n):
                r, c = que.popleft()
                for y, x in directions:
                    n_y = y + r
                    n_x = x + c
                    if 0 <= n_y < rows and 0 <= n_x < cols and grid[n_y][n_x] == 1:
                        fresh -= 1
                        grid[n_y][n_x] = 2
                        que.append((n_y, n_x))
            time += 1
        
        return time if not fresh else -1
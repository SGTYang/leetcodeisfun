class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()
        que = deque([])
        time = 0
        fresh = 0
        ROW, COL = len(grid), len(grid[0])
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    que.append([i, j])
                    visited.add((i, j))
        
        while que and fresh:
            n = len(que)
            for _ in range(n):
                r, c = que.popleft()
            
                for y, x in directions:
                    n_r, n_c = y + r, x + c
                    
                    if n_r < 0 or n_c < 0 or n_r >= ROW or n_c >= COL or (n_r, n_c) in visited or grid[n_r][n_c] == 0:
                        continue
                    visited.add((n_r, n_c))
                    que.append((n_r, n_c))
                    grid[n_r][n_c] = 2
                    fresh -= 1
                    
            time += 1
        
        return time if not fresh else -1
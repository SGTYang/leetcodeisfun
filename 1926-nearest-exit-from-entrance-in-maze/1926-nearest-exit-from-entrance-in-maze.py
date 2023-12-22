class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # . : an empty cell
        # # : a wall
        res = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROW, COL = len(maze), len(maze[0])
        
        que = deque([])
        visited = set()
        y, x = entrance
        que.append([y, x, 0])
        visited.add((y, x))
         
        while que:
            r, c, w = que.popleft()
            
            if (r == 0 or c == 0 or r == ROW - 1 or c == COL - 1) and maze[r][c] == "." and w != 0:
                return w
            
            for y, x in directions:
                n_r, n_c = y + r, x + c
                if n_r < 0 or n_c < 0 or n_r >= ROW or n_c >= COL or (n_r, n_c) in visited or maze[n_r][n_c] == "+":
                    continue
                visited.add((n_r, n_c))
                que.append((n_r, n_c, w + 1))
        
        return -1
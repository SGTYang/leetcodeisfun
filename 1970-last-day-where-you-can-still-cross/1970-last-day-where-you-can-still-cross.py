class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def existingPath(mid):
            grid = [[0] * col for _ in range(row)]
            
            for i in range(mid):
                r, c = cells[i]
                grid[r-1][c-1] = 1
            
            # Perform a depth-first search to check if there is a path from top to bottom
            stack = []
            for c in range(col):
                if grid[0][c] == 0:
                    stack.append((0, c))
                    grid[0][c] = 1
            
            while stack:
                r, c = stack.pop()
                if r == row - 1: return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        stack.append((nr, nc))
                        grid[nr][nc] = 1
                        
            return False

        left = 0
        right = len(cells)
        possible_path = 0
        
        while left <= right:
            mid = (left + right) // 2
            if existingPath(mid):
                possible_path = max(possible_path, mid)
                left = mid + 1
            else:
                right = mid - 1
        
        return possible_path
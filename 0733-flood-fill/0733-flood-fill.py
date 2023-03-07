class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        
        start_color = image[sr][sc]
        image[sr][sc] = color
        
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        
        que = deque()
        que.append((sr,sc))
        visited = set((sr,sc))
        while que:
            y,x = que.popleft()
            
            for r,c in directions:
                n_y, n_x = y+r, x+c
                
                if (0<=n_y<len(image) and 0<=n_x<len(image[0]) 
                    and image[n_y][n_x] == start_color and 
                    (n_y, n_x)not in visited):
                    image[n_y][n_x] = color
                    que.append((n_y,n_x))
                    visited.add((n_y,n_x))
        
        return image
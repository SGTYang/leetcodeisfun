class Solution:
    def isPathCrossing(self, path: str) -> bool:
        n = s = e = w = 0
        visited = set()
        origin = [0,0]
        visited.add(tuple(origin))
        
        for c in path:
            if c == "N":
                origin[0] += 1
            elif c == "S":
                origin[0] -= 1
            elif c == "E":
                origin[1] += 1
            else:
                origin[1] -= 1
            
            if tuple(origin) in visited:
                return True
            visited.add(tuple(origin))
        
        return False
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [0]
        visited = set()

        while keys:
            n = len(keys)
            for _ in range(n):
                curr_key = keys.pop()
                if curr_key not in visited:
                    visited.add(curr_key)
                    for k in rooms[curr_key]:
                        keys.append(k)
        
        return len(visited) == len(rooms)
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def bfs(node):
            
            dist = [-1]*len(edges)
            
            visited = set()
            
            dist[node] = 0
            
            que = deque([node])
            
            while que:
                
                n = que.popleft()
                
                if n in visited:
                    continue
                
                visited.add(n)
                neighbor = edges[n]
                
                if neighbor not in visited and neighbor != -1:
                    dist[neighbor] = dist[n]+1
                    que.append(neighbor)
            
            return dist
        
        dist1 = bfs(node1)
        dist2 = bfs(node2)
        
        min_dist = float('inf')
        neighbor_node = -1
        
        for i in range(len(dist1)):
            if dist1[i] == -1 or dist2[i] == -1:
                continue
            
            max_dist = max(dist1[i], dist2[i])
            
            if min_dist > max_dist:
                min_dist = max_dist
                neighbor_node = i
        
        return neighbor_node
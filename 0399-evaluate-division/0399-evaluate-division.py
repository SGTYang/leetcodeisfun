class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        
        for i in range(len(equations)):
            x, y = equations[i]
            adj[x].append((y, values[i]))
            adj[y].append((x, 1/values[i]))
        
        def bfs(q1, q2):
            if q1 not in adj or q2 not in adj:
                return -1.0
            
            que = deque()
            que.append([q1, 1])
            visited = set()
            visited.add(q1)
            
            while que:
                s, w = que.popleft()
                
                if s == q2:
                    return w
                
                for n, weight in adj[s]:
                    if n not in visited:
                        visited.add(n)
                        que.append((n, w * weight))
                        
            return -1.0
            
            
        
        return [bfs(q1, q2) for q1, q2 in queries]
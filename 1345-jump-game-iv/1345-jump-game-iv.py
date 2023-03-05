class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        if n <= 1:
            return 0
        
        graph = defaultdict(list)
        
        for i in range(n):
            graph[arr[i]].append(i)
        
        visited = set()
        que = deque()
        que.append((0,0))
        
        while que:
            node, level = que.popleft()
            
            if node == n-1:
                return level
            
            for child in graph[arr[node]]:
                if child not in visited:
                    que.append((child, level+1))
                    visited.add(child)
                    
            for child in [node-1, node+1]:
                if 0 <= child < n and child not in visited:
                    que.append((child, level+1))
                    visited.add(child)
            
            del graph[arr[node]]

        return -1
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        if not edges and vals:
            return len(vals)
        
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        parent = [i for i in range(len(vals))]
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
            
        subtree = [[val, 1] for val in vals]
        
        res = 0
        
        for curr in sorted(range(len(vals)),key=lambda i:vals[i]):
            x = find(curr)
            for node in graph[curr]:
                y = find(node)
                if x == y or vals[y] > vals[x]:
                    continue
                
                if subtree[x][0] == subtree[y][0]:
                    res += subtree[x][1]*subtree[y][1]
                    subtree[x][1] += subtree[y][1]
                subtree[y] = subtree[x][:]
                parent[y] = x
        return res + len(vals)
            
        # TLE
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        
        self.res = 0
        
        def dfs(node):
            visited.add(node)
            self.res += 1
            counter = Counter([vals[node]])
            for neighbor in graph[node]:
                if neighbor not in visited:
                    for item, freq in dfs(neighbor).items():
                        if item >= vals[node]:
                            self.res += counter[item]*freq
                            counter[item] += freq
            
            return counter
        
        dfs(0)
        
        return self.res
        
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = [0]
        roads = defaultdict(list)
        ways = set()
        visited = set()
        
        
        for start, end in connections:
            roads[start].append(end)
            roads[end].append(start)
            ways.add((start, end))
        
        def dfs(node):
            visited.add(node)
            
            for n in roads[node]:
                if n not in visited:
                    if (n, node) not in ways:
                        res[0] += 1
                    dfs(n)

        dfs(0)
        
        return res[0]
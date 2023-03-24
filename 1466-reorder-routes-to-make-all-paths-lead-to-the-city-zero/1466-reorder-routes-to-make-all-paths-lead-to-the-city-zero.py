class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        city_dict = {city:[] for city in range(n)}
        visited = set()
        ans = 0
        city_set = {(a,b) for a,b in connections}

        for a,b in connections:
            city_dict[a].append(b)
            city_dict[b].append(a)

        
        def dfs(city):
            nonlocal visited, city_dict, ans, city_set
            
            for a in city_dict[city]:
                if a in visited:
                    continue
                if (a, city) not in city_set:
                    ans += 1
                visited.add(a)
                dfs(a)
            
        visited.add(0)
        dfs(0)
        return ans
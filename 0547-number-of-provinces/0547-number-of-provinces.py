class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        province = defaultdict(list)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    province[i].append(j)
                    province[j].append(i)
        
        res = 0
        visited = set()
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in province[node]:
                dfs(n)
        
        for n in province.keys():
            if n not in visited:
                res += 1
                dfs(n)
        
        return res
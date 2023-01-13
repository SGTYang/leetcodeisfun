class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        edge = defaultdict(list)
        
        for i in range(1,len(parent)):
            edge[parent[i]].append(i)
        
        ans = 1
        
        def dfs(node):
            nonlocal ans
            if not edge[node]:
                return 1
            
            res = 1
            
            for leaf in edge[node]:
                child = dfs(leaf)
                if s[node] != s[leaf]:
                    ans = max(child+res, ans)
                    res = max(child+1, res)
                
            return res
        
        dfs(0)
        return ans
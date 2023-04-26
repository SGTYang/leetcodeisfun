class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(idx):
            if len(subset) == k:
                res.append(subset.copy())
                return
            
            for i in range(idx, n+1):
                subset.append(i)
                dfs(i+1)
                subset.pop()
        
        dfs(1)
        return res
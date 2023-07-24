class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(i, bucket):
            if i > n+1:
                return
            if len(bucket) == k:
                res.append(bucket.copy())
                return
            
            bucket += [i]
            dfs(i + 1, bucket)
            bucket.pop()
            dfs(i + 1, bucket)
            
        dfs(1, [])
        
        return res
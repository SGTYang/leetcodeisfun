class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Time: O(k * 2^n)
        # Space: O(k)
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
        
        # Time: O(k * n^k)
        # Space: O(k)
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
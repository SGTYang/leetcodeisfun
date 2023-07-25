class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Time: O(k * 9^k)
        # Space: O(k)
        res = []
        
        def dfs(idx, total, curr):
            if total > n or len(curr) > k:
                return
            if len(curr) == k and total == n:
                res.append(curr.copy())
                return
            
            for i in range(idx, 10):
                curr.append(i)
                dfs(i + 1, total + i, curr)
                curr.pop()
        
        dfs(1, 0, [])
        
        return res
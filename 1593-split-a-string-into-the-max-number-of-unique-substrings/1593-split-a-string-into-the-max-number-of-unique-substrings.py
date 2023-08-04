class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited = set()
        
        def dfs(idx):
            cnt = 0
            for i in range(idx + 1, len(s) + 1):
                if s[idx:i] in visited:
                    continue
                visited.add(s[idx:i])
                cnt = max(cnt, dfs(i) + 1)
                visited.remove(s[idx:i])
            
            return cnt
        
        return dfs(0)
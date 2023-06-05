class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        
        def trev(u):
            if not visited[u]:
                visited[u] = True
                for i in range(n):
                    if isConnected[i][u]:
                        trev(i)
                        
        ans = 0
        for i in range(n):
            if not visited[i]:
                trev(i)
                ans+=1
        return ans
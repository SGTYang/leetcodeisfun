class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        par = [i for i in range(len(isConnected))]
        rank = [1]*len(isConnected)
        res = len(isConnected)
        
        def find(node):
            res = node
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    res -= union(i, j)
        
        return res
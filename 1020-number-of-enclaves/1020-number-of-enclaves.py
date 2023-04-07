class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        row, col = len(A), len(A[0])

        if not A or not A[0]:
            return 0

        def dfs(x,y,A):
            if 0<=x<row and 0<=y<col and A[x][y] ==1:
                A[x][y] = "T"
                dfs(x+1,y,A)
                dfs(x-1,y,A)
                dfs(x,y+1,A)
                dfs(x,y-1,A)


        for x in range(row):
            dfs(x,0,A)
            dfs(x,col-1,A)

        for y in range(1,col-1):
            dfs(0,y,A)
            dfs(row-1,y,A)

        count=0
        for x in range(row):
            for y in range(col):
                if A[x][y]==1:
                    count+=1

        return count
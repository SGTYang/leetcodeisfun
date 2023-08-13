class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for j in range(n)]
        col = set()
        pos_diag = set()
        neg_diag = set()
        res = []
        
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c not in col and r - c not in pos_diag and r + c not in neg_diag:
                    board[r][c] = "Q"
                    col.add(c)
                    pos_diag.add(r - c)
                    neg_diag.add(r + c)
                    dfs(r + 1)
                    col.remove(c)
                    pos_diag.remove(r - c)
                    neg_diag.remove(r + c)
                    board[r][c] = "."
        
        dfs(0)
            
        return res
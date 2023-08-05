class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        
        row = [set() for i in range(m)]
        col = [set() for i in range(n)]
        box = [[set() for j in range(n//3)] for i in range(m//3)]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in box[i//3][j//3] or board[i][j] in row[i] or board[i][j] in col[j]:
                    return False
                if board[i][j] != ".":
                    box[i//3][j//3].add(board[i][j])
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
        
        return True
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Space: O(len(word)). This is the space required to store the recursive stack during the DFS search.
        # Time: O(n * m) * dfs -> O(n * m * 4^len(word)) 
        # The call stack of dfs is going to be len(word)
        # So 4^len(word)
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[idx] or (i, j) in visited:
                return False
            visited.add((i, j))
            
            res = (dfs(i + 1, j, idx + 1) or
                   dfs(i - 1, j, idx + 1) or
                   dfs(i, j + 1, idx + 1) or 
                   dfs(i, j - 1, idx + 1))
            visited.remove((i, j))
            return res
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
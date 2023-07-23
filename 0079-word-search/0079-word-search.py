class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Space: O(len(word)). This is the space required to store the recursive stack during the DFS search.
        # Time: O(n * m) * dfs -> O(n * m * 4^len(word)) 
        # The call stack of dfs is going to be len(word)
        # So 4^len(word)
        
        visited = set()
        m, n = len(board), len(board[0])
        
        def backtrack(i,j, idx):
            if idx == len(word):
                return True
            
            if (i,j) in visited or i >= m or j >= n or i < 0 or j < 0 or board[i][j] != word[idx]:
                return False
            
            visited.add((i,j))
            
            res = (backtrack(i + 1, j, idx+1) or
                backtrack(i - 1, j, idx+1) or
                backtrack(i, j - 1, idx+1) or
                backtrack(i, j + 1, idx+1))
            
            visited.remove((i,j))
            
            return res
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        
        return False
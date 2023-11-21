class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add(self, word):
        trie = self
        for c in word:
            if c not in trie.children:
                trie.children[c] = TrieNode()
            trie = trie.children[c]
        trie.is_word = True

        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = TrieNode()
        row, col = len(board), len(board[0])
        for word in words:
            t.add(word)
            
        visited = set()
        res = set()
        
        def dfs(i, j, trie, word):
            if i < 0 or j < 0 or i >= row or j >= col or (i, j) in visited or board[i][j] not in trie.children:
                return
            
            visited.add((i, j))
            trie = trie.children[board[i][j]]
            word = word + board[i][j]
            
            if trie.is_word:
                res.add(word)
                trie.is_word = False
            
            dfs(i - 1, j, trie, word)
            dfs(i + 1, j, trie, word)
            dfs(i, j - 1, trie, word)
            dfs(i, j + 1, trie, word)
            
            visited.remove((i, j))
            
        for i in range(row):
            for j in range(col):
                dfs(i, j, t, "")
                
        return list(res)
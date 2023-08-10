class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add(self, word):
        trie = self
        for c in word:
            if c not in trie.children:
                trie.children[c] = Trie()
            trie = trie.children[c]
        trie.is_word = True
    
    def prune_word(self, word):
        curr = self
        node_and_child = []
        for c in word:
            node_and_child.append((curr, c))
            curr = curr.children[c]
        
        for i in range(len(node_and_child)-1, -1, -1):
            parent, child = node_and_child[i]
            target = parent.children[child]
            if len(target.children) == 0:
                del parent.children[child]
            else:
                return
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.add(word)
        visited = set()
        res = set()
        
        def dfs(i, j, node, word):
            if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited or board[i][j] not in node.children:
                return
        
            visited.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]
            
            if node.is_word:
                res.add(word)
                node.is_word = False
                trie.prune_word(word)
            
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j - 1, node, word)
            dfs(i, j + 1, node, word)
            
            visited.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")
        
        return list(res)
            
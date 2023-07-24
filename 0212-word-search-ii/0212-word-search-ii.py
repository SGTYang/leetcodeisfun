class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True
    
    def prune_word(self, word):
        curr = self
        node_and_child = []
        for c in word:
            node_and_child.append((curr, c))
            curr = curr.children[c]
        
        for i in range(len(node_and_child)-1, -1, -1):
            p, c = node_and_child[i]
            target = p.children[c]
            if len(target.children) == 0:
                del p.children[c]
            else:
                return
            
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for word in words:
            root.add(word)
        
        m, n = len(board), len(board[0])
        visited = set()
        res = set()
        
        def dfs(i, j, node, word):
            if i >= m or j >= n or i < 0 or j < 0 or (i, j) in visited or board[i][j] not in node.children:
                return
            visited.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]
            
            if node.is_word:
                res.add(word)
                node.is_word = False
                root.prune_word(word)
            
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)
            
            visited.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
        
        return list(res)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        t = self.trie
        for c in word:
            if c not in t.children:
                t.children[c] = TrieNode()
            t = t.children[c]
        t.is_word = True
           

    def search(self, word: str) -> bool:
        def dfs(idx, trie):
            curr = trie
            for i in range(idx, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.is_word
        return dfs(0, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
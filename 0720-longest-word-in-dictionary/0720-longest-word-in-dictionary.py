class TrieNode:
    def __init__(self, val):
        self.children = {}
        self.val = val
        self.is_word = False
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        res = ""
        max_len = 0
        trie = TrieNode(0)
        
        for word in words:
            t = trie
            cnt = 0
            for c in word:
                if c not in t.children:
                    t.children[c] = TrieNode(cnt)
                t = t.children[c]
                if t.is_word:
                    cnt += 1
            t.is_word = True
            t.val += 1
            
            if t.val == len(word) and t.val > max_len:
                max_len = t.val
                res = word
        return res
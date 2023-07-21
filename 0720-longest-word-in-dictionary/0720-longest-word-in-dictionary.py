class TrieNode:
    def __init__(self, val):
        self.child = {}
        self.val = val
        self.end_of_word = False
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = TrieNode(0)
        
        max_len = 0
        res = ""
        
        for word in sorted(words):
            t = trie
            cnt = 0
            
            for c in word:
                if c not in t.child:
                    t.child[c] = TrieNode(cnt)
                t = t.child[c]
                if t.end_of_word:
                    cnt += 1
            
            t.end_of_word = True
            t.val += 1
            
            if t.val == len(word) and t.val > max_len:
                max_len = t.val
                res = word
        
        return res
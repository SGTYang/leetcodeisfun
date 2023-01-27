class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        word_set = set(words)
        res = []
        
        def dfs(word):
            
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if ((prefix in word_set and suffix in word_set) or 
                    (prefix in word_set and dfs(suffix))):
                    return True
                   
        for w in words:
            if dfs(w):
                res.append(w)
        return res
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # Time: O(2^num of alphabets + num of numbers)
        # Space: O(n)
        
        res = []

        def dfs(i, word):
            if len(word) == len(s):
                res.append(word)
                return
            
            if s[i].isalpha():
                if s[i].islower():
                    dfs(i+1, word+s[i].upper())
                else:
                    dfs(i+1, word+s[i].lower())
                    
            dfs(i+1, word+s[i])
        
        dfs(0, "")
        return res
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtracking(i, word):
            if i >= len(s):
                res.append(word)
                return

            if s[i].isalpha():
                if s[i].islower():
                    backtracking(i+1, word+s[i].upper())
                else:
                    backtracking(i+1, word+s[i].lower())
            backtracking(i+1, word+s[i])
        
        backtracking(0, "")
        
        return res
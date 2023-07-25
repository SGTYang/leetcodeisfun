class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        
        def dfs(idx, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for c in digit[digits[idx]]:
                dfs(idx+1, curr+c)
        
        dfs(0, "")
        if digits == "":
            return []
        return res
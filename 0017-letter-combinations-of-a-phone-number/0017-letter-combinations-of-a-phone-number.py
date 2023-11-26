class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        
        res = []
        
        def dfs(idx, curr):
            if idx == len(digits):
                res.append("".join(curr))
                return
            
            for c in dig[digits[idx]]:
                curr.append(c)
                dfs(idx + 1, curr)
                curr.pop()
        
        dfs(0, [])
        
        return res if digits else []
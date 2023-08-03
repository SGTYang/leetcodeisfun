class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        curr = []
        def dfs(idx):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return
            if idx >= len(digits):
                return
            
            for c in num_dict[digits[idx]]:
                curr.append(c)
                dfs(idx+1)
                curr.pop()
        
        dfs(0)
        if digits == "":
            return []
        
        return res
                    
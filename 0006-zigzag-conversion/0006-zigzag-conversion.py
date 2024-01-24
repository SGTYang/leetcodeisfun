class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res = []
        for i in range(numRows):
            increment = 2 * (numRows - 1)
            for j in range(i, len(s), increment):
                res.append(s[j])
                if i > 0 and i < numRows - 1 and j + increment - 2 * i < len(s):
                    res.append(s[j + increment - 2 * i])
            
        return "".join(res)
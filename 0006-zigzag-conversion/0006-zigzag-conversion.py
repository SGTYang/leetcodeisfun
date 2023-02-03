class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        res = [""]*numRows

        pointer = 0
        
        l = len(s)
        
        for i in range(l):
            if pointer == 0:
                operator = 1
            elif pointer == numRows-1:
                operator = -1
            
            res[pointer] += s[i]
            
            pointer += operator
            
        return "".join(res) 
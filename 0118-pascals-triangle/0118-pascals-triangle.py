class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for i in range(numRows):
            row = [0] * (i + 1)
            row[0], row[-1] = 1, 1
            for j in range(1, i):
                row[j] = res[-1][j - 1] + res[-1][j]
            res.append(row)
        
        return res
                
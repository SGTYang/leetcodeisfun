class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(img), len(img[0])
        
        res = [[0 for i in range(COL)] for j in range(ROW)]
        
        def smooth(i, j):
            total = 0
            cnt = 0
            for r in range(max(0, i - 1), min(ROW, i + 2)):
                for c in range(max(0, j - 1), min(COL, j + 2)):
                    total += img[r][c]
                    cnt += 1
            
            return math.floor(total / cnt)
        
        
        for i in range(ROW):
            for j in range(COL):
                res[i][j] = smooth(i, j)
        
        return res
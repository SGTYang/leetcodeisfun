class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(img), len(img[0])
        
        def smooth(i, j):
            total = 0
            cnt = 0
            for r in range(max(0, i - 1), min(ROW, i + 2)):
                for c in range(max(0, j - 1), min(COL, j + 2)):
                    total += img[r][c] % 256
                    cnt += 1
            
            return img[i][j] ^ (total // cnt) << 8
        
        
        for i in range(ROW):
            for j in range(COL):
                img[i][j] = smooth(i, j)
        
        for i in range(ROW):
            for j in range(COL):
                img[i][j] = img[i][j] >> 8
        
        return img
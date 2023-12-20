class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_p = defaultdict(int)
        res = 0
        for i in range(len(grid[0])):
            tmp = []
            for j in range(len(grid)):
                tmp.append(grid[j][i])
            row_p[tuple(tmp)] += 1
        
        for i in range(len(grid)):
            if tuple(grid[i]) in row_p:
                res += row_p[tuple(grid[i])]
        
        return res
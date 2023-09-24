class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cups = [[0 for j in range(i + 1)] for i in range(query_row + 1)]
        cups[0][0] = poured
        
        for i in range(query_row):
            for j in range(len(cups[i])):
                half = (cups[i][j] - 1) / 2.0
                if half > 0:
                    cups[i + 1][j] += half
                    cups[i + 1][j + 1] += half
        return cups[query_row][query_glass] if cups[query_row][query_glass] <= 1 else 1
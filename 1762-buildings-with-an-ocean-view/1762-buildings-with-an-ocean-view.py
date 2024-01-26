class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        right_max = 0
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > right_max:
                res.append(i)
                right_max = heights[i]
        res = res[::-1]
        return res
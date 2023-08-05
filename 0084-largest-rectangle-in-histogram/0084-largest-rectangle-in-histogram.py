class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][0] > heights[i]:
                height, index = stack.pop()
                res = max(res, (i - index) * height)
            stack.append([heights[i], index])
        
        while stack:
            height, idx = stack.pop()
            res = max(res, (len(heights) - idx) * height)
        
        return res
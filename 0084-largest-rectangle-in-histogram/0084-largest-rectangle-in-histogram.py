class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # start, height
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append([start, heights[i]])
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area
            
        
        # O(n**2)
        res = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                res = max(res, (j - i) * min(heights[i], heights[j]))
        
        return res
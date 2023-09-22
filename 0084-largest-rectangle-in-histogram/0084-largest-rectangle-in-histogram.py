class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # [index, height]
        
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx, h = stack.pop()
                max_area = max(max_area, (i - idx) * h)
                start = idx
            stack.append([start, heights[i]])
        
        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)
        
        return max_area
            
        
        # O(n**2)
        res = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                res = max(res, (j - i) * min(heights[i], heights[j]))
        
        return res
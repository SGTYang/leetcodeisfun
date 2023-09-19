class Solution:
    def trap(self, height: List[int]) -> int:
#         # Time O(N)
#         # Space O(N)
#         n = len(height)
#         max_left = [0 for i in range(n)]
#         max_right = [0 for i in range(n)]
        
#         curr = height[0]
#         for i in range(1, n):
#             curr = max(curr, height[i - 1])
#             max_left[i] = curr
        
#         curr = height[-1]
#         for i in range(n - 2, -1, -1):
#             curr = max(curr, height[i + 1])
#             max_right[i] = curr
        
#         res = 0
#         for i in range(n):
#             water = min(max_left[i], max_right[i]) - height[i]
#             res += water if water > 0 else 0
        
#         return res
        
        # Time O(N)
        # Space O(1)
        
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        res = 0
        
        while left < right:
            if max_left <= max_right:
                left += 1
                water = max_left - height[left]
                max_left = max(max_left, height[left])
            else:
                right -= 1
                water = max_right - height[right]
                max_right = max(max_right, height[right])
            res += water if water > 0 else 0
        
        return res
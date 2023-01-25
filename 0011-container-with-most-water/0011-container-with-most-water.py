class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        
        max_water = 0
        
        while left < right:
            
            curr = (right-left)*min(height[left],height[right])
            
            max_water = max(max_water, curr)
            
            if height[left] == height[right]:
                left += 1
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_water
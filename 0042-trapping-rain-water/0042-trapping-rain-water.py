class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_r = [0 for i in range(n)]
        max_l = [0 for i in range(n)]
        res = [0 for i in range(n)]
        
        curr_max = height[0]
        for i in range(1, n):
            curr_max = max(curr_max, height[i-1])
            max_l[i] = curr_max
            
        curr_max = height[n-1]
        for i in range(n-2,-1,-1):
            curr_max = max(curr_max, height[i+1])
            max_r[i] = curr_max
        
        for i in range(n):
            water = min(max_l[i], max_r[i]) - height[i]
            if water < 0:
                water = 0
            res[i] = water
        
        return sum(res)
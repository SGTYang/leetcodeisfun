class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0
        
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        
        return res
        
        # Time complexity: O(n)
        # Space complexity: O(n)
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
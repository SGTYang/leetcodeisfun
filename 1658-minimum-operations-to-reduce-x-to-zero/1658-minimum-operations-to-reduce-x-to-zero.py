class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        curr_sum = 0
        max_window = -1
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            
            while l <= r and curr_sum > target:
                curr_sum -= nums[l]
                l += 1
                
            if curr_sum == target:
                max_window = max(max_window, r - l + 1)    
        
        return -1 if max_window == -1 else len(nums) - max_window        
        
        
        res = []
        def dfs(left, right, x, cnt):
            if x < 0 or left > right or left == len(nums) or right == -1:
                return
            
            if x - nums[left] == 0:
                res.append(cnt + 1)
            
            if x - nums[right] == 0:
                res.append(cnt + 1)

            dfs(left + 1, right, x - nums[left], cnt + 1)
            dfs(left, right - 1, x - nums[right], cnt + 1)
        
        dfs(0, len(nums)-1, x, 0)
        
        return min(res) if res else -1
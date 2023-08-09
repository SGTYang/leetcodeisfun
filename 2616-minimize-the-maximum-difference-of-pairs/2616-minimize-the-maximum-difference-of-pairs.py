class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        min_max_diff = 0
        max_max_diff = nums[-1] - nums[0]
        
        while min_max_diff < max_max_diff:
            mid_max_diff = (min_max_diff + max_max_diff) // 2
            
            pair_count = 0
            i = 1
            while i < n:
                if nums[i] - nums[i-1] <= mid_max_diff:
                    pair_count += 1
                    i += 1
                i += 1
            
            if pair_count >= p:
                max_max_diff = mid_max_diff
            
            else:
                min_max_diff = mid_max_diff + 1
        
        return min_max_diff
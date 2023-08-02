class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                curr_diff = abs(target - total)
                if curr_diff < diff:
                    res = total
                    diff = curr_diff
                
                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return res
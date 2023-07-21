class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        res = sum(nums[:3])
        nums.sort()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            
            while left < right:
                n_sum = nums[i] + nums[left] + nums[right]
                
                curr_diff = abs(target - n_sum)
                
                if curr_diff < diff:
                    diff = curr_diff
                    res = n_sum
                
                if n_sum < target:
                    left += 1
                else:
                    right -= 1

        return res
                
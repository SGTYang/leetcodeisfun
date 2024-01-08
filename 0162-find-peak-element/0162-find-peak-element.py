class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Adjacent neighbors are not same
        if len(nums) < 2 or nums[0] > nums[1]:
            return 0
        
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid-1] < nums[mid] > nums[mid + 1]:
                return mid
            
            elif nums[mid - 1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
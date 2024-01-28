class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Adjacent neighbors are not same
        # go thorugh all the elements and check their neighbors
        # [1, 9, 10, 2, 4, -1, 2, -4]
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # left nei is greater
            if mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1
            # right nei is greater
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                return mid
        
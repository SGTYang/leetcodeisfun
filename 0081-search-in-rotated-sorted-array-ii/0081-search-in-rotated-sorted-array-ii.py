class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[left]:
                left += 1
                continue
            if nums[mid] == nums[right]:
                right -= 1
                continue
            
            if nums[left] <= nums[mid]:
                if target > nums[mid] or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return False
    
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return True
            if nums[mid] == nums[l]:
                l += 1
                continue
            if nums[mid] == nums[r]:
                r -= 1
                continue
                
            # Left sorted portion
            if nums[l] <= nums[mid]:
                if nums[mid] < target or nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1  
            # Right sorted portion
            else:
                if nums[mid] > target or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return False
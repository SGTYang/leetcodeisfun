class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # 4 5 6 7 0 1 2
        # 1 2 3 4 5 6 7
        
        left, right = 0, len(nums)-1
        ans = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                return min(ans, nums[left])
            mid = (left+right)//2
            ans = min(ans, nums[mid])
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
                
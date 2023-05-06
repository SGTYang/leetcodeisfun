class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. l < mid, r < l, r < mid
        # 2. l > mid, mid < r, 
        # 3. l < mid, r > l, r > mid
        
        l, r = 0, len(nums)-1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l+r)//2
            res = min(res, nums[mid])
            if nums[r] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res
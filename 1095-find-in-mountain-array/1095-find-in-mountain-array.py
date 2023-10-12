# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        
        left, right = 1, length - 2
        
        while left <= right:
            mid = (left + right) // 2
            l, m, r = mountain_arr.get(mid-1), mountain_arr.get(mid), mountain_arr.get(mid+1)
            
            if l < m < r:
                left = mid + 1
            elif l > m > r:
                right = mid - 1
            else:
                break
        
        peak = mid
        
        left, right = 0, peak
        while left <= right:
            mid = (left + right)//2
            val = mountain_arr.get(mid)
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return mid
        
        left, right = peak, length - 1
        while left <= right:
            mid = (left + right)//2
            val = mountain_arr.get(mid)
            if val > target:
                left = mid + 1
            elif val < target:
                right = mid - 1
            else:
                return mid
        
        return -1
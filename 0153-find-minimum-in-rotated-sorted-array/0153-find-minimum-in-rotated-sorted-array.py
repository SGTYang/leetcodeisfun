class Solution:
    def findMin(self, nums: List[int]) -> int:
        first, last = 0, len(nums) - 1
        while first < last:
            midpoint = (first + last) // 2
            if nums[midpoint] > nums[last]:
                first = midpoint + 1
            else:
                last = midpoint
        return nums[first]
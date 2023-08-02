class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Partition with two pointers
        i, left, right = 0, 0, len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                i -= 1
            i += 1
        
        
#         # Bucket Sort
#         bucket = [0] * 3
        
#         for num in nums:
#             bucket[num] += 1
        
#         left = 0
#         for i in range(len(bucket)):
#             right = left + bucket[i]
#             for j in range(left, right):
#                 nums[j] = i
#             left = right
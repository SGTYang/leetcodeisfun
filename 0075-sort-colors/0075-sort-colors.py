class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Partition with two pointers
        left, right, pointer = 0, len(nums) - 1, 0
        
        while pointer <= right:
            if nums[pointer] == 0:
                nums[pointer], nums[left] = nums[left], nums[pointer]
                left += 1
            elif nums[pointer] == 2:
                nums[pointer], nums[right] = nums[right], nums[pointer]
                right -= 1
                pointer -= 1
            pointer += 1
        
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
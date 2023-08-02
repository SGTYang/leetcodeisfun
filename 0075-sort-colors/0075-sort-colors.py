class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bucket Sort
        bucket = [0] * 3
        
        for num in nums:
            bucket[num] += 1
        
        left = 0
        for i in range(len(bucket)):
            right = left + bucket[i]
            for j in range(left, right):
                nums[j] = i
            left = right
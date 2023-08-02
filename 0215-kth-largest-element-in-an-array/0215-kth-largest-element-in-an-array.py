class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Quick select
        
        k = len(nums) - k # Kth largest
        
        def quick_select(left, right):
            pivot, pointer = nums[right], left
            
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1
            
            nums[right], nums[pointer] = nums[pointer], nums[right]
            
            if k > pointer:
                return quick_select(pointer + 1, right)
            elif k < pointer:
                return quick_select(left, pointer - 1)
            else:
                return nums[pointer]
        
        return quick_select(0, len(nums) - 1)
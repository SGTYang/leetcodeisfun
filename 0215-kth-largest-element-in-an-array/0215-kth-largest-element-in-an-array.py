class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quick select
        k = len(nums) - k # kth largest
        
        def quick_select(l, r):
            pivot, p_pointer = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p_pointer], nums[i] = nums[i], nums[p_pointer]
                    p_pointer += 1
            
            nums[p_pointer], nums[r] = pivot, nums[p_pointer]
            
            if p_pointer > k:
                return quick_select(l, p_pointer - 1)
            elif p_pointer < k:
                return quick_select(p_pointer + 1, r)
            else:
                return nums[p_pointer]
        
        return quick_select(0, len(nums) - 1)
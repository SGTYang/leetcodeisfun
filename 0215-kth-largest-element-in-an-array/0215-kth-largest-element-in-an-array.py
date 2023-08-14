class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Quick select
        k = len(nums) - k
        def quick_select(left, pivot):
            l = pointer = left
            while l < pivot:
                if nums[pivot] >= nums[l]:
                    nums[pointer], nums[l] = nums[l], nums[pointer]
                    pointer += 1
                l += 1
            nums[pivot], nums[pointer] = nums[pointer], nums[pivot]
            if pointer < k:
                return quick_select(pointer + 1, pivot)
            elif pointer > k:
                return quick_select(left, pointer - 1)
            else:
                return nums[pointer]
        
        return quick_select(0, len(nums) - 1)
        
        # Time O(klogn)
        # Max heap
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        while k:
            res = heapq.heappop(max_heap)
            k -= 1
        
        return -res
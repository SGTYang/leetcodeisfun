class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Quick select
        n = len(nums)
        k = n - k
        
        def quick_select(l, pivot):
            pointer = l
            left = l
            while left < pivot:
                if nums[left] <= nums[pivot]:
                    nums[left], nums[pointer] = nums[pointer], nums[left]
                    pointer += 1
                left += 1
            nums[pivot], nums[pointer] = nums[pointer], nums[pivot]
            
            if pointer > k:
                return quick_select(l, pointer - 1)
            elif pointer < k:
                return quick_select(pointer + 1, pivot)
            else:
                return nums[pointer]
            
        return quick_select(0, n - 1)
        
        
        # # Time: O(klogn)
        # max_heap = [-num for num in nums]
        # heapq.heapify(max_heap)
        # while k:
        #     res = heapq.heappop(max_heap)
        #     k -= 1
        # return -res
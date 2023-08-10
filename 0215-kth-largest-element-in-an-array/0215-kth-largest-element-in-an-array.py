class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Quick select
        
        # Time: O(klogn)
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        while k:
            res = heapq.heappop(max_heap)
            k -= 1
        return -res
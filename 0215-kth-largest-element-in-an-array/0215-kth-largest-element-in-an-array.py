class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Does this input array contains negative numbers?
        # Does this input array contains duplicate numbers?
        # [-1, 2, 3, 4, 5, 0, 2, -8]
        # Can I use built in python function
        
        # Heap
        # [-5, -4, -3, -2, -2, 0, 1, 8]
        # k = 3 -> res = 5 k = 2, res = 4 k = 1, res = 3 k =0
        # O(N + Klogn)
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        
        while k:
            res = -heapq.heappop(heap)
            k -= 1
            
        return res
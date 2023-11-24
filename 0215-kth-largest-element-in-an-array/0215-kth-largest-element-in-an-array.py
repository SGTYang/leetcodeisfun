class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Quick select
        
        
        # Time O(klogn)
        # Max heap
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]
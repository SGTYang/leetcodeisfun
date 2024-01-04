class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [[n1, n2] for n1, n2 in zip(nums1, nums2)]
        pairs.sort(key = lambda x : x[1], reverse = True)
        
        res = 0
        curr = 0
        
        min_heap = []
        
        for n1, n2 in pairs:
            curr += n1
            heapq.heappush(min_heap, n1)
            
            if len(min_heap) > k:
                curr -= heapq.heappop(min_heap)
            
            if len(min_heap) == k:
                res = max(res, n2 * curr)
            
        
        return res
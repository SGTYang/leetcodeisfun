class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        res = []
        j = 0
        for i in range(min(len(nums1), k)):
            heapq.heappush(minHeap, (nums1[i]+nums2[0], i, j, j))
        
        
        while minHeap and len(res) < k:
            minSum, n, m, j = heapq.heappop(minHeap)
            res.append([nums1[n],nums2[m]])
            if j < len(nums2)-1:
                heapq.heappush(minHeap, (nums1[n]+nums2[j+1], n, j+1, j+1))
        
        return res
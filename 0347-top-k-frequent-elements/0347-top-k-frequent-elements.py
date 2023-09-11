class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        max_heap = []
        for num,cnt in count.items():
            heapq.heappush(max_heap, [-cnt, num])
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        
        return res
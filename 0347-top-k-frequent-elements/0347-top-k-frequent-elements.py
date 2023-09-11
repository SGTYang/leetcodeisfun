class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket
        res = []
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for freq,v in count.items():
            buckets[v].append(freq)
        
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i] != []:
                for num in buckets[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
        
        # Heap
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
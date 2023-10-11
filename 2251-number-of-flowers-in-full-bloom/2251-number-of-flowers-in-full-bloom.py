class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = [(p, i) for i, p in enumerate(people)]
        res = [0] * len(people)
        count = 0
        start_heap = [f[0] for f in flowers]
        end_heap = [f[1] for f in flowers]
        heapq.heapify(start_heap)
        heapq.heapify(end_heap)
        
        for p, i in sorted(people):
            while start_heap and start_heap[0] <= p:
                heapq.heappop(start_heap)
                count += 1
            
            while end_heap and end_heap[0] < p:
                heapq.heappop(end_heap)
                count -= 1
            
            res[i] = count
        
        return res
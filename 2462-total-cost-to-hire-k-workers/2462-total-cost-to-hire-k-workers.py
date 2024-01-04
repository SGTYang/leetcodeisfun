class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        res = []
        
        left, right = 0, len(costs) - 1
        
        while left < candidates:
            heapq.heappush(heap, (costs[left], left))
            left += 1
            
        while right >= len(costs) - candidates and left <= right:
            heapq.heappush(heap, (costs[right], right))
            right -= 1
        
        while len(res) < k:            
            v, i = heapq.heappop(heap)
            res.append(v)
            
            if i < left and left <= right:
                heapq.heappush(heap, (costs[left], left))
                left += 1
            
            elif i > right and left <= right:
                heapq.heappush(heap, (costs[right], right))
                right -= 1

        return sum(res)
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        maxheap = []
        minheap = []
        for i in range(1,n):
            heappush(minheap,weights[i]+weights[i-1])
            heappush(maxheap,-(weights[i]+weights[i-1]))
        
        M, m = 0, 0
        
        for _ in range(k-1):
            M += -heappop(maxheap)
            m += heappop(minheap)
            
        return M-m
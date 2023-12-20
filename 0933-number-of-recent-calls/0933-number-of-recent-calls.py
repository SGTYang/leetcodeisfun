class RecentCounter:
    def __init__(self):
        self.heap = []
        
    def ping(self, t: int) -> int:
        heapq.heappush(self.heap, t)
        
        while self.heap[0] > t or self.heap[0] < t - 3000:
            heapq.heappop(self.heap)
        
        return len(self.heap)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
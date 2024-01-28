class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.curr = deque([])
        self.total = 0

    def next(self, val: int) -> float:
        self.total += val
        self.curr.append(val)
        
        if len(self.curr) > self.size:
            self.total -= self.curr.popleft()

        return self.total / len(self.curr)
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
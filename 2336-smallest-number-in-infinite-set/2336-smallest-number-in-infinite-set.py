class SmallestInfiniteSet:

    def __init__(self):
        self.pop_set = set()
        self.min_num = 1
        
    def popSmallest(self) -> int:
        res = self.min_num
        self.pop_set.add(self.min_num)
        
        while self.min_num in self.pop_set:
            self.min_num += 1
        return res
        
    def addBack(self, num: int) -> None:
        if num in self.pop_set:
            self.min_num = min(num, self.min_num)
            self.pop_set.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
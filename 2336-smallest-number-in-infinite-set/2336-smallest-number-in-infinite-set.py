class SmallestInfiniteSet:
    def __init__(self):
        self.pop = set()
        
    def popSmallest(self) -> int:
        pointer = 1
        while pointer in self.pop:
            pointer += 1
        
        self.pop.add(pointer)
        return pointer

    def addBack(self, num: int) -> None:
        if num in self.pop:
            self.pop.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
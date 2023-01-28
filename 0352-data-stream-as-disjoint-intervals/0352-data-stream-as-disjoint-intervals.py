from sortedcontainers import SortedSet
class SummaryRanges:

    def __init__(self):
        self.tree_map = SortedSet()
        

    def addNum(self, value: int) -> None:
        self.tree_map.add(value)
        

    def getIntervals(self) -> List[List[int]]:
        res = []
        for n in self.tree_map:
            if res and res[-1][1] +1 == n:
                res[-1][1] = n
            else:
                res.append([n, n])
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
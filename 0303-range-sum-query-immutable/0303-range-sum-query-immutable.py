class NumArray:

    def __init__(self, nums: List[int]):
        self.num_list = nums

    def sumRange(self, left: int, right: int) -> int:
        if left > right or right > len(self.num_list):
            return None
        return sum(self.num_list[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
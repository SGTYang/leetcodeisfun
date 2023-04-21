class NumArray:

    def __init__(self, nums: List[int]):
        self.list_sum = [0]*len(nums)
        self.list_sum[0] = nums[0]
        for i in range(1,len(nums)):
            self.list_sum[i] = self.list_sum[i-1]+nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        if left > right or right > len(self.list_sum):
            return None
        if left > 0:
            return self.list_sum[right]-self.list_sum[left-1]
        return self.list_sum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
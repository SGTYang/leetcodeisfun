class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_sum = sum(set(nums))
        return set_sum*2-sum(nums)
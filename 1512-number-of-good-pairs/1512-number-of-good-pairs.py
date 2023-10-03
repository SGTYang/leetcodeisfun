class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_count = defaultdict(int)
        res = 0
        for num in nums:
            num_count[num] += 1
        
        for cnt in num_count.values():
            res += cnt * (cnt - 1) // 2
        
        return res
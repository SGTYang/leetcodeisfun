class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        total_sum = 0
        
        for n in nums:
            total_sum += n
            prefix_sum = total_sum - k
            if prefix_sum in prefix:
                res += prefix[prefix_sum]
            prefix[total_sum] += 1
        
        return res
        
        res = 0
        
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    res += 1
        
        return res
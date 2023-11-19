class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        num_range = 5*10**4 + 1
        print(num_range)
        freq = [0] * num_range
        
        for num in nums:
            freq[num] += 1
            
        res, operations = 0, 0
        
        for i in range(num_range - 1, 0, -1):
            if freq[i] > 0:
                operations += freq[i]
                res += operations - freq[i]
        return res
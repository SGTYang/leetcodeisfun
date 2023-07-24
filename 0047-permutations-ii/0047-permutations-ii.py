class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        num_count = defaultdict(int)
        
        for num in nums:
            num_count[num] += 1
        
        def dfs(bucket):
            if len(bucket) == len(nums):
                res.append(bucket.copy())
                return
            
            for n in num_count:
                if num_count[n] > 0:
                    num_count[n] -= 1
                    bucket += [n]
                    dfs(bucket)
                    num_count[n] += 1
                    bucket.pop()
                    
        dfs([])
        
        return res
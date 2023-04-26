class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    subset.append(n)
                    count[n] -= 1
                    
                    dfs()
                    
                    count[n] += 1
                    subset.pop()
        dfs()
        return res
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = defaultdict(int)
        res = [[] for i in range(len(nums))]
        
        for n in nums:
            res[freq[n]].append(n)
            freq[n] += 1
        
        
        while not res[-1]:
            res.pop()
        
        return res
        
        
#         res = []
#         while nums:
#             tmp = []
#             seen = set()
            
#             for n in nums:
#                 if n in seen:
#                     tmp.append(n)
#                 else:
#                     seen.add(n)
            
#             nums = tmp
#             res.append(list(seen))
        
#         return res
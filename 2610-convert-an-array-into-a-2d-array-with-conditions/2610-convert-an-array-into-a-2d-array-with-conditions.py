class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        while nums:
            tmp = []
            seen = set()
            
            for n in nums:
                if n in seen:
                    tmp.append(n)
                else:
                    seen.add(n)
            
            nums = tmp
            res.append(list(seen))
        
        return res
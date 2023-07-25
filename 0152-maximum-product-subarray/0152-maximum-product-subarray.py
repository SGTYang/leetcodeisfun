class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxP, minP = 1, 1
        
        for n in nums:
            if n == 0:
                maxP, minP = 1, 1
                continue
            temp = maxP*n
            maxP = max(maxP*n, minP*n, n)
            minP = min(temp, minP*n, n)
            res = max(res, maxP)
        
        return res
    
        res = max(nums)
        curr_max = 1
        curr_min = 1
        
        for n in nums:
            if n == 0:
                curr_max = 1
                curr_min = 1
                continue
            tmp = curr_max * n
            curr_max = max(n, curr_max * n, curr_min * n)
            curr_min = max(n, tmp, curr_min * n)
            res = max(res, curr_max)
            
        return res
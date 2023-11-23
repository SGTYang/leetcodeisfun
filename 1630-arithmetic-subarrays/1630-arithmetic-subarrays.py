class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        
        for i in range(len(l)):
            start = l[i]
            end = r[i]
            elem = sorted(nums[start : end+1])
            is_arith = True
            if len(elem) >= 2:
                diff = elem[1] - elem[0]
                prev = elem[1]
                for j in range(2, len(elem)):
                    if elem[j] - prev != diff:
                        is_arith = False
                        break
                    prev = elem[j]
            res.append(is_arith)
        
        return res
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        
        for i in range(len(l)):
            start = l[i]
            end = r[i]
            q_range = nums[start : end+1]
            min_num = min(q_range)
            max_num = max(q_range)
            if (max_num - min_num) % (len(q_range) - 1) != 0:
                res.append(False)
                continue
            diff = (max_num - min_num) // (len(q_range) - 1)
            
            q_range_set = set(q_range)
            curr = min_num + diff
            is_arith = True
            while curr < max_num:
                if curr not in q_range_set:
                    is_arith = False
                    break
                curr += diff
            
            res.append(is_arith)
             
        return res
    
#############
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
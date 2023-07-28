class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.sort()
        secondList.sort()
        first_idx = 0
        second_idx = 0
        res = []
        
        while first_idx < len(firstList) and second_idx < len(secondList):
            first_start, first_end = firstList[first_idx]
            second_start, second_end = secondList[second_idx]
            
            overlap_start = max(first_start, second_start)
            overlap_end = min(first_end, second_end)
            
            if overlap_start <= overlap_end:
                res.append([overlap_start, overlap_end])
            
            if first_end < second_end:
                first_idx += 1
            else:
                second_idx += 1
        
        return res
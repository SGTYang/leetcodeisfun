class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.sort(key = lambda x : x[0])
        secondList.sort(key = lambda x: x[1])
        
        res = []
        
        first, second = 0, 0
        
        while first < len(firstList) and second < len(secondList):
            first_start, first_end = firstList[first]
            second_start, second_end = secondList[second]
            
            overlap_start, overlap_end = max(first_start, second_start), min(first_end, second_end)
            
            if overlap_start <= overlap_end:
                res.append([overlap_start, overlap_end])
            
            if first_end < second_end:
                first +=1
            else:
                second +=1
        
        return res
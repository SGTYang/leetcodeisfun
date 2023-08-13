class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()
        
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            for j in range(len(triplets[i])):
                if triplets[i][j] == target[j]:
                    res.add(j)
        
        return len(res) == 3
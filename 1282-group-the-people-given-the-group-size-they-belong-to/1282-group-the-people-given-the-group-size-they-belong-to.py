class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        group = defaultdict(list)
        for i in range(len(groupSizes)):
            curr_size = groupSizes[i]
            if not group[curr_size] or len(group[curr_size][-1]) == curr_size:
                group[curr_size].append([])
            group[curr_size][-1].append(i)
        
        for k,v in group.items():
            res += v
        
        return res
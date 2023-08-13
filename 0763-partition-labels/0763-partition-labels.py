class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, v in enumerate(s):
            last_index[v] = i
        res = []
        size = 0
        end = 0
        for i, v in enumerate(s):
            size += 1
            end = max(end, last_index[v])
            if i == end:
                res.append(size)
                size = 0
        
        return res
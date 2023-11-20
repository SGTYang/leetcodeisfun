class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        trash = defaultdict(int)
        last_idx = {}
        for i in range(len(garbage)):
            for c in garbage[i]:
                trash[c] += 1
                last_idx[c] = i
        
        res = 0
        
        for t, _ in last_idx.items():
            res += trash[t] + sum(travel[:last_idx[t]])
        
        return res
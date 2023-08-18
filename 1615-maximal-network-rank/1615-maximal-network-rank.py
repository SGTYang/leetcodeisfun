class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        cnt = defaultdict(int)
        connect = defaultdict(set)
        for s, e in roads:
            cnt[s] += 1
            cnt[e] += 1
            connect[s].add(e)
            connect[e].add(s)
        
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                overlap = -1 if j in connect[i] or i in connect[j] else 0
                res = max(res, cnt[i] + cnt[j] + overlap)
        return res
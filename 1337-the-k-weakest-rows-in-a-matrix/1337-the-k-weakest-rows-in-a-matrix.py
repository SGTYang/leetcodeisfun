class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = []
        for r in range(len(mat)):
            cnt = 0
            for c in range(len(mat[r])):
                if mat[r][c] == 1:
                    cnt += 1
            heapq.heappush(min_heap, (cnt, r))
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res
                    
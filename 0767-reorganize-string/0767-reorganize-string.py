class Solution:
    def reorganizeString(self, s: str) -> str:
        s_cnt = Counter(s)
        max_heap = [[-cnt, char] for char, cnt in s_cnt.items()]
        res = ""
        prev = None
        heapq.heapify(max_heap)
        
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            cnt, char = heapq.heappop(max_heap)
            res += char
            cnt += 1
            
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        
        return res
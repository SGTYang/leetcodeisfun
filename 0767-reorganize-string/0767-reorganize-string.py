class Solution:
    def reorganizeString(self, s: str) -> str:
        s_cnt = Counter(s)
        
        max_heap = [[-cnt, char] for char, cnt in s_cnt.items()]
        heapq.heapify(max_heap) # O(N)
        prev = None
        res = ""
        
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            cnt, char = heapq.heappop(max_heap)
            cnt += 1
            res += char
            
            if prev:
                heapq.heappush(max_heap, prev)
            
            if cnt != 0:
                prev = [cnt, char]
            else:
                prev = None
        
        return res
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(n * m)
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        que = deque()
        time = 0
        
        while max_heap or que:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    que.append([cnt, time + n])
                
            if que and que[0][1] == time:
                cnt, _ = que.popleft()
                heapq.heappush(max_heap, cnt)
        
        return time
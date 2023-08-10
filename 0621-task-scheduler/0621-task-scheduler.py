class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(n * m)
        count = Counter(tasks)
        max_heap = [[-cnt, task] for task, cnt in count.items()]
        heapq.heapify(max_heap)
        time = 0
        que = deque([])
        
        while max_heap or que:
            if max_heap:
                cnt, task = heapq.heappop(max_heap)
                if cnt + 1 != 0:
                    que.append([cnt + 1, task, time + n])
                
            if que and que[0][2] == time:
                cnt, task, _ = que.popleft()
                heapq.heappush(max_heap, [cnt, task])
                
            time += 1
        
        return time
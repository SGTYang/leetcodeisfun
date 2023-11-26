class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(n * m)
        
        cnt = defaultdict(int)
        for task in tasks:
            cnt[task] += 1
        
        heap = []
        stack = deque([])
        for c in cnt.values():
            heapq.heappush(heap, (-c, 0))
        
        time = 0
        
        while True:
            if heap:
                task_cnt, t = heapq.heappop(heap)
                task_cnt += 1
                if task_cnt < 0:
                    stack.append((task_cnt, time + n))
                    
            if stack and stack[0][1] == time:
                heapq.heappush(heap, stack.popleft())
            time += 1
            if not heap and not stack:
                break
        
        return time
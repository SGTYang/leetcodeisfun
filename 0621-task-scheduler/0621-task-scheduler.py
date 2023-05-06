class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        que = deque([])
        
        while maxHeap or que:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    que.append([cnt, time+n])
            if que and que[0][1] == time:
                heapq.heappush(maxHeap, que.popleft()[0])
        
        return time
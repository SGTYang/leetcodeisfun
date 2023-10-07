class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque([])
        res = []
        
        for i in range(k):
            while que and nums[que[-1]] < nums[i]:
                que.pop()
            
            que.append(i)
        res.append(nums[que[0]])
        l = 1
        
        for i in range(k, len(nums)):
            while que and nums[que[-1]] < nums[i]:
                que.pop()
            que.append(i)
            
            while l > que[0]:
                que.popleft()
            l += 1
            res.append(nums[que[0]])
        
        return res
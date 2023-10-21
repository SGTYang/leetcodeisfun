class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        maxSum = nums[0]
        que = deque()

        for i in range(len(nums)):
            nums[i] += que[0] if que else 0
            maxSum = max(maxSum, nums[i])

            while que and nums[i] > que[-1]:
                que.pop()

            if nums[i] > 0:
                que.append(nums[i])

            if i >= k and que and que[0] == nums[i - k]:
                que.popleft()

        return maxSum
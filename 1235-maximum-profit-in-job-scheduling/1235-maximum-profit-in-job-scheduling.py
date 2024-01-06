class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime) 
        intervals = sorted([(startTime[i], endTime[i], profit[i]) for i in range(n)], key=lambda ival: ival[1])
        dp = [0] * (n + 1)

        def findSubproblem(startVal):
            low, high = 0, n
            ret = -1
            while low <= high:
                mid = low + (high - low) // 2
                if intervals[mid][1] <= startVal:
                    ret = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ret + 1

        for i in range(1, n + 1):
            st = intervals[i - 1][0]
            dp[i] = dp[i - 1]
            dp[i] = max(dp[i], intervals[i-1][2] + dp[findSubproblem(st)])

        return dp[n]

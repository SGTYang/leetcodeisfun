class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        new = list(zip(nums, cost))
        new.sort(key=lambda x: x[0])

        s1, s2 = 0, 0
        dx, sx = [0], [0]
        N = len(cost)

        for i in range(N-1):
            s1 += new[i][1]
            s2 += new[-i-1][1]

            dx.append(dx[-1]+(new[i+1][0]-new[i][0])*s1)
            sx.append(sx[-1]+(new[-i-1][0]-new[-i-2][0])*s2)

        ans = float("inf")
        for i in range(N):
            ans = min(ans, dx[i]+sx[-i-1])

        return ans
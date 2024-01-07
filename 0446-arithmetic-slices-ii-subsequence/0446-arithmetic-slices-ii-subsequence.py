class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        nums2mp = collections.defaultdict(list)
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i, num in enumerate(nums):
            nums2mp[num].append(i)

        for i in range(n):
            for j in range(i):
                prev = 2 * nums[j] - nums[i]
                if prev > sys.maxsize or prev < -sys.maxsize - 1:
                    continue
                prev_indices = nums2mp.get(prev, [])
                for k in prev_indices:
                    if k >= j:
                        break
                    dp[i][j] += dp[j][k] + 1
                res += dp[i][j]
        return res
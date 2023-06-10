class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calc_sum(cnt, end):
            if cnt == 0:
                return 0
            start = max(end - cnt, 0)
            sum1 = end * (1 + end) // 2
            sum2 = start * (1 + start) // 2
            return sum1 - sum2

        maxSum -= n
        l, r = 0, maxSum
        while l <= r:
            mid = (l + r) // 2
            left_sum = calc_sum(index + 1, mid)
            right_sum = calc_sum(n - index - 1, mid - 1)
            if left_sum + right_sum <= maxSum:
                l = mid + 1
            else:
                r = mid - 1
        return l
        
        # brutal force solution
        def dfs(num_array, total_sum):
            if len(num_array) > n or total_sum > maxSum or num_array[-1] < 0:
                return 0
            
            if len(num_array) == n:
                print(num_array)
                return num_array[index]

            res = 0
            
            for p in [-1,0,1]:
                bound = p + num_array[-1]
                num_array.append(bound)
                res = max(res, dfs(num_array, total_sum + bound))
                num_array.pop()
            
            return res
        
        ans = 0
        for i in range(1,maxSum+1):
            ans = max(ans, dfs([i], i))
        return ans
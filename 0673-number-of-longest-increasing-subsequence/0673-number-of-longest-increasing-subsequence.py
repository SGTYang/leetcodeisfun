class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        len_lis, res = 0, 0
        
        for i in range(len(nums)-1, -1, -1):
            max_len, max_cnt = 1, 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    length, count = dp[j]
                    if length + 1 > max_len:
                        max_len, max_cnt = length + 1, count
                    elif length + 1 == max_len:
                        max_cnt += count
                        
            if max_len > len_lis:
                len_lis, res = max_len, max_cnt
            elif max_len == len_lis:
                res += max_cnt
            
            dp[i] = [max_len, max_cnt]
        
        return res
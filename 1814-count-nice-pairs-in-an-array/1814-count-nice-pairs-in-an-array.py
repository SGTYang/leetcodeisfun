class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        sub = []
        for i in range(len(nums)):
            num = nums[i]
            rev = 0
            while num:
                rev = rev * 10 + num % 10
                num = num // 10
            
            sub.append(nums[i] - rev)

        cnt = defaultdict(int)
        res = 0
        for num in sub:
            res = (res + cnt[num]) % MOD
            cnt[num] += 1
        
        return res
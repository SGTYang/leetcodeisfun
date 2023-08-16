class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time: O(n * m)
        # Space: O(n)  
#         dp = [False] * (len(s) + 1)
#         dp[-1] = True
        
#         for i in range(len(s) - 1, -1, -1):
#             for word in wordDict:
#                 if i + len(word) <= len(s) and s[i:i+len(word)] == word:
#                     dp[i] = dp[i + len(word)]
#                 if dp[i]:
#                     break
        
#         return dp[0]
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)+1):
            for word in wordDict:
                if i - len(word) >= 0 and s[i - len(word):i] == word:
                    dp[i] = dp[i - len(word)]
                if dp[i]:
                    break
        
        return dp[-1]
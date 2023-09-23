class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def dfs(word):
            if word not in dp:
                return 0
            if not dp[word]:
                dp[word] = max([dfs(word[:i]+word[i+1:]) + 1 for i in range(len(word))])
            return dp[word]
			
        dp = {word: None for word in words}
        return max([dfs(word) for word in dp if not dp[word]])
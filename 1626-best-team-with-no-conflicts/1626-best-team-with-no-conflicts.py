class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        pairs = list(zip(scores, ages))
        
        pairs.sort(key = lambda x: (x[0],x[1]))
        
        dp = [pairs[i][0] for i in range(len(pairs))]
        
        for i in range(len(pairs)):
            curr_score, curr_age = pairs[i]
            for j in range(i):
                score, age = pairs[j]
                
                if curr_age >= age:
                    dp[i] = max(dp[j]+curr_score, dp[i])
                    
        return max(dp)
            
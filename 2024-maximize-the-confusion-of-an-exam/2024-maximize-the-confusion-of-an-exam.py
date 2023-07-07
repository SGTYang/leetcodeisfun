class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def fn(target): 
            """Return max consecutive target."""
            ans = cnt = ii = 0 
            for i, x in enumerate(answerKey): 
                if x == target: cnt += 1 
                while cnt > k: 
                    if answerKey[ii] == target: cnt -= 1
                    ii += 1
                ans = max(ans, i - ii + 1)
            return ans 
        
        return max(fn("T"), fn("F"))
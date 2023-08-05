class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Time: O(2*n*2^2*n)
        # Space: O(2*n)
        res = []
        
        def dfs(curr, cnt):
            if cnt["("] == n and cnt[")"] == n:
                res.append("".join(curr))
                return
            if cnt[")"] > n or cnt["("] < cnt[")"] or cnt["("] > n:
                return
            curr.append("(")
            cnt["("] += 1
            dfs(curr, cnt)
            curr.pop()
            cnt["("] -= 1
            
            curr.append(")")
            cnt[")"] += 1
            dfs(curr, cnt)
            curr.pop()
            cnt[")"] -= 1
        
        dfs([], defaultdict(int))
        return res
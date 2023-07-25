class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(curr, count):
            if count[")"] > count["("] or count["("] > n or count[")"] > n:
                return
            if count["("] == n and count[")"] == n:
                res.append("".join(curr))
                return

            count["("] += 1
            curr.append("(")
            dfs(curr, count)
            count["("] -= 1
            curr.pop()
            
            count[")"] += 1
            curr.append(")")
            dfs(curr, count)
            curr.pop()
            count[")"] -= 1
        
        dfs([], defaultdict(int))
        
        return res
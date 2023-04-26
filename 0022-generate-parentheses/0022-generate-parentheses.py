class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        
        def backtrack(openP,closedP):
            if openP == closedP == n:
                res.append("".join(curr))
                return
            
            if openP < n:
                curr.append("(")
                backtrack(openP+1, closedP)
                curr.pop()
            if closedP < openP:
                curr.append(")")
                backtrack(openP, closedP+1)
                curr.pop()
        
        backtrack(0,0)
        return res
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        curr = []
        num_list = [i+1 for i in range(9)]
        
        def backtrack(idx,total):
            if total > n or len(curr) > k:
                return
            
            if len(curr) == k and total == n:
                res.append(curr.copy())
                return

            for i in range(idx,9):
                curr.append(num_list[i])
                backtrack(i+1, total+num_list[i])
                curr.pop()
        
        backtrack(0,0)
        return res